#!/usr/bin/env python3

import copy
import logging
import sys
import os
import pathlib
import re
import socket
import threading
import queue
from functools import partial

import pytest
from unittest import mock

import mecademicpy.robot as mdr
import mecademicpy.mx_robot_def as mx_def
import mecademicpy.robot_trajectory_files as robot_files

TEST_IP = '127.0.0.1'
MECA500_CONNECTED_RESPONSE = 'Connected to Meca500 R3 v9.0.0'
MECA500_CONNECTED_RESPONSE_LEGACY = 'Connected to Meca500 R3 v8.0.0'
MECA500_CONNECTED_RESPONSE_SCARA = 'Connected to Scara R1-virtual v9.0.0'
MECA500_SERIAL = 'm500-99999999'
SCARA_SERIAL = 'scara-87654321'
DEFAULT_TIMEOUT = 10  # Set 10s as default timeout.

#####################################################################################
# Test readme
#####################################################################################

# Use the 'robot' test fixture to automatically instantiate a robot object.

# Using the 'robot' fixture also enables automatically calling robot.Disconnect() at
# test teardown.

# Use 'connect_robot_helper(robot, args..)' to take care of robot connection.

# Refer to the 'test_start_offline_program()' test case for an example usage that
# also includes using `simple_response_handler()` to test a message exchange.

#####################################################################################
# Test fixtures and helper functions
#####################################################################################


# Fixture for creating robot object and also disconnecting on test teardown.
@pytest.fixture
def robot():
    robot = mdr.Robot()
    assert robot is not None

    # Yield the robot setup function.
    yield robot

    # Finally disconnect on teardown.
    robot.Disconnect()


# Automates sending the welcome message and responding to the robot serial query. Do not use for monitor_mode=True.
def connect_robot_helper(robot: mdr.Robot,
                         monitor_mode=False,
                         offline_mode=True,
                         disconnect_on_exception=False,
                         enable_synchronous_mode=False,
                         supports_rt_monitoring=True,
                         is_scara=False):

    # Prepare connection messages like the one that the robot should send upon connetion
    if is_scara:
        connected_msg = MECA500_CONNECTED_RESPONSE_SCARA
        supports_rt_monitoring = True
    elif supports_rt_monitoring:
        connected_msg = MECA500_CONNECTED_RESPONSE
    else:
        connected_msg = MECA500_CONNECTED_RESPONSE_LEGACY

    if monitor_mode:
        robot._monitor_rx_queue.put(mdr._Message(mx_def.MX_ST_CONNECTED, connected_msg))
    else:
        robot._command_rx_queue.put(mdr._Message(mx_def.MX_ST_CONNECTED, connected_msg))

    expected_commands = []
    robot_responses = []
    if not monitor_mode:
        # Prepare expected responses to "Get" requests that the Robot class does automatically while connecting
        expected_commands.append('GetRobotSerial')
        if is_scara:
            robot_responses = [mdr._Message(mx_def.MX_ST_GET_ROBOT_SERIAL, SCARA_SERIAL)]
        else:
            robot_responses = [mdr._Message(mx_def.MX_ST_GET_ROBOT_SERIAL, MECA500_SERIAL)]
        if supports_rt_monitoring:
            expected_commands.append('GetRealTimeMonitoring')
            robot_responses.append(mdr._Message(mx_def.MX_ST_GET_REAL_TIME_MONITORING, ''))
            expected_commands.append('SetCtrlPortMonitoring')
            robot_responses.append(mdr._Message(mx_def.MX_ST_SET_CTRL_PORT_MONIT, ''))

    # Start the fake robot thread (that will simulate response to expected requests)
    fake_robot = threading.Thread(target=simple_response_handler,
                                  args=(robot._command_tx_queue, robot._command_rx_queue, expected_commands,
                                        robot_responses))

    fake_robot.start()

    robot.Connect(TEST_IP,
                  offline_mode=offline_mode,
                  disconnect_on_exception=disconnect_on_exception,
                  enable_synchronous_mode=enable_synchronous_mode,
                  monitor_mode=monitor_mode)

    fake_robot.join()

    robot.WaitConnected(timeout=0)


# Function for exchanging one message with queue.
def simple_response_handler(queue_in, queue_out, expected_in, desired_out):
    if isinstance(expected_in, list):
        for i in range(len(expected_in)):
            event = queue_in.get(block=True, timeout=1)
            assert event == expected_in[i]
            queue_out.put(desired_out[i])

    else:
        event = queue_in.get(block=True, timeout=1)
        assert event == expected_in
        queue_out.put(desired_out)


# Server to listen for a connection. Send initial data in data_list on connect, send rest in response to any msg.
def fake_server(address, port, data_list, server_up):
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.settimeout(1)  # Allow up to 1 second to create the connection.
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind((address, port))
    server_sock.listen()
    server_up.set()

    client, addr = server_sock.accept()

    if data_list:
        client.sendall(data_list.pop(0).encode('ascii'))

    while True:
        received_data = client.recv(1024)
        if not received_data:
            break
        if data_list:
            client.sendall(data_list.pop(0).encode('ascii'))


# Run the fake_server in a separate thread.
def run_fake_server(address, port, data_list):
    server_up_event = threading.Event()  # Synchronization event for fake server.
    server_thread = threading.Thread(target=fake_server, args=(address, port, data_list, server_up_event))
    server_thread.start()
    assert server_up_event.wait(timeout=DEFAULT_TIMEOUT)
    return server_thread


# Simulated socket, initialized with list of responses, one response at a time is returned with recv().
class FakeSocket():

    def __init__(self, input):
        self.queue = queue.Queue()
        for x in input:
            self.queue.put(x)

    def setblocking(self, _):
        pass

    def recv(self, _):
        return self.queue.get()


#####################################################################################
# Test cases
#####################################################################################


# Test that connecting with invalid parameters raises exception.
def test_setup_invalid_input(robot: mdr.Robot):

    with pytest.raises(TypeError):
        robot.Connect(2)
    with pytest.raises(ValueError):
        robot.Connect('1.1.1.1.1')


# Test that connecting without robot will raise exception. On failure, first check that virtual robot is not running!
def test_connection_no_robot(robot: mdr.Robot):
    robot.default_timeout = 0

    with pytest.raises(mdr.CommunicationError):
        robot.Connect(TEST_IP)


