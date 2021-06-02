#!/usr/bin/env python3
import os
import sys

import mecademic.robot as mdr

robot = mdr.Robot()

# CHECK THAT IP ADDRESS IS CORRECT! #
try:
    robot.Connect(address='192.168.0.100')
except mdr.CommunicationError as e:
    print(f'Robot failed to connect. Is the IP address correct? {e}')
    raise e

try:
    # Send the commands to get the robot ready for operation.
    print('Activating and homing robot...', flush=True)
    robot.ActivateRobot()
    robot.Home()

    # Wait until robot is homed.
    robot.WaitHomed(timeout=60)  # Add a timeout of 60 seconds in case something fails.

    # Configure robot's behavior to desired speed/accel/etc
    print('Configuring robot\'s behavior...', flush=True)
    robot.SetJointVel(50)
    robot.SetJointAcc(50)
    robot.SetBlending(50)

    # Configure monitoring interval and required events to capture
    # (here we ask for target and current joint positions)
    robot.SetMonitoringInterval(0.001)
    robot.SetRealTimeMonitoring(events=["TargetJointPos", "JointPos"])

    # Move to starting position
    print('Moving to a well-known starting position...', flush=True)
    robot.MoveJoints(0, 0, 0, 0, 0, 0)

    # Wait until robot is idle (reached starting position)
    robot.WaitIdle()

    # Start running a test script while logging robot data to a csv file
    # (here we log target and current joint positions)
    print('Start running test script while logging to csv file...', flush=True)
    with robot.FileLogger(fields=["rt_target_joint_pos", "rt_joint_pos"]):
        # Perform 2 simple joint moves
        robot.MoveJoints(30, 25, 20, 15, 10, 5)
        robot.MoveJoints(-30, -25, -20, -15, -10, -5)

        # Wait until robot is idle (above commands finished executing) before stopping logging.
        robot.WaitIdle(60)
        # Exiting the "FileLogger" scope automatically stops logging

    print('Done!', flush=True)

except Exception as exception:
    # Attempt to clear error if robot is in error.
    if robot.GetRobotState().error_status:
        print(exception)
        print('Robot has encountered an error, attempting to clear...', flush=True)
        robot.ResetError()
        robot.ResumeMotion()
    else:
        raise

print('Disconnecting from robot.', flush=True)
robot.Disconnect()