# Test connection/disconnection cycle with real socket. On failure, first check that virtual robot is not running!
def test_successful_connection_full_socket(robot: mdr.Robot):

    command_server_thread = run_fake_server(
        TEST_IP, mx_def.MX_ROBOT_TCP_PORT_CONTROL,
        ['[3000][Connected to Meca500 R3-virtual v9.1.0]\0', '[2083][m500-99999]\0', '[2117][]\0'])

    with pytest.raises(mdr.TimeoutException):
        robot.WaitConnected(timeout=0)

    robot.Connect(TEST_IP)
    robot.WaitConnected()

    assert robot.GetRobotInfo().model == 'Meca500'
    assert robot.GetRobotInfo().revision == 3
    assert robot.GetRobotInfo().is_virtual is True
    assert robot.GetRobotInfo().fw_major_rev == 9
    assert robot.GetRobotInfo().fw_minor_rev == 1
    assert robot.GetRobotInfo().fw_patch_num == 0
    assert robot.GetRobotInfo().serial == 'm500-99999'

    robot.Disconnect()
    assert robot._command_socket is None
    assert robot._monitor_socket is None

    command_server_thread.join()


# Test connection/disconnection cycle with real socket simulating a legacy robot.
# **** On failure, first check that virtual robot is not running!
def test_successful_connection_full_socket_legacy(robot: mdr.Robot):

    command_server_thread = run_fake_server(
        TEST_IP, mx_def.MX_ROBOT_TCP_PORT_CONTROL,
        ['[3000][Connected to Meca500 R3-virtual v8.3.10]\0', '[2083][m500-99999]\0'])
    monitor_server_thread = run_fake_server(TEST_IP, mx_def.MX_ROBOT_TCP_PORT_FEED, [])

    with pytest.raises(mdr.TimeoutException):
        robot.WaitConnected(timeout=0)

    robot.Connect(TEST_IP)
    robot.WaitConnected()

    assert robot.GetRobotInfo().model == 'Meca500'
    assert robot.GetRobotInfo().revision == 3
    assert robot.GetRobotInfo().is_virtual is True
    assert robot.GetRobotInfo().fw_major_rev == 8
    assert robot.GetRobotInfo().fw_minor_rev == 3
    assert robot.GetRobotInfo().fw_patch_num == 10
    assert robot.GetRobotInfo().serial == 'm500-99999'

    robot.Disconnect()
    assert robot._command_socket is None
    assert robot._monitor_socket is None

    command_server_thread.join()
    monitor_server_thread.join()


# Test that the socket handler properly concatenates messages split across multiple recv() calls.
def test_successful_connection_split_response():
    fake_socket = FakeSocket([b'[3', b'00', b'0][Connected to Meca500 R3 v9.0.0]\0', b''])
    rx_queue = queue.Queue()

    # Test the socket handler directly to ensure messages are received across several recv() calls.
    mdr.Robot._handle_socket_rx(fake_socket, rx_queue, logging.getLogger(__name__))

    assert rx_queue.qsize() == 1
    message = rx_queue.get()
    assert message.id == mx_def.MX_ST_CONNECTED
    assert message.data == MECA500_CONNECTED_RESPONSE


# Test that we can connect to a Scara robot.
def test_scara_connection(robot: mdr.Robot):
    connect_robot_helper(robot, is_scara=True)
    assert not robot.GetStatusRobot().activation_state
    assert robot.GetRobotInfo().model == 'Scara'
    assert robot.GetRobotInfo().num_joints == 4
    assert robot.GetRobotInfo().fw_major_rev == 9
    assert robot.GetRobotInfo().rt_message_capable
    assert robot.GetRobotInfo().serial == SCARA_SERIAL


# Ensure user can reconnect to robot after disconnection or failure to connect.
def test_sequential_connections(robot: mdr.Robot):

    robot._command_rx_queue.put(mdr._Message(mx_def.MX_ST_USER_ALREADY, ''))
    with pytest.raises(Exception):
        robot.Connect(TEST_IP, offline_mode=True, disconnect_on_exception=False)

    robot._command_rx_queue.put(mdr._Message(99999, ''))
    with pytest.raises(Exception):
        robot.Connect(TEST_IP, offline_mode=True, disconnect_on_exception=False)

    connect_robot_helper(robot)
    robot.Disconnect()

    connect_robot_helper(robot)
    robot.Disconnect()


def test_monitoring_connection(robot: mdr.Robot):
    robot._monitor_rx_queue.put(mdr._Message(99999, ''))
    robot._monitor_rx_queue.put(mdr._Message(99999, ''))
    robot._monitor_rx_queue.put(mdr._Message(99999, ''))
    robot._monitor_rx_queue.put(mdr._Message(99999, ''))
    # Make sure robot connects quickly even if many messages preceding connection message are on monitoring port
    connect_robot_helper(robot)
    robot.WaitConnected(timeout=0)


# Ensure user can wrap robot object within "with" block.
def test_with_block(robot: mdr.Robot):
    called_callbacks = []

    def on_connected_test():
        called_callbacks.append('on_connected_test')

    def on_disconnected_test():
        called_callbacks.append('on_disconnected_test')

    with mdr.Robot() as robot2:
        callbacks = mdr.RobotCallbacks()
        callbacks.on_connected = on_connected_test
        callbacks.on_disconnected = on_disconnected_test
        robot2.RegisterCallbacks(callbacks, run_callbacks_in_separate_thread=True)

        # Simulate a connection
        connect_robot_helper(robot2)

    # Test that connection occurred, and disconnection too (at end of "with" block)
    assert called_callbacks == ['on_connected_test', 'on_disconnected_test']


# Ensure user can wrap robot object within "with" block on an already existing robot
def test_with_block_twice(robot: mdr.Robot):
    called_callbacks = []

    def on_connected_test():
        called_callbacks.append('on_connected_test')

    def on_disconnected_test():
        called_callbacks.append('on_disconnected_test')

    # Create robot and attach callbacks
    robot2 = mdr.Robot()
    callbacks = mdr.RobotCallbacks()
    callbacks.on_connected = on_connected_test
    callbacks.on_disconnected = on_disconnected_test
    robot2.RegisterCallbacks(callbacks, run_callbacks_in_separate_thread=True)

    # Connect within 'with' block -> Should disconnect but keep callbacks attached
    with robot2:
        connect_robot_helper(robot2)

    # Connect again 'with' block -> Should disconnect but keep callbacks attached
    with robot2:
        connect_robot_helper(robot2)

    # Test that connection occurred, and disconnection too (at end of "with" block)
    assert called_callbacks == [
        'on_connected_test', 'on_disconnected_test', 'on_connected_test', 'on_disconnected_test'
    ]


# Ensure robot must not yet be connected when entering "with" block.
def test_with_pre_connected(robot: mdr.Robot):
    robot2 = mdr.Robot()
    connect_robot_helper(robot2)
    with pytest.raises(mdr.InvalidStateError):
        with robot2:
            robot2.Disconnect()


# Test parsing of monitoring port messages, and that robot state is correctly updated.
def test_monitoring_connection(robot: mdr.Robot):
    connect_robot_helper(robot, monitor_mode=True)

    # Helper functions for generating test data. To ensure data is unique in each field, we add the response code to the
    # 'seed' array, with is generated with range().
    def make_test_array(code, data):
        return [x + code for x in data]

    # Convert the test array into a TimestampedData object.
    def make_test_data(code, data):
        test_array = make_test_array(code, data)
        return mdr.TimestampedData(test_array[0], test_array[1:])

    # Convert the test array into a Message object.
    def make_test_message(code, data):
        test_array = make_test_array(code, data)
        return mdr._Message(code, ','.join([str(x) for x in test_array]))

    # Send monitor messages.
    robot._monitor_rx_queue.put(make_test_message(mx_def.MX_ST_RT_TARGET_JOINT_POS, range(7)))
    robot._monitor_rx_queue.put(make_test_message(mx_def.MX_ST_RT_TARGET_CART_POS, range(7)))
    robot._monitor_rx_queue.put(make_test_message(mx_def.MX_ST_RT_TARGET_JOINT_VEL, range(7)))
    robot._monitor_rx_queue.put(make_test_message(mx_def.MX_ST_RT_TARGET_CART_VEL, range(7)))

    robot._monitor_rx_queue.put(make_test_message(mx_def.MX_ST_RT_TARGET_CONF, range(4)))
    robot._monitor_rx_queue.put(make_test_message(mx_def.MX_ST_RT_TARGET_CONF_TURN, range(2)))

    robot._monitor_rx_queue.put(make_test_message(mx_def.MX_ST_RT_JOINT_POS, range(7)))
    robot._monitor_rx_queue.put(make_test_message(mx_def.MX_ST_RT_CART_POS, range(7)))
    robot._monitor_rx_queue.put(make_test_message(mx_def.MX_ST_RT_JOINT_VEL, range(7)))
    robot._monitor_rx_queue.put(make_test_message(mx_def.MX_ST_RT_JOINT_TORQ, range(7)))
    robot._monitor_rx_queue.put(make_test_message(mx_def.MX_ST_RT_CART_VEL, range(7)))

    robot._monitor_rx_queue.put(make_test_message(mx_def.MX_ST_RT_CONF, range(4)))
    robot._monitor_rx_queue.put(make_test_message(mx_def.MX_ST_RT_CONF_TURN, range(2)))

    robot._monitor_rx_queue.put(make_test_message(mx_def.MX_ST_RT_ACCELEROMETER, range(5)))

    robot.Disconnect()

    # Temporarily test using direct members, switch to using proper getters once implemented.
    assert robot._robot_kinematics.rt_target_joint_pos == make_test_data(mx_def.MX_ST_RT_TARGET_JOINT_POS, range(7))
    assert robot._robot_kinematics.rt_target_cart_pos == make_test_data(mx_def.MX_ST_RT_TARGET_CART_POS, range(7))
    assert robot._robot_kinematics.rt_target_joint_vel == make_test_data(mx_def.MX_ST_RT_TARGET_JOINT_VEL, range(7))
    assert robot._robot_kinematics.rt_target_cart_vel == make_test_data(mx_def.MX_ST_RT_TARGET_CART_VEL, range(7))
    assert robot._robot_kinematics.rt_target_conf == make_test_data(mx_def.MX_ST_RT_TARGET_CONF, range(4))
    assert robot._robot_kinematics.rt_target_conf_turn == make_test_data(mx_def.MX_ST_RT_TARGET_CONF_TURN, range(2))

    assert robot._robot_kinematics.rt_joint_pos == make_test_data(mx_def.MX_ST_RT_JOINT_POS, range(7))
    assert robot._robot_kinematics.rt_cart_pos == make_test_data(mx_def.MX_ST_RT_CART_POS, range(7))
    assert robot._robot_kinematics.rt_joint_vel == make_test_data(mx_def.MX_ST_RT_JOINT_VEL, range(7))
    assert robot._robot_kinematics.rt_joint_torq == make_test_data(mx_def.MX_ST_RT_JOINT_TORQ, range(7))
    assert robot._robot_kinematics.rt_cart_vel == make_test_data(mx_def.MX_ST_RT_CART_VEL, range(7))
    assert robot._robot_kinematics.rt_conf == make_test_data(mx_def.MX_ST_RT_CONF, range(4))
    assert robot._robot_kinematics.rt_conf_turn == make_test_data(mx_def.MX_ST_RT_CONF_TURN, range(2))

    # The data is sent as [timestamp, accelerometer_id, {measurements...}].
    # We convert it to a dictionary which maps the accelerometer_id to a TimestampedData object.
    accel_array = make_test_array(mx_def.MX_ST_RT_ACCELEROMETER, range(5))
    assert robot._robot_kinematics.rt_accelerometer == {
        accel_array[1]: mdr.TimestampedData(accel_array[0], accel_array[2:])
    }


# Test that checkpoints created by user are properly sent to robot, waited on, and unblocked.
def test_user_set_checkpoints(robot: mdr.Robot):
    connect_robot_helper(robot)

    # Validate internal checkpoint waiting.
    checkpoint_1 = robot.SetCheckpoint(1)
    # Check that the command is sent to the robot.
    assert robot._command_tx_queue.get() == 'SetCheckpoint(1)'
    # Check that the id is correct.
    assert checkpoint_1.id == 1
    # Check that wait times out if response has not been sent.
    with pytest.raises(mdr.TimeoutException):
        checkpoint_1.wait(timeout=0)
    robot._command_rx_queue.put(mdr._Message(mx_def.MX_ST_CHECKPOINT_REACHED, '1'))
    # Check that wait succeeds if response is sent.
    checkpoint_1.wait(timeout=DEFAULT_TIMEOUT)


# Test that the user can wait on checkpoints which were set by an external source, like an offline program.
def test_external_checkpoints(robot: mdr.Robot):
    connect_robot_helper(robot)

    # Validate external checkpoint waiting.
    checkpoint_1 = robot.ExpectExternalCheckpoint(1)
    # Check that the command is not sent to the robot.
    assert robot._command_tx_queue.qsize() == 0
    # Check that the id is correct.
    assert checkpoint_1.id == 1
    # Check that wait times out if response has not been sent.
    with pytest.raises(mdr.TimeoutException):
        checkpoint_1.wait(timeout=0)
    robot._command_rx_queue.put(mdr._Message(mx_def.MX_ST_CHECKPOINT_REACHED, '1'))
    # Check that wait succeeds if response is sent.
    checkpoint_1.wait(timeout=DEFAULT_TIMEOUT)


# Test that user-set and external checkpoints work concurrently.
def test_multiple_checkpoints(robot: mdr.Robot):
    connect_robot_helper(robot)

    # Validate multiple checkpoints, internal and external.
    checkpoint_1 = robot.SetCheckpoint(1)
    checkpoint_2 = robot.SetCheckpoint(2)
    checkpoint_3 = robot.ExpectExternalCheckpoint(3)

    # All three checkpoints are still pending, check that all three time out.
    with pytest.raises(mdr.TimeoutException):
        checkpoint_1.wait(timeout=0)
    with pytest.raises(mdr.TimeoutException):
        checkpoint_2.wait(timeout=0)
    with pytest.raises(mdr.TimeoutException):
        checkpoint_3.wait(timeout=0)

    # First checkpoint is reached, second two should time out.
    robot._command_rx_queue.put(mdr._Message(mx_def.MX_ST_CHECKPOINT_REACHED, '1'))
    checkpoint_1.wait(timeout=DEFAULT_TIMEOUT)
    with pytest.raises(mdr.TimeoutException):
        checkpoint_2.wait(timeout=0)
    with pytest.raises(mdr.TimeoutException):
        checkpoint_3.wait(timeout=0)

    # First and second checkpoints are reached, last one should time out.
    robot._command_rx_queue.put(mdr._Message(mx_def.MX_ST_CHECKPOINT_REACHED, '2'))
    checkpoint_1.wait(timeout=DEFAULT_TIMEOUT)
    checkpoint_2.wait(timeout=DEFAULT_TIMEOUT)
    with pytest.raises(mdr.TimeoutException):
        checkpoint_3.wait(timeout=0)

    # All checkpoints are reached.
    robot._command_rx_queue.put(mdr._Message(mx_def.MX_ST_CHECKPOINT_REACHED, '3'))
    checkpoint_3.wait(timeout=DEFAULT_TIMEOUT)
    checkpoint_2.wait(timeout=DEFAULT_TIMEOUT)
    checkpoint_1.wait(timeout=DEFAULT_TIMEOUT)


# Test that repeated checkpoints are unblocked in the order they are set.
# Repeated checkpoints are supported but discouraged.
def test_repeated_checkpoints(robot: mdr.Robot):
    connect_robot_helper(robot)

    checkpoint_1_a = robot.SetCheckpoint(1)
    checkpoint_1_b = robot.SetCheckpoint(1)

    # Check that wait times out if response has not been sent.
    with pytest.raises(mdr.TimeoutException):
        checkpoint_1_a.wait(timeout=0)
    with pytest.raises(mdr.TimeoutException):
        checkpoint_1_b.wait(timeout=0)

    # Only one checkpoint has been returned, the second should still block.
    robot._command_rx_queue.put(mdr._Message(mx_def.MX_ST_CHECKPOINT_REACHED, '1'))
    with pytest.raises(mdr.TimeoutException):
        checkpoint_1_b.wait(timeout=0)
    checkpoint_1_a.wait(timeout=DEFAULT_TIMEOUT)

    # Check that waits succeeds if response is sent.
    robot._command_rx_queue.put(mdr._Message(mx_def.MX_ST_CHECKPOINT_REACHED, '1'))
    checkpoint_1_b.wait(timeout=DEFAULT_TIMEOUT)
    checkpoint_1_a.wait(timeout=DEFAULT_TIMEOUT)


# Test WaitForAnyCheckpoint().
def test_special_checkpoints(robot: mdr.Robot):
    connect_robot_helper(robot)

    checkpoint_1 = robot.SetCheckpoint(1)
    checkpoint_2 = robot.SetCheckpoint(2)

    with pytest.raises(mdr.TimeoutException):
        robot.WaitForAnyCheckpoint(timeout=0)

    robot._command_rx_queue.put(mdr._Message(mx_def.MX_ST_CHECKPOINT_REACHED, '1'))
    robot.WaitForAnyCheckpoint()


# Test that receiving a checkpoint without an associated wait does not raise exception.
def test_unaccounted_checkpoints(robot: mdr.Robot):
    connect_robot_helper(robot)

    # Send unexpected checkpoint.
    robot._command_rx_queue.put(mdr._Message(mx_def.MX_ST_CHECKPOINT_REACHED, '1'))

    # This call will raise an exception if internal states are invalid.
    robot._check_internal_states()


# Test that checkpoints which will never be unblocked raise an exception.
def test_stranded_checkpoints(robot: mdr.Robot):
    connect_robot_helper(robot)

    checkpoint_1 = robot.SetCheckpoint(1)

    robot.Disconnect()

    # Checkpoint should throw error instead of blocking since robot is already disconnected.
    with pytest.raises(mdr.InterruptException):
        checkpoint_1.wait(timeout=DEFAULT_TIMEOUT)


# Test that events can be correctly waited for and set.
def test_events(robot: mdr.Robot):
    with pytest.raises(mdr.TimeoutException):
        robot.WaitActivated(timeout=0)
    robot.WaitDeactivated()
    with pytest.raises(mdr.TimeoutException):
        robot.WaitConnected(timeout=0)
    robot.WaitDisconnected()

    connect_robot_helper(robot)

    robot.WaitConnected()
    with pytest.raises(mdr.TimeoutException):
        robot.WaitDisconnected(timeout=0)

    with pytest.raises(mdr.TimeoutException):
        robot.WaitActivated(timeout=0)
    robot.WaitDeactivated()

    robot.ActivateRobot()
    robot._command_rx_queue.put(mdr._Message(mx_def.MX_ST_GET_STATUS_ROBOT, '1,0,0,0,0,0,0'))

    robot.WaitActivated(timeout=1)
    with pytest.raises(mdr.TimeoutException):
        robot.WaitDeactivated(timeout=0)

    with pytest.raises(mdr.TimeoutException):
        robot.WaitHomed(timeout=0)
    robot.Home()
    robot._command_rx_queue.put(mdr._Message(mx_def.MX_ST_GET_STATUS_ROBOT, '1,1,0,0,0,0,0'))
    robot.WaitHomed(timeout=1)

    robot.PauseMotion()
    robot._command_rx_queue.put(mdr._Message(mx_def.MX_ST_GET_STATUS_ROBOT, '1,1,0,0,1,0,0'))
    # Wait until pause is successfully set.
    robot.WaitMotionPaused(timeout=DEFAULT_TIMEOUT)

    with pytest.raises(mdr.TimeoutException):
        robot.WaitMotionResumed(timeout=0)
    robot.ResumeMotion()
    robot._command_rx_queue.put(mdr._Message(mx_def.MX_ST_GET_STATUS_ROBOT, '1,1,0,0,0,0,0'))
    robot.WaitMotionResumed(timeout=1)

    robot.ClearMotion()
    robot._command_rx_queue.put(mdr._Message(mx_def.MX_ST_CLEAR_MOTION, ''))
    robot.WaitMotionCleared(timeout=1)

    robot._command_rx_queue.put(mdr._Message(mx_def.MX_ST_GET_STATUS_ROBOT, '1,1,0,0,0,1,0'))
    robot._robot_events.on_end_of_block.wait(timeout=1)

    # Robot enters error state.
    robot._command_rx_queue.put(mdr._Message(mx_def.MX_ST_GET_STATUS_ROBOT, '1,1,0,1,0,0,0'))
    robot._robot_events.on_error.wait(timeout=1)

    robot.ResetError()
    robot._command_rx_queue.put(mdr._Message(mx_def.MX_ST_GET_STATUS_ROBOT, '1,1,0,0,0,0,0'))
    robot._robot_events.on_error_reset.wait(timeout=1)

    robot.DeactivateRobot()
    robot._command_rx_queue.put(mdr._Message(mx_def.MX_ST_GET_STATUS_ROBOT, '0,0,0,0,0,0,0'))

    # Note: the order of these waits is intentional.
    # The WaitActivated check may fail if message hasn't yet been processed.
    robot.WaitDeactivated(timeout=1)
    with pytest.raises(mdr.TimeoutException):
        robot.WaitActivated(timeout=0)

    robot._command_rx_queue.put(mdr._Message(mx_def.MX_ST_BRAKES_OFF, ''))
    robot._robot_events.on_brakes_deactivated.wait(timeout=DEFAULT_TIMEOUT)

    robot._command_rx_queue.put(mdr._Message(mx_def.MX_ST_BRAKES_ON, ''))
    robot._robot_events.on_brakes_activated.wait(timeout=DEFAULT_TIMEOUT)

    with pytest.raises(mdr.TimeoutException):
        robot.WaitDisconnected(timeout=0)
    robot.Disconnect()
    robot.WaitDisconnected()


# Test that robot disconnects automatically on exception when feature is enabled.
def test_disconnect_on_exception(robot: mdr.Robot):

    connect_robot_helper(robot, disconnect_on_exception=True)

    with pytest.raises(mdr.DisconnectError):
        robot.SetCheckpoint(0)

    # Test that disabling the feature avoids the disconnect.
    robot.Disconnect()
    connect_robot_helper(robot, disconnect_on_exception=False)

    with pytest.raises(AssertionError):
        robot.SetCheckpoint(0)


# Test that callbacks can be set and are correctly called. Every callback in the RobotCallbacks class is checked.
# If a new callback is added, the test must be updated to trigger the callback.
def test_callbacks(robot: mdr.Robot):
    # Initialize object which will contain all user-defined callback functions.
    callbacks = mdr.RobotCallbacks()

    # Expect that almost all callbacks will be called
    expected_callbacks = copy.deepcopy(callbacks.__dict__)
    # ... except on_monitor_message since we're not connecting to monitoring port by default
    expected_callbacks.pop('on_monitor_message')

    # Create list to store names of callbacks which have been called.
    called_callbacks = []

    # Function to record which callbacks have been called.
    # To avoid writing a separate function for each callback, we take in a name parameter.
    # Just before the callback is assigned, we set the name to be the callback we currently care about.
    def test_callback(name):
        called_callbacks.append(name)

    # For each available callback 'slot', assign the 'test_callback' function, with the callback name as a parameter.
    for attr in callbacks.__dict__:
        callbacks.__dict__[attr] = partial(test_callback, name=attr)

    # Checkpoint callbacks are different than other callbacks, use different function.
    checkpoint_id = 123

    def checkpoint_callback(id):
        called_callbacks.append('on_checkpoint_reached')
        called_callbacks.append(id)

    callbacks.on_checkpoint_reached = checkpoint_callback

    # The two message callbacks are also unique.
    def command_message_callback(message):
        called_callbacks.append('on_command_message')

    def monitor_message_callback(message):
        called_callbacks.append('on_monitor_message')

    callbacks.on_command_message = command_message_callback
    callbacks.on_monitor_message = monitor_message_callback

    # End of cycle callback is alike on_monitor_message, as it also happens on a monitoring message, but less often
    def end_of_cycle_callback():
        called_callbacks.append('on_end_of_cycle')

    callbacks.on_end_of_cycle = end_of_cycle_callback

    for run_in_thread in [True]:
        # Register all callbacks.
        robot.RegisterCallbacks(callbacks, run_callbacks_in_separate_thread=run_in_thread)

        connect_robot_helper(robot, enable_synchronous_mode=True)

        robot._command_rx_queue.put(mdr._Message(mx_def.MX_ST_GET_STATUS_ROBOT, '1,0,0,0,0,0,0'))
        robot.ActivateRobot()

        robot._command_rx_queue.put(mdr._Message(mx_def.MX_ST_GET_STATUS_ROBOT, '1,1,0,0,0,0,0'))
        robot._command_rx_queue.put(mdr._Message(mx_def.MX_ST_RT_CYCLE_END, '12345'))
        robot.Home()

        robot.GetStatusRobot(synchronous_update=False)
        robot._command_rx_queue.put(mdr._Message(mx_def.MX_ST_GET_STATUS_ROBOT, '1,1,0,0,1,0,0'))

        robot.GetStatusGripper(synchronous_update=False)
        robot._command_rx_queue.put(mdr._Message(mx_def.MX_ST_GET_STATUS_GRIPPER, '0,0,0,0,0,0'))

        checkpoint_1 = robot.SetCheckpoint(checkpoint_id)
        robot._command_rx_queue.put(mdr._Message(mx_def.MX_ST_CHECKPOINT_REACHED, str(checkpoint_id)))

        robot._command_rx_queue.put(mdr._Message(mx_def.MX_ST_GET_STATUS_ROBOT, '1,1,0,0,1,0,0'))
        robot.PauseMotion()

        robot._command_rx_queue.put(mdr._Message(mx_def.MX_ST_GET_STATUS_ROBOT, '1,1,0,0,0,0,0'))
        robot.ResumeMotion()

        robot._command_rx_queue.put(mdr._Message(mx_def.MX_ST_CLEAR_MOTION, ''))
        # Note we don't actually run robot.ClearMotion() here as the command will block in synchronous mode.
        # It is also not necessary for the test.

        robot._command_rx_queue.put(mdr._Message(mx_def.MX_ST_OFFLINE_START, ''))
        # Note we don't actually run robot.StartOfflineProgram() here as there is no actual robot and thus
        # no recorded programs
        # It is also not necessary for the test.

        # Simulate end of cycle (detected on MX_ST_GET_POSE monitor message when robot is not 'rt_message_capable')
        robot._command_rx_queue.put(mdr._Message(mx_def.MX_ST_GET_POSE, '0.0,0.0,0.0,0.0,0.0,0.0'))

        # Robot enters error state.
        robot._command_rx_queue.put(mdr._Message(mx_def.MX_ST_GET_STATUS_ROBOT, '1,1,0,1,0,0,0'))

        robot._command_rx_queue.put(mdr._Message(mx_def.MX_ST_GET_STATUS_ROBOT, '1,1,0,0,0,0,0'))
        robot.ResetError()

        # Robot pstop triggered.
        robot._command_rx_queue.put(mdr._Message(mx_def.MX_ST_PSTOP, '1'))

        robot._command_rx_queue.put(mdr._Message(mx_def.MX_ST_PSTOP, '0'))
        robot.ResetPStop()

        robot._command_rx_queue.put(mdr._Message(mx_def.MX_ST_GET_STATUS_ROBOT, '1,1,1,0,0,0,0'))
        robot.ActivateSim()
        robot._command_rx_queue.put(mdr._Message(mx_def.MX_ST_GET_STATUS_ROBOT, '1,1,0,0,0,0,0'))
        robot.DeactivateSim()

        robot._command_rx_queue.put(mdr._Message(mx_def.MX_ST_OFFLINE_START, ''))

        robot._command_rx_queue.put(mdr._Message(mx_def.MX_ST_GET_STATUS_ROBOT, '0,0,0,0,0,0,0'))
        robot.DeactivateRobot()

        robot.Disconnect()

        if not run_in_thread:
            robot.RunCallbacks()

        robot.UnregisterCallbacks()

        # Check that all callbacks have been called.
        for attr in expected_callbacks:
            assert attr in called_callbacks, f'callback {attr} not called (called={called_callbacks})'

        assert checkpoint_id in called_callbacks

        assert robot._callback_thread is None


# Test unblocking InterruptableEvent class with exception.
def test_event_with_exception():
    # Test successful setting.
    event = mdr.InterruptableEvent()
    event.set()
    event.wait(timeout=0)

    # Test event timed out.
    event.clear()
    with pytest.raises(mdr.TimeoutException):
        event.wait(timeout=0)

    # Test event throwing exception.
    exception_event = mdr.InterruptableEvent()
    exception_event.abort()
    with pytest.raises(mdr.InterruptException):
        exception_event.wait(timeout=0)


# Test all motion commands except those in skip_list. Skipped commands do not follow standard motion command format, or
# their arguments cannot be deduced from the function signature.
def test_motion_commands(robot: mdr.Robot):
    connect_robot_helper(robot)

    skip_list = ['MoveGripper', 'MoveJoints', 'MoveJointsVel', 'MoveJointsRel']

    # Run all move-type commands in API and check that the text_command matches.
    for name in dir(robot):
        if name in skip_list:
            continue
        elif name.startswith('Move') or name.startswith('Set'):
            method = getattr(robot, name)

            # Assemble parameter list. Note we need to get the wrapped function since a decorator is used.
            num_args = method.__wrapped__.__code__.co_argcount
            test_args = list(range(1, num_args))
            test_args_text = ','.join([str(x) for x in test_args])

            # Call method.
            method(*test_args)

            text_command = robot._command_tx_queue.get(block=True, timeout=1)

            # Check that the text commands begins with the appropriate name.
            assert text_command.find(name) == 0, 'Method {} does not match text command'.format(name)

            # Check that the test arguments.
            assert text_command.find(test_args_text) != -1, 'Method {} args do not match text command'.format(name)


# Test that joint-type moves send the correct command and checks input.
def test_joint_moves(robot: mdr.Robot):
    connect_robot_helper(robot)

    test_args = [1, 2, 3, 4, 5, 6]
    test_args_text = ','.join([str(x) for x in test_args])

    robot.MoveJoints(*test_args)
    text_command = robot._command_tx_queue.get(block=True, timeout=1)
    assert text_command.find('MoveJoints') == 0
    assert text_command.find(test_args_text) != -1

    with pytest.raises(ValueError):
        robot.MoveJoints(1, 2, 3)

    robot.MoveJointsRel(*test_args)
    text_command = robot._command_tx_queue.get(block=True, timeout=1)
    assert text_command.find('MoveJointsRel') == 0
    assert text_command.find(test_args_text) != -1

    with pytest.raises(ValueError):
        robot.MoveJointsRel(1, 2, 3)

    robot.MoveJointsVel(*test_args)
    text_command = robot._command_tx_queue.get(block=True, timeout=1)
    assert text_command.find('MoveJointsVel') == 0
    assert text_command.find(test_args_text) != -1

    with pytest.raises(ValueError):
        robot.MoveJointsVel(1, 2, 3)


# Test get commands with synchronous_update=True.
def test_synchronous_gets(robot: mdr.Robot):
    connect_robot_helper(robot)

    # Test GetRtTargetJointPos.
    expected_commands = ['Sync(1)', 'GetRtTargetJointPos']
    robot_responses = []
    robot_responses.append(mdr._Message(mx_def.MX_ST_SYNC, '1'))
    robot_responses.append(mdr._Message(mx_def.MX_ST_RT_TARGET_JOINT_POS, '1234, 1, 2, 3, 4, 5, 6'))
    fake_robot = threading.Thread(target=simple_response_handler,
                                  args=(robot._command_tx_queue, robot._command_rx_queue, expected_commands,
                                        robot_responses))

    fake_robot.start()

    # Try synchronous get
    assert robot.GetRtTargetJointPos(synchronous_update=True, timeout=1) == [1, 2, 3, 4, 5, 6]

    # Also test get with timestamp
    expected_response = mdr.TimestampedData(1234, [1, 2, 3, 4, 5, 6])
    assert robot.GetRtTargetJointPos(include_timestamp=True, synchronous_update=False) == expected_response

    fake_robot.join()

    # Test GetRtTargetCartPos.
    expected_commands = ['Sync(2)', 'GetRtTargetCartPos']
    robot_responses = []
    robot_responses.append(mdr._Message(mx_def.MX_ST_SYNC, '2'))
    robot_responses.append(mdr._Message(mx_def.MX_ST_RT_TARGET_CART_POS, '2345, 2, 3, 4, 5, 6, 7'))
    fake_robot = threading.Thread(target=simple_response_handler,
                                  args=(robot._command_tx_queue, robot._command_rx_queue, expected_commands,
                                        robot_responses))

    fake_robot.start()

    # Try synchronous get
    assert robot.GetRtTargetCartPos(synchronous_update=True, timeout=1) == [2, 3, 4, 5, 6, 7]

    # Also test get with timestamp
    expected_response = mdr.TimestampedData(2345, [2, 3, 4, 5, 6, 7])
    assert robot.GetRtTargetCartPos(include_timestamp=True, synchronous_update=False) == expected_response

    fake_robot.join()

    # Attempting these gets without the appropriate robot response should result in timeout.

    with pytest.raises(mdr.TimeoutException):
        robot.GetRtTargetJointPos(synchronous_update=True, timeout=0)

    with pytest.raises(mdr.TimeoutException):
        robot.GetRtTargetCartPos(synchronous_update=True, timeout=0)


# Test that get commands correctly return timestamps.
def test_synchronous_gets_legacy(robot: mdr.Robot):
    # Use a connected response that indicate a robot that does not support real-time monitoring
    connect_robot_helper(robot, supports_rt_monitoring=False)

    # Helper functions for generating fake data.
    def fake_data(seed, length=6):
        return [seed] * length

    def fake_string(seed, length=6):
        return ','.join([str(x) for x in fake_data(seed, length)])

    #
    # Test legacy messages:
    #
    robot._monitor_rx_queue.put(mdr._Message(mx_def.MX_ST_GET_JOINTS, fake_string(1)))
    robot._monitor_rx_queue.put(mdr._Message(mx_def.MX_ST_GET_POSE, fake_string(1)))

    # Terminate queue and wait for thread to exit to ensure messages are processed.
    robot._monitor_rx_queue.put(mdr._TERMINATE)
    robot._monitor_handler_thread.join(timeout=5)
    robot._initialize_monitoring_connection()

    # Without RT messages, enabling 'include_timestamp' should raise exception.
    with pytest.raises(mdr.InvalidStateError):
        robot.GetRtTargetJointPos(include_timestamp=True)
    with pytest.raises(mdr.InvalidStateError):
        robot.GetRtTargetCartPos(include_timestamp=True)

    robot.GetRtTargetJointPos(include_timestamp=False) == fake_data(1)
    robot.GetRtTargetCartPos(include_timestamp=False) == fake_data(1)

    assert not robot.GetRobotInfo().rt_message_capable

    # Test synchronous gets without RT messages.
    expected_command = 'GetJoints'
    robot_response = mdr._Message(mx_def.MX_ST_GET_JOINTS, fake_string(2))
    fake_robot = threading.Thread(target=simple_response_handler,
                                  args=(robot._command_tx_queue, robot._command_rx_queue, expected_command,
                                        robot_response))

    fake_robot.start()

    assert robot.GetRtTargetJointPos(synchronous_update=True, timeout=1) == fake_data(2)
    fake_robot.join()

    expected_command = 'GetPose'
    robot_response = mdr._Message(mx_def.MX_ST_GET_POSE, fake_string(2))
    fake_robot = threading.Thread(target=simple_response_handler,
                                  args=(robot._command_tx_queue, robot._command_rx_queue, expected_command,
                                        robot_response))

    fake_robot.start()

    assert robot.GetRtTargetCartPos(synchronous_update=True, timeout=1) == fake_data(2)
    fake_robot.join()


# Test initializing offline programs.
def test_start_offline_program(robot: mdr.Robot):
    connect_robot_helper(robot, enable_synchronous_mode=True)

    expected_command = 'StartProgram(1)'

    # Report that the program has been started successfully.
    robot_response = mdr._Message(mx_def.MX_ST_OFFLINE_START, '')
    fake_robot = threading.Thread(target=simple_response_handler,
                                  args=(robot._command_tx_queue, robot._command_rx_queue, expected_command,
                                        robot_response))
    fake_robot.start()

    robot.StartOfflineProgram(1, timeout=1)

    fake_robot.join(timeout=1)

    # Report that the program does not exist.
    robot_response = mdr._Message(mx_def.MX_ST_NO_OFFLINE_SAVED, '')
    fake_robot = threading.Thread(target=simple_response_handler,
                                  args=(robot._command_tx_queue, robot._command_rx_queue, expected_command,
                                        robot_response))
    fake_robot.start()

    with pytest.raises(mdr.InvalidStateError):
        robot.StartOfflineProgram(1, timeout=1)

    fake_robot.join(timeout=1)


# Test monitor-only mode. (No commands can be sent.)
def test_monitor_mode(robot: mdr.Robot):

    robot._monitor_rx_queue.put(mdr._Message(mx_def.MX_ST_CONNECTED, MECA500_CONNECTED_RESPONSE))
    robot.Connect(TEST_IP,
                  monitor_mode=True,
                  offline_mode=True,
                  disconnect_on_exception=False,
                  enable_synchronous_mode=True)

    robot.WaitConnected(timeout=0)

    # Check that the Meca500 response was correctly parsed to have 6 joints.
    assert robot.GetRobotInfo().num_joints == 6

    # Send test messages.
    robot._monitor_rx_queue.put(mdr._Message(mx_def.MX_ST_RT_TARGET_JOINT_POS, '1234, 1, 2, 3, 4, 5, 6'))
    robot._monitor_rx_queue.put(mdr._Message(mx_def.MX_ST_RT_TARGET_CART_POS, '1234, 7, 8, 9, 10, 11, 12'))

    # Terminate queue and wait for thread to exit to ensure messages are processed.
    robot._monitor_rx_queue.put(mdr._TERMINATE)
    robot._monitor_handler_thread.join(timeout=5)

    # Check that these gets do not raise an exception.
    assert robot.GetRtTargetJointPos() == [1, 2, 3, 4, 5, 6]
    assert robot.GetRtTargetCartPos() == [7, 8, 9, 10, 11, 12]

    with pytest.raises(mdr.InvalidStateError):
        robot.MoveJoints(1, 2, 3, 4, 5, 6)


# Test the sending and receiving of custom commands.
def test_custom_command(robot: mdr.Robot):
    connect_robot_helper(robot)

    expected_command = 'TestCommand'
    robot_response = mdr._Message(mx_def.MX_ST_CMD_SUCCESSFUL, 'TestResponse')
    fake_robot = threading.Thread(target=simple_response_handler,
                                  args=(robot._command_tx_queue, robot._command_rx_queue, expected_command,
                                        robot_response))

    fake_robot.start()

    response_event = robot.SendCustomCommand('TestCommand', expected_responses=[mx_def.MX_ST_CMD_SUCCESSFUL])
    response_event.wait(timeout=DEFAULT_TIMEOUT) == robot_response

    assert len(robot._custom_response_events) == 0


# Returns a copy of the string with all whitespaces removed
def remove_all_whitespaces(string):
    return re.sub(r"\s+", "", string)


# Compare 2 CSV files (ignoring whitespaces)
# Returns true if equal
def robot_trajectory_files_identical(file_path_1, file_path_2):
    robot_traj_1 = robot_files.RobotTrajectories.from_file(file_path_1)
    robot_traj_2 = robot_files.RobotTrajectories.from_file(file_path_2)

    return robot_traj_1 == robot_traj_2


# Test the ability to log robot state for legacy (non rt monitoring message capable) platforms.
def test_file_logger(tmp_path, robot: mdr.Robot):
    connect_robot_helper(robot)

    # The following two functions are used to mock up data to be logged.
    def fake_data(seed, length=6):
        return [seed] * length

    def fake_string(seed, length=6):
        return ','.join([str(x) for x in fake_data(seed, length)])

    # Manually set that the robot is rt-message-capable.
    robot._robot_info.rt_message_capable = True
    # Send status message to indicate that the robot is activated and homed, and idle.
    robot._command_rx_queue.put(mdr._Message(mx_def.MX_ST_GET_STATUS_ROBOT, '1,1,0,0,0,1,1'))

    # Start logging with context manager version of logger. record_time is False to for comparison with reference file.
    with robot.FileLogger(0.001, file_path=tmp_path, record_time=False):
        robot.MoveJoints(0, -60, 60, 0, 0, 0)
        robot.MoveJoints(0, 0, 0, 0, 0, 0)
        for i in range(1, 4):
            robot._command_rx_queue.put(mdr._Message(mx_def.MX_ST_GET_JOINTS, fake_string(1)))
            robot._command_rx_queue.put(mdr._Message(mx_def.MX_ST_GET_POSE, fake_string(2)))
            robot._command_rx_queue.put(mdr._Message(mx_def.MX_ST_GET_CONF, fake_string(3, 3)))
            robot._command_rx_queue.put(mdr._Message(mx_def.MX_ST_GET_CONF_TURN, fake_string(4, 2)))

            robot._command_rx_queue.put(mdr._Message(mx_def.MX_ST_RT_TARGET_JOINT_VEL, fake_string(5, 7)))
            robot._command_rx_queue.put(mdr._Message(mx_def.MX_ST_RT_TARGET_CART_VEL, fake_string(6, 7)))
            robot._command_rx_queue.put(mdr._Message(mx_def.MX_ST_RT_TARGET_CONF, fake_string(7, 4)))
            robot._command_rx_queue.put(mdr._Message(mx_def.MX_ST_RT_TARGET_CONF_TURN, fake_string(8, 2)))

            robot._command_rx_queue.put(mdr._Message(mx_def.MX_ST_RT_JOINT_POS, fake_string(9, 7)))
            robot._command_rx_queue.put(mdr._Message(mx_def.MX_ST_RT_CART_POS, fake_string(10, 7)))
            robot._command_rx_queue.put(mdr._Message(mx_def.MX_ST_RT_JOINT_VEL, fake_string(11, 7)))
            robot._command_rx_queue.put(mdr._Message(mx_def.MX_ST_RT_JOINT_TORQ, fake_string(12, 7)))
            robot._command_rx_queue.put(mdr._Message(mx_def.MX_ST_RT_CART_VEL, fake_string(13, 7)))

            robot._command_rx_queue.put(mdr._Message(mx_def.MX_ST_RT_CONF, fake_string(14, 4)))
            robot._command_rx_queue.put(mdr._Message(mx_def.MX_ST_RT_CONF_TURN, fake_string(15, 2)))

            robot._command_rx_queue.put(mdr._Message(mx_def.MX_ST_RT_ACCELEROMETER, '16,5,' + fake_string(16000, 3)))

            robot._command_rx_queue.put(mdr._Message(mx_def.MX_ST_RT_CYCLE_END, str(i)))

        # Terminate queue and wait for thread to exit to ensure messages are processed.
        robot._command_rx_queue.put(mdr._TERMINATE)
        robot._command_response_handler_thread.join(timeout=5)
        # Restart the monitoring connection to ensure the API is in a good state.
        robot._initialize_monitoring_connection()

    # Ensure one log file is created.
    directory = os.listdir(tmp_path)
    assert len(directory) == 1

    log_file_name = directory[0]
    assert log_file_name.startswith('Meca500_R3_v9_0_0')

    log_file_path = os.path.join(tmp_path, log_file_name)
    reference_file_path = os.path.join(os.path.dirname(__file__), 'log_file_reference.zip')

    # Check that the logger output matches the reference file.
    assert robot_trajectory_files_identical(log_file_path, reference_file_path)

    robot.Disconnect()


# Test ability to log robot state for legacy (non rt monitoring message capable) platforms.
# Logging with legacy platforms use system time. To ensure consistency across tests, mock system time call to always
# return the same time (in nanoseconds).
@mock.patch('time.time_ns', mock.MagicMock(return_value=1621277770487091))
def test_file_logger_legacy(tmp_path, robot: mdr.Robot):
    connect_robot_helper(robot, supports_rt_monitoring=False)

    # The following two functions are used to mock up data to be logged.
    def fake_data(seed, length=6):
        return [seed] * length

    def fake_string(seed, length=6):
        return ','.join([str(x) for x in fake_data(seed, length)])

    # This is explicitly set for readability, and is not necessary.
    robot._robot_info.rt_message_capable = False
    # Send status message to indicate that the robot is activated and homed, and idle.
    robot._monitor_rx_queue.put(mdr._Message(mx_def.MX_ST_GET_STATUS_ROBOT, '1,1,0,0,0,1,1'))

    # Start logging with context manager version of logger. Only log the two available fields.
    with robot.FileLogger(
            0.001,
            file_path=tmp_path,
            fields=['TargetJointPos', 'TargetCartPos'],
            record_time=False,
    ):
        robot.MoveJoints(0, -60, 60, 0, 0, 0)
        robot.MoveJoints(0, 0, 0, 0, 0, 0)
        for i in range(1, 4):
            robot._monitor_rx_queue.put(mdr._Message(mx_def.MX_ST_GET_JOINTS, fake_string(i)))
            robot._monitor_rx_queue.put(mdr._Message(mx_def.MX_ST_GET_POSE, fake_string(i)))

        # Terminate queue and wait for thread to exit to ensure messages are processed.
        robot._monitor_rx_queue.put(mdr._TERMINATE)
        robot._monitor_handler_thread.join(timeout=5)
        # Restart the monitoring connection to ensure the API is in a good state.
        robot._initialize_monitoring_connection()

    # Ensure one log file is created.
    directory = os.listdir(tmp_path)
    assert len(directory) == 1

    log_file_name = directory[0]
    assert log_file_name.startswith('Meca500_R3_v8_0_0')

    log_file_path = os.path.join(tmp_path, log_file_name)
    reference_file_path = os.path.join(os.path.dirname(__file__), 'legacy_log_file_reference.zip')

    # Check that the logger output matches the reference file.
    assert robot_trajectory_files_identical(log_file_path, reference_file_path)

    robot.Disconnect()
