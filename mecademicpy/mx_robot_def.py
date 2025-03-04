MX_ROBOT_MAX_NB_ACCELEROMETERS = 1
MX_DEFAULT_ROBOT_IP = "192.168.0.100"
MX_ROBOT_TCP_PORT_CONTROL = 10000
MX_ROBOT_TCP_PORT_FEED = 10001
MX_ROBOT_UDP_PORT_TRACE = 10002
MX_ROBOT_UDP_PORT_RT_CTRL = 10003
MX_CHECKPOINT_ID_MIN = 1
MX_CHECKPOINT_ID_MAX = 8000
MX_ACCELEROMETER_UNIT_PER_G = 16000
MX_GRAVITY_MPS2 = 9.8067
MX_ACCELEROMETER_JOINT_M500 = 5
MX_EXT_TOOL_MPM500_NB_VALVES = 2
MX_EXT_TOOL_VBOX_MAX_VALVES = 6
MX_EIP_MAJOR_VERSION = 2
MX_EIP_MINOR_VERSION = 1
MX_NB_DYNAMIC_PDOS = 4
MX_ROBOT_MODEL_UNKNOWN = 0
MX_ROBOT_MODEL_M500_R1 = 1
MX_ROBOT_MODEL_M500_R2 = 2
MX_ROBOT_MODEL_M500_R3 = 3
MX_ROBOT_MODEL_M1000_R1 = 10
MX_ROBOT_MODEL_SCARA_R1 = 20
MX_EXT_TOOL_NONE = 0
MX_EXT_TOOL_MEGP25_SHORT = 1
MX_EXT_TOOL_MEGP25_LONG = 2
MX_EXT_TOOL_VBOX_2VALVES = 3
MX_EXT_TOOL_TYPE_INVALID = 0xFFFFFFFF
MX_EXT_TOOL_COMPLEMENTARY = 0
MX_EXT_TOOL_INDEPENDENT = 1
MX_EXT_TOOL_POSITION = 2
MX_EXT_TOOL_MODE_INVALID = 0xFFFFFFFF
MX_VALVE_STATE_STAY = -1
MX_VALVE_STATE_CLOSE = 0
MX_VALVE_STATE_OPEN = 1
MX_EVENT_SEVERITY_SILENT = 0
MX_EVENT_SEVERITY_WARNING = 1
MX_EVENT_SEVERITY_PAUSE_MOTION = 2
MX_EVENT_SEVERITY_CLEAR_MOTION = 3
MX_EVENT_SEVERITY_ERROR = 4
MX_EVENT_SEVERITY_INVALID = 0xFFFFFFFF
MX_TORQUE_LIMITS_DETECT_ALL = 0
MX_TORQUE_LIMITS_DETECT_SKIP_ACCEL = 1
MX_TORQUE_LIMITS_INVALID = 0xFFFFFFFF
MX_MOTION_CMD_TYPE_NO_MOVE = 0
MX_MOTION_CMD_TYPE_MOVEJOINTS = 1
MX_MOTION_CMD_TYPE_MOVEPOSE = 2
MX_MOTION_CMD_TYPE_MOVELIN = 3
MX_MOTION_CMD_TYPE_MOVELINRELTRF = 4
MX_MOTION_CMD_TYPE_MOVELINRELWRF = 5
MX_MOTION_CMD_TYPE_DELAY = 6
MX_MOTION_CMD_TYPE_SETBLENDING = 7
MX_MOTION_CMD_TYPE_SETJOINTVEL = 8
MX_MOTION_CMD_TYPE_SETJOINTACC = 9
MX_MOTION_CMD_TYPE_SETCARTANGVEL = 10
MX_MOTION_CMD_TYPE_SETCARTLINVEL = 11
MX_MOTION_CMD_TYPE_SETCARTACC = 12
MX_MOTION_CMD_TYPE_SETTRF = 13
MX_MOTION_CMD_TYPE_SETWRF = 14
MX_MOTION_CMD_TYPE_SETCONF = 15
MX_MOTION_CMD_TYPE_SETAUTOCONF = 16
MX_MOTION_CMD_TYPE_SETCHECKPOINT = 17
MX_MOTION_CMD_TYPE_GRIPPER = 18
MX_MOTION_CMD_TYPE_GRIPPERVEL = 19
MX_MOTION_CMD_TYPE_GRIPPERFORCE = 20
MX_MOTION_CMD_TYPE_MOVEJOINTSVEL = 21
MX_MOTION_CMD_TYPE_MOVELINVELWRF = 22
MX_MOTION_CMD_TYPE_MOVELINVELTRF = 23
MX_MOTION_CMD_TYPE_VELCTRLTIMEOUT = 24
MX_MOTION_CMD_TYPE_SETCONFTURN = 25
MX_MOTION_CMD_TYPE_SETAUTOCONFTURN = 26
MX_MOTION_CMD_TYPE_SETTORQUELIMITS = 27
MX_MOTION_CMD_TYPE_SETTORQUELIMITSCFG = 28
MX_MOTION_CMD_TYPE_MOVEJOINTSREL = 29
MX_MOTION_CMD_TYPE_SETVALVESTATE = 30
MX_MOTION_CMD_TYPE_START_OFFLINE_PROGRAM = 100
MX_MOTION_CMD_TYPE_SETDBG = 1000
MX_EIP_DYNAMIC_AUTO = 0
MX_EIP_DYNAMIC_CFG_FW_VERSION = 1
MX_EIP_DYNAMIC_CFG_PRODUCT_TYPE = 2
MX_EIP_DYNAMIC_CFG_ROBOT_SERIAL = 3
MX_EIP_DYNAMIC_CFG_JOINT_OFFSET = 4
MX_EIP_DYNAMIC_CFG_ROBOT_DH_MODEL_1 = 5
MX_EIP_DYNAMIC_CFG_ROBOT_DH_MODEL_2 = 6
MX_EIP_DYNAMIC_CFG_ROBOT_DH_MODEL_3 = 7
MX_EIP_DYNAMIC_CFG_ROBOT_DH_MODEL_4 = 8
MX_EIP_DYNAMIC_CFG_ROBOT_DH_MODEL_5 = 9
MX_EIP_DYNAMIC_CFG_ROBOT_DH_MODEL_6 = 10
MX_EIP_DYNAMIC_CFG_JOINT_LIMITS_CFG = 11
MX_EIP_DYNAMIC_CFG_MODEL_JOINT_LIMITS_1_2_3 = 12
MX_EIP_DYNAMIC_CFG_MODEL_JOINT_LIMITS_4_5_6 = 13
MX_EIP_DYNAMIC_CFG_JOINT_LIMITS_1_2_3 = 14
MX_EIP_DYNAMIC_CFG_JOINT_LIMITS_4_5_6 = 15
MX_EIP_DYNAMIC_MQ_CONF = 20
MX_EIP_DYNAMIC_MQ_PARAMS = 21
MX_EIP_DYNAMIC_MQ_VEL_ACCEL = 22
MX_EIP_DYNAMIC_MQ_GRIPPER_CFG = 23
MX_EIP_DYNAMIC_MQ_TORQUE_LIMITS_CFG = 24
MX_EIP_DYNAMIC_MQ_TORQUE_LIMITS = 25
MX_EIP_DYNAMIC_RT_TARGET_JOINT_POS = 30
MX_EIP_DYNAMIC_RT_TARGET_CART_POS = 31
MX_EIP_DYNAMIC_RT_TARGET_JOINT_VEL = 32
MX_EIP_DYNAMIC_RT_TARGET_JOINT_TORQ = 33
MX_EIP_DYNAMIC_RT_TARGET_CART_VEL = 34
MX_EIP_DYNAMIC_RT_TARGET_CONF = 35
MX_EIP_DYNAMIC_RT_JOINT_POS = 40
MX_EIP_DYNAMIC_RT_CART_POS = 41
MX_EIP_DYNAMIC_RT_JOINT_VEL = 42
MX_EIP_DYNAMIC_RT_JOINT_TORQ = 43
MX_EIP_DYNAMIC_RT_CART_VEL = 44
MX_EIP_DYNAMIC_RT_CONF = 45
MX_EIP_DYNAMIC_RT_ACCELEROMETER_5 = 46
MX_EIP_DYNAMIC_RT_WRF = 50
MX_EIP_DYNAMIC_RT_TRF = 51
MX_EIP_DYNAMIC_RT_EXTTOOL_STATUS = 52
MX_EIP_DYNAMIC_RT_GRIPPER_VALVE_STATE = 53
MX_EIP_DYNAMIC_FORCE_32_BITS = 0xFFFFFFFF
MX_ST_BUFFER_FULL = 1000
MX_ST_UNKNOWN_CMD = 1001
MX_ST_SYNTAX_ERR = 1002
MX_ST_ARG_ERR = 1003
MX_ST_NOT_ACTIVATED = 1005
MX_ST_NOT_HOMED = 1006
MX_ST_JOINT_OVER_LIMIT = 1007
MX_ST_VEL_OVER_LIMIT = 1008
MX_ST_ACCEL_OVER_LIMIT = 1009
MX_ST_BLOCKED_BY_180_DEG_PROT = 1010
MX_ST_ALREADY_ERR = 1011
MX_ST_SINGULARITY_ERR = 1012
MX_ST_ACTIVATION_ERR = 1013
MX_ST_HOMING_ERR = 1014
MX_ST_MASTER_ERR = 1015
MX_ST_OUT_OF_REACH = 1016
MX_ST_COMM_ERR = 1017
MX_ST_EOS_MISSING = 1018
MX_ST_ROBOT_NOT_LEVELED = 1019
MX_ST_BRAKES_ERR = 1020
MX_ST_DEACTIVATION_ERR = 1021
MX_ST_OFFLINE_SAVE_ERR = 1022
MX_ST_IGNORE_CMD_OFFLINE = 1023
MX_ST_MASTERING_NEEDED = 1024
MX_ST_IMPOSSIBLE_RESET_ERR = 1025
MX_ST_MUST_BE_DEACTIVATED = 1026
MX_ST_SIM_MUST_DEACTIVATED = 1027
MX_ST_NETWORK_ERR = 1028
MX_ST_OFFLINE_FULL = 1029
MX_ST_ALREADY_SAVING = 1030
MX_ST_ILLEGAL_WHILE_SAVING = 1031
MX_ST_GRIPPER_FORCE_OVER_LIMIT = 1035
MX_ST_GRIPPER_VEL_OVER_LIMIT = 1036
MX_ST_GRIPPER_RANGE_OVER_LIMIT = 1037
MX_ST_NO_GRIPPER = 1038
MX_ST_GRIPPER_TEMP_OVER_LIMIT = 1039
MX_ST_CMD_FAILED = 1040
MX_ST_NO_VBOX = 1041
MX_ST_ACTIVATED = 2000
MX_ST_ALREADY_ACTIVATED = 2001
MX_ST_HOME_DONE = 2002
MX_ST_HOME_ALREADY = 2003
MX_ST_DEACTIVATED = 2004
MX_ST_ERROR_RESET = 2005
MX_ST_NO_ERROR_RESET = 2006
MX_ST_GET_STATUS_ROBOT = 2007
MX_ST_BRAKES_OFF = 2008
MX_ST_MASTER_DONE = 2009
MX_ST_BRAKES_ON = 2010
MX_ST_GET_WRF = 2013
MX_ST_GET_TRF = 2014
MX_ST_SET_CART_VEL = 2020
MX_ST_SET_CART_ACC = 2021
MX_ST_SET_JOINT_VEL = 2022
MX_ST_SET_JOINT_ACC = 2023
MX_ST_SET_TOOL_DEF = 2024
MX_ST_SET_WRF = 2025
MX_ST_GET_JOINTS = 2026
MX_ST_GET_POSE = 2027
MX_ST_GET_AUTO_CONF = 2028
MX_ST_GET_CONF = 2029
MX_ST_GET_PHYS_CONF = 2030
MX_ST_GET_AUTO_CONF_TURN = 2031
MX_ST_SET_CORNERING = 2032
MX_ST_CLR_CORNERING = 2033
MX_ST_AUTOCONF_ON = 2034
MX_ST_AUTOCONF_OFF = 2035
MX_ST_GET_CONF_TURN = 2036
MX_ST_ACT_POS_FEED = 2038
MX_ST_DEACT_POS_FEED = 2039
MX_ST_ACT_JOINTS_FEED = 2040
MX_ST_DEACT_JOINTS_FEED = 2041
MX_ST_PAUSE_MOTION = 2042
MX_ST_RESUME_MOTION = 2043
MX_ST_CLEAR_MOTION = 2044
MX_ST_SIM_ON = 2045
MX_ST_SIM_OFF = 2046
MX_ST_EXTTOOL_SIM = 2047
MX_ST_EXTTOOL_SIM_OFF = 2048
MX_ST_RECOVERY_MODE_ON = 2049
MX_ST_RECOVERY_MODE_OFF = 2050
MX_ST_RECOVERY_VEL_CAP = 2051
MX_ST_EOM_ON = 2052
MX_ST_EOM_OFF = 2053
MX_ST_EOB_ON = 2054
MX_ST_EOB_OFF = 2055
MX_ST_START_SAVING = 2060
MX_ST_N_CMD_SAVED = 2061
MX_ST_OFFLINE_ALREADY_SAVING = 2062
MX_ST_OFFLINE_START = 2063
MX_ST_OFFLINE_LOOP_ON = 2064
MX_ST_OFFLINE_LOOP_OFF = 2065
MX_ST_START_PROGRAM_ARDY = 2066
MX_ST_SET_CART_DELTAREF_WRF = 2067
MX_ST_SET_CART_DELTAREF_TRF = 2068
MX_ST_ACTIVATION_IN_PROGRESS = 2070
MX_ST_HOMING_IN_PROGRESS = 2071
MX_ST_MASTER_IN_PROGRESS = 2072
MX_ST_GRIP_HOME = 2075
MX_ST_GRIP_ARD_HOME = 2076
MX_ST_SET_GRIP_FORCE = 2077
MX_ST_SET_GRIP_VEL = 2078
MX_ST_GET_STATUS_GRIPPER = 2079
MX_ST_GET_CMD_PENDING_COUNT = 2080
MX_ST_GET_FW_VERSION = 2081
MX_ST_GET_FW_VERSION_FULL = 2082
MX_ST_GET_ROBOT_SERIAL = 2083
MX_ST_GET_PRODUCT_TYPE = 2084
MX_ST_CMD_SUCCESSFUL = 2085
MX_ST_GET_JOINT_LIMITS = 2090
MX_ST_SET_JOINT_LIMITS = 2092
MX_ST_SET_JOINT_LIMITS_CFG = 2093
MX_ST_GET_JOINT_LIMITS_CFG = 2094
MX_ST_GET_ROBOT_NAME = 2095
MX_ST_SET_CTRL_PORT_MONIT = 2096
MX_ST_SYNC_CMD_QUEUE = 2097
MX_ST_JOINT_TORQUE = 2100
MX_ST_JOINT_SPEED = 2101
MX_ST_JOINT_POS = 2102
MX_ST_CART_POSE = 2103
MX_ST_TEMPERATURE = 2104
MX_ST_GET_ROBOT_KIN_MODEL = 2110
MX_ST_GET_ROBOT_DH_MODEL = 2111
MX_ST_GET_JOINT_OFFSET = 2112
MX_ST_GET_MODEL_JOINT_LIMITS = 2113
MX_ST_GET_MOTION_OPTIONS = 2115
MX_ST_GET_MONITORING_INTERVAL = 2116
MX_ST_GET_REAL_TIME_MONITORING = 2117
MX_ST_GET_STATUS_EVENTS = 2118
MX_ST_GET_NETWORK_OPTIONS = 2119
MX_ST_GET_RTC = 2140
MX_ST_GET_BLENDING = 2150
MX_ST_GET_VEL_TIMEOUT = 2151
MX_ST_GET_JOINT_VEL = 2152
MX_ST_GET_JOINT_ACC = 2153
MX_ST_GET_CART_LIN_VEL = 2154
MX_ST_GET_CART_ANG_VEL = 2155
MX_ST_GET_CART_ACC = 2156
MX_ST_GET_CHECKPOINT = 2157
MX_ST_GET_GRIPPER_FORCE = 2158
MX_ST_GET_GRIPPER_VEL = 2159
MX_ST_GET_TORQUE_LIMITS_CFG = 2160
MX_ST_GET_TORQUE_LIMITS = 2161
MX_ST_RT_TARGET_JOINT_POS = 2200
MX_ST_RT_TARGET_CART_POS = 2201
MX_ST_RT_TARGET_JOINT_VEL = 2202
MX_ST_RT_TARGET_JOINT_TORQ = 2203
MX_ST_RT_TARGET_CART_VEL = 2204
MX_ST_RT_TARGET_CONF = 2208
MX_ST_RT_TARGET_CONF_TURN = 2209
MX_ST_RT_JOINT_POS = 2210
MX_ST_RT_CART_POS = 2211
MX_ST_RT_JOINT_VEL = 2212
MX_ST_RT_JOINT_TORQ = 2213
MX_ST_RT_CART_VEL = 2214
MX_ST_RT_CONF = 2218
MX_ST_RT_CONF_TURN = 2219
MX_ST_RT_ACCELEROMETER = 2220
MX_ST_RT_CHECKPOINT = 2227
MX_ST_RT_WRF = 2228
MX_ST_RT_TRF = 2229
MX_ST_RT_CYCLE_END = 2230
MX_ST_RT_EXTTOOL_STATUS = 2300
MX_ST_RT_VALVE_STATE = 2310
MX_ST_RT_GRIPPER_STATE = 2320
MX_ST_RT_GRIPPER_FORCE = 2321
MX_ST_RT_GRIPPER_POS = 2322
MX_ST_CONNECTED = 3000
MX_ST_USER_ALREADY = 3001
MX_ST_UPGRADE_IN_PROGRESS = 3002
MX_ST_CMD_TOO_LONG = 3003
MX_ST_EOM = 3004
MX_ST_ERROR_MOTION = 3005
MX_ST_SEND_JOINT_RT = 3007
MX_ST_COLLISION = 3008
MX_ST_INIT_FAILED = 3009
MX_ST_SEND_POS_RT = 3010
MX_ST_CANNOT_MOVE = 3011
MX_ST_EOB = 3012
MX_ST_END_OFFLINE = 3013
MX_ST_CANT_SAVE_OFFLINE = 3014
MX_ST_OFFLINE_TIMEOUT = 3015
MX_ST_IGNORING_CMD = 3016
MX_ST_NO_OFFLINE_SAVED = 3017
MX_ST_OFFLINE_LOOP = 3018
MX_ST_JOGGING_STOPPED = 3019
MX_ST_ERROR_GRIPPER = 3025
MX_ST_MAINTENANCE_CHECK = 3026
MX_ST_INTERNAL_ERROR = 3027
MX_ST_EXCESSIVE_TRQ = 3028
MX_ST_CHECKPOINT_REACHED = 3030
MX_ST_TEXT_API_ERROR = 3031
MX_ST_PSTOP = 3032
MX_ST_NO_VALID_CFG = 3033
MX_ST_TRACE_LVL_CHANGED = 3034
MX_ST_TCP_DUMP_STARTED = 3035
MX_ST_TCP_DUMP_DONE = 3036
MX_ST_ERROR_VBOX = 3037
MX_ST_INVALID = 0xFFFFFFFF


class RobotStatusCodeInfo:

    def __init__(self, code, name, is_error):
        """This class contains information bout a robot status codes above (ex: MX_ST_BUFFER_FULL)

        Parameters
        ----------
        code : integer
            The integer value (ex: 1001)
        name : string
            The code name (ex: "MX_ST_BUFFER_FULL"
        is_error : bool
            True if this is an error code
        """
        self.code = code
        self.name = name
        self.is_error = is_error


robot_status_code_info = {
    MX_ST_BUFFER_FULL:
    RobotStatusCodeInfo(MX_ST_BUFFER_FULL, "MX_ST_BUFFER_FULL", is_error=True),
    MX_ST_UNKNOWN_CMD:
    RobotStatusCodeInfo(MX_ST_UNKNOWN_CMD, "MX_ST_UNKNOWN_CMD", is_error=True),
    MX_ST_SYNTAX_ERR:
    RobotStatusCodeInfo(MX_ST_SYNTAX_ERR, "MX_ST_SYNTAX_ERR", is_error=True),
    MX_ST_ARG_ERR:
    RobotStatusCodeInfo(MX_ST_ARG_ERR, "MX_ST_ARG_ERR", is_error=True),
    MX_ST_NOT_ACTIVATED:
    RobotStatusCodeInfo(MX_ST_NOT_ACTIVATED, "MX_ST_NOT_ACTIVATED", is_error=True),
    MX_ST_NOT_HOMED:
    RobotStatusCodeInfo(MX_ST_NOT_HOMED, "MX_ST_NOT_HOMED", is_error=True),
    MX_ST_JOINT_OVER_LIMIT:
    RobotStatusCodeInfo(MX_ST_JOINT_OVER_LIMIT, "MX_ST_JOINT_OVER_LIMIT", is_error=True),
    MX_ST_BLOCKED_BY_180_DEG_PROT:
    RobotStatusCodeInfo(MX_ST_BLOCKED_BY_180_DEG_PROT, "MX_ST_BLOCKED_BY_180_DEG_PROT", is_error=True),
    MX_ST_ALREADY_ERR:
    RobotStatusCodeInfo(MX_ST_ALREADY_ERR, "MX_ST_ALREADY_ERR", is_error=True),
    MX_ST_SINGULARITY_ERR:
    RobotStatusCodeInfo(MX_ST_SINGULARITY_ERR, "MX_ST_SINGULARITY_ERR", is_error=True),
    MX_ST_ACTIVATION_ERR:
    RobotStatusCodeInfo(MX_ST_ACTIVATION_ERR, "MX_ST_ACTIVATION_ERR", is_error=True),
    MX_ST_HOMING_ERR:
    RobotStatusCodeInfo(MX_ST_HOMING_ERR, "MX_ST_HOMING_ERR", is_error=True),
    MX_ST_MASTER_ERR:
    RobotStatusCodeInfo(MX_ST_MASTER_ERR, "MX_ST_MASTER_ERR", is_error=True),
    MX_ST_OUT_OF_REACH:
    RobotStatusCodeInfo(MX_ST_OUT_OF_REACH, "MX_ST_OUT_OF_REACH", is_error=True),
    MX_ST_OFFLINE_SAVE_ERR:
    RobotStatusCodeInfo(MX_ST_OFFLINE_SAVE_ERR, "MX_ST_OFFLINE_SAVE_ERR", is_error=True),
    MX_ST_IGNORE_CMD_OFFLINE:
    RobotStatusCodeInfo(MX_ST_IGNORE_CMD_OFFLINE, "MX_ST_IGNORE_CMD_OFFLINE", is_error=True),
    MX_ST_MASTERING_NEEDED:
    RobotStatusCodeInfo(MX_ST_MASTERING_NEEDED, "MX_ST_MASTERING_NEEDED", is_error=True),
    MX_ST_IMPOSSIBLE_RESET_ERR:
    RobotStatusCodeInfo(MX_ST_IMPOSSIBLE_RESET_ERR, "MX_ST_IMPOSSIBLE_RESET_ERR", is_error=True),
    MX_ST_MUST_BE_DEACTIVATED:
    RobotStatusCodeInfo(MX_ST_MUST_BE_DEACTIVATED, "MX_ST_MUST_BE_DEACTIVATED", is_error=True),
    MX_ST_SIM_MUST_DEACTIVATED:
    RobotStatusCodeInfo(MX_ST_SIM_MUST_DEACTIVATED, "MX_ST_SIM_MUST_DEACTIVATED", is_error=True),
    MX_ST_OFFLINE_FULL:
    RobotStatusCodeInfo(MX_ST_OFFLINE_FULL, "MX_ST_OFFLINE_FULL", is_error=True),
    MX_ST_ALREADY_SAVING:
    RobotStatusCodeInfo(MX_ST_ALREADY_SAVING, "MX_ST_ALREADY_SAVING", is_error=True),
    MX_ST_ILLEGAL_WHILE_SAVING:
    RobotStatusCodeInfo(MX_ST_ILLEGAL_WHILE_SAVING, "MX_ST_ILLEGAL_WHILE_SAVING", is_error=True),
    MX_ST_NO_GRIPPER:
    RobotStatusCodeInfo(MX_ST_NO_GRIPPER, "MX_ST_NO_GRIPPER", is_error=True),
    MX_ST_NO_VBOX:
    RobotStatusCodeInfo(MX_ST_NO_VBOX, "MX_ST_NO_VBOX", is_error=True),
    MX_ST_CMD_FAILED:
    RobotStatusCodeInfo(MX_ST_CMD_FAILED, "MX_ST_CMD_FAILED", is_error=True),
    MX_ST_ACTIVATED:
    RobotStatusCodeInfo(MX_ST_ACTIVATED, "MX_ST_ACTIVATED", is_error=False),
    MX_ST_ALREADY_ACTIVATED:
    RobotStatusCodeInfo(MX_ST_ALREADY_ACTIVATED, "MX_ST_ALREADY_ACTIVATED", is_error=False),
    MX_ST_HOME_DONE:
    RobotStatusCodeInfo(MX_ST_HOME_DONE, "MX_ST_HOME_DONE", is_error=False),
    MX_ST_HOME_ALREADY:
    RobotStatusCodeInfo(MX_ST_HOME_ALREADY, "MX_ST_HOME_ALREADY", is_error=False),
    MX_ST_DEACTIVATED:
    RobotStatusCodeInfo(MX_ST_DEACTIVATED, "MX_ST_DEACTIVATED", is_error=False),
    MX_ST_ERROR_RESET:
    RobotStatusCodeInfo(MX_ST_ERROR_RESET, "MX_ST_ERROR_RESET", is_error=False),
    MX_ST_NO_ERROR_RESET:
    RobotStatusCodeInfo(MX_ST_NO_ERROR_RESET, "MX_ST_NO_ERROR_RESET", is_error=False),
    MX_ST_GET_STATUS_ROBOT:
    RobotStatusCodeInfo(MX_ST_GET_STATUS_ROBOT, "MX_ST_GET_STATUS_ROBOT", is_error=False),
    MX_ST_BRAKES_OFF:
    RobotStatusCodeInfo(MX_ST_BRAKES_OFF, "MX_ST_BRAKES_OFF", is_error=False),
    MX_ST_MASTER_DONE:
    RobotStatusCodeInfo(MX_ST_MASTER_DONE, "MX_ST_MASTER_DONE", is_error=False),
    MX_ST_BRAKES_ON:
    RobotStatusCodeInfo(MX_ST_BRAKES_ON, "MX_ST_BRAKES_ON", is_error=False),
    MX_ST_GET_WRF:
    RobotStatusCodeInfo(MX_ST_GET_WRF, "MX_ST_GET_WRF", is_error=False),
    MX_ST_GET_TRF:
    RobotStatusCodeInfo(MX_ST_GET_TRF, "MX_ST_GET_TRF", is_error=False),
    MX_ST_GET_JOINTS:
    RobotStatusCodeInfo(MX_ST_GET_JOINTS, "MX_ST_GET_JOINTS", is_error=False),
    MX_ST_GET_POSE:
    RobotStatusCodeInfo(MX_ST_GET_POSE, "MX_ST_GET_POSE", is_error=False),
    MX_ST_GET_AUTO_CONF:
    RobotStatusCodeInfo(MX_ST_GET_AUTO_CONF, "MX_ST_GET_AUTO_CONF", is_error=False),
    MX_ST_GET_CONF:
    RobotStatusCodeInfo(MX_ST_GET_CONF, "MX_ST_GET_CONF", is_error=False),
    MX_ST_GET_AUTO_CONF_TURN:
    RobotStatusCodeInfo(MX_ST_GET_AUTO_CONF_TURN, "MX_ST_GET_AUTO_CONF_TURN", is_error=False),
    MX_ST_GET_CONF_TURN:
    RobotStatusCodeInfo(MX_ST_GET_CONF_TURN, "MX_ST_GET_CONF_TURN", is_error=False),
    MX_ST_PAUSE_MOTION:
    RobotStatusCodeInfo(MX_ST_PAUSE_MOTION, "MX_ST_PAUSE_MOTION", is_error=False),
    MX_ST_RESUME_MOTION:
    RobotStatusCodeInfo(MX_ST_RESUME_MOTION, "MX_ST_RESUME_MOTION", is_error=False),
    MX_ST_CLEAR_MOTION:
    RobotStatusCodeInfo(MX_ST_CLEAR_MOTION, "MX_ST_CLEAR_MOTION", is_error=False),
    MX_ST_SIM_ON:
    RobotStatusCodeInfo(MX_ST_SIM_ON, "MX_ST_SIM_ON", is_error=False),
    MX_ST_SIM_OFF:
    RobotStatusCodeInfo(MX_ST_SIM_OFF, "MX_ST_SIM_OFF", is_error=False),
    MX_ST_EXTTOOL_SIM:
    RobotStatusCodeInfo(MX_ST_EXTTOOL_SIM, "MX_ST_EXTTOOL_SIM", is_error=False),
    MX_ST_EOM_ON:
    RobotStatusCodeInfo(MX_ST_EOM_ON, "MX_ST_EOM_ON", is_error=False),
    MX_ST_EOM_OFF:
    RobotStatusCodeInfo(MX_ST_EOM_OFF, "MX_ST_EOM_OFF", is_error=False),
    MX_ST_EOB_ON:
    RobotStatusCodeInfo(MX_ST_EOB_ON, "MX_ST_EOB_ON", is_error=False),
    MX_ST_EOB_OFF:
    RobotStatusCodeInfo(MX_ST_EOB_OFF, "MX_ST_EOB_OFF", is_error=False),
    MX_ST_START_SAVING:
    RobotStatusCodeInfo(MX_ST_START_SAVING, "MX_ST_START_SAVING", is_error=False),
    MX_ST_N_CMD_SAVED:
    RobotStatusCodeInfo(MX_ST_N_CMD_SAVED, "MX_ST_N_CMD_SAVED", is_error=False),
    MX_ST_OFFLINE_START:
    RobotStatusCodeInfo(MX_ST_OFFLINE_START, "MX_ST_OFFLINE_START", is_error=False),
    MX_ST_OFFLINE_LOOP_ON:
    RobotStatusCodeInfo(MX_ST_OFFLINE_LOOP_ON, "MX_ST_OFFLINE_LOOP_ON", is_error=False),
    MX_ST_OFFLINE_LOOP_OFF:
    RobotStatusCodeInfo(MX_ST_OFFLINE_LOOP_OFF, "MX_ST_OFFLINE_LOOP_OFF", is_error=False),
    MX_ST_GET_STATUS_GRIPPER:
    RobotStatusCodeInfo(MX_ST_GET_STATUS_GRIPPER, "MX_ST_GET_STATUS_GRIPPER", is_error=False),
    MX_ST_GET_CMD_PENDING_COUNT:
    RobotStatusCodeInfo(MX_ST_GET_CMD_PENDING_COUNT, "MX_ST_GET_CMD_PENDING_COUNT", is_error=False),
    MX_ST_GET_FW_VERSION:
    RobotStatusCodeInfo(MX_ST_GET_FW_VERSION, "MX_ST_GET_FW_VERSION", is_error=False),
    MX_ST_GET_FW_VERSION_FULL:
    RobotStatusCodeInfo(MX_ST_GET_FW_VERSION_FULL, "MX_ST_GET_FW_VERSION_FULL", is_error=False),
    MX_ST_GET_ROBOT_SERIAL:
    RobotStatusCodeInfo(MX_ST_GET_ROBOT_SERIAL, "MX_ST_GET_ROBOT_SERIAL", is_error=False),
    MX_ST_GET_PRODUCT_TYPE:
    RobotStatusCodeInfo(MX_ST_GET_PRODUCT_TYPE, "MX_ST_GET_PRODUCT_TYPE", is_error=False),
    MX_ST_CMD_SUCCESSFUL:
    RobotStatusCodeInfo(MX_ST_CMD_SUCCESSFUL, "MX_ST_CMD_SUCCESSFUL", is_error=False),
    MX_ST_SET_CTRL_PORT_MONIT:
    RobotStatusCodeInfo(MX_ST_SET_CTRL_PORT_MONIT, "MX_ST_SET_CTRL_PORT_MONIT", is_error=False),
    MX_ST_SYNC_CMD_QUEUE:
    RobotStatusCodeInfo(MX_ST_SYNC_CMD_QUEUE, "MX_ST_SYNC_CMD_QUEUE", is_error=False),
    MX_ST_GET_JOINT_LIMITS:
    RobotStatusCodeInfo(MX_ST_GET_JOINT_LIMITS, "MX_ST_GET_JOINT_LIMITS", is_error=False),
    MX_ST_SET_JOINT_LIMITS:
    RobotStatusCodeInfo(MX_ST_SET_JOINT_LIMITS, "MX_ST_SET_JOINT_LIMITS", is_error=False),
    MX_ST_SET_JOINT_LIMITS_CFG:
    RobotStatusCodeInfo(MX_ST_SET_JOINT_LIMITS_CFG, "MX_ST_SET_JOINT_LIMITS_CFG", is_error=False),
    MX_ST_GET_JOINT_LIMITS_CFG:
    RobotStatusCodeInfo(MX_ST_GET_JOINT_LIMITS_CFG, "MX_ST_GET_JOINT_LIMITS_CFG", is_error=False),
    MX_ST_GET_ROBOT_NAME:
    RobotStatusCodeInfo(MX_ST_GET_ROBOT_NAME, "MX_ST_GET_ROBOT_NAME", is_error=False),
    MX_ST_GET_ROBOT_KIN_MODEL:
    RobotStatusCodeInfo(MX_ST_GET_ROBOT_KIN_MODEL, "MX_ST_GET_ROBOT_KIN_MODEL", is_error=False),
    MX_ST_GET_ROBOT_DH_MODEL:
    RobotStatusCodeInfo(MX_ST_GET_ROBOT_DH_MODEL, "MX_ST_GET_ROBOT_DH_MODEL", is_error=False),
    MX_ST_GET_JOINT_OFFSET:
    RobotStatusCodeInfo(MX_ST_GET_JOINT_OFFSET, "MX_ST_GET_JOINT_OFFSET", is_error=False),
    MX_ST_GET_MODEL_JOINT_LIMITS:
    RobotStatusCodeInfo(MX_ST_GET_MODEL_JOINT_LIMITS, "MX_ST_GET_MODEL_JOINT_LIMITS", is_error=False),
    MX_ST_GET_MOTION_OPTIONS:
    RobotStatusCodeInfo(MX_ST_GET_MOTION_OPTIONS, "MX_ST_GET_MOTION_OPTIONS", is_error=False),
    MX_ST_GET_MONITORING_INTERVAL:
    RobotStatusCodeInfo(MX_ST_GET_MONITORING_INTERVAL, "MX_ST_GET_MONITORING_INTERVAL", is_error=False),
    MX_ST_GET_REAL_TIME_MONITORING:
    RobotStatusCodeInfo(MX_ST_GET_REAL_TIME_MONITORING, "MX_ST_GET_REAL_TIME_MONITORING", is_error=False),
    MX_ST_GET_STATUS_EVENTS:
    RobotStatusCodeInfo(MX_ST_GET_STATUS_EVENTS, "MX_ST_GET_STATUS_EVENTS", is_error=False),
    MX_ST_GET_NETWORK_OPTIONS:
    RobotStatusCodeInfo(MX_ST_GET_NETWORK_OPTIONS, "MX_ST_GET_NETWORK_OPTIONS", is_error=False),
    MX_ST_GET_RTC:
    RobotStatusCodeInfo(MX_ST_GET_RTC, "MX_ST_GET_RTC", is_error=False),
    MX_ST_GET_BLENDING:
    RobotStatusCodeInfo(MX_ST_GET_BLENDING, "MX_ST_GET_BLENDING", is_error=False),
    MX_ST_GET_VEL_TIMEOUT:
    RobotStatusCodeInfo(MX_ST_GET_VEL_TIMEOUT, "MX_ST_GET_VEL_TIMEOUT", is_error=False),
    MX_ST_GET_JOINT_VEL:
    RobotStatusCodeInfo(MX_ST_GET_JOINT_VEL, "MX_ST_GET_JOINT_VEL", is_error=False),
    MX_ST_GET_JOINT_ACC:
    RobotStatusCodeInfo(MX_ST_GET_JOINT_ACC, "MX_ST_GET_JOINT_ACC", is_error=False),
    MX_ST_GET_CART_LIN_VEL:
    RobotStatusCodeInfo(MX_ST_GET_CART_LIN_VEL, "MX_ST_GET_CART_LIN_VEL", is_error=False),
    MX_ST_GET_CART_ANG_VEL:
    RobotStatusCodeInfo(MX_ST_GET_CART_ANG_VEL, "MX_ST_GET_CART_ANG_VEL", is_error=False),
    MX_ST_GET_CART_ACC:
    RobotStatusCodeInfo(MX_ST_GET_CART_ACC, "MX_ST_GET_CART_ACC", is_error=False),
    MX_ST_GET_CHECKPOINT:
    RobotStatusCodeInfo(MX_ST_GET_CHECKPOINT, "MX_ST_GET_CHECKPOINT", is_error=False),
    MX_ST_GET_GRIPPER_FORCE:
    RobotStatusCodeInfo(MX_ST_GET_GRIPPER_FORCE, "MX_ST_GET_GRIPPER_FORCE", is_error=False),
    MX_ST_GET_GRIPPER_VEL:
    RobotStatusCodeInfo(MX_ST_GET_GRIPPER_VEL, "MX_ST_GET_GRIPPER_VEL", is_error=False),
    MX_ST_GET_TORQUE_LIMITS_CFG:
    RobotStatusCodeInfo(MX_ST_GET_TORQUE_LIMITS_CFG, "MX_ST_GET_TORQUE_LIMITS_CFG", is_error=False),
    MX_ST_GET_TORQUE_LIMITS:
    RobotStatusCodeInfo(MX_ST_GET_TORQUE_LIMITS, "MX_ST_GET_TORQUE_LIMITS", is_error=False),
    MX_ST_RT_TARGET_JOINT_POS:
    RobotStatusCodeInfo(MX_ST_RT_TARGET_JOINT_POS, "MX_ST_RT_TARGET_JOINT_POS", is_error=False),
    MX_ST_RT_TARGET_CART_POS:
    RobotStatusCodeInfo(MX_ST_RT_TARGET_CART_POS, "MX_ST_RT_TARGET_CART_POS", is_error=False),
    MX_ST_RT_TARGET_JOINT_VEL:
    RobotStatusCodeInfo(MX_ST_RT_TARGET_JOINT_VEL, "MX_ST_RT_TARGET_JOINT_VEL", is_error=False),
    MX_ST_RT_TARGET_JOINT_TORQ:
    RobotStatusCodeInfo(MX_ST_RT_TARGET_JOINT_TORQ, "MX_ST_RT_TARGET_JOINT_TORQ", is_error=False),
    MX_ST_RT_TARGET_CART_VEL:
    RobotStatusCodeInfo(MX_ST_RT_TARGET_CART_VEL, "MX_ST_RT_TARGET_CART_VEL", is_error=False),
    MX_ST_RT_TARGET_CONF:
    RobotStatusCodeInfo(MX_ST_RT_TARGET_CONF, "MX_ST_RT_TARGET_CONF", is_error=False),
    MX_ST_RT_TARGET_CONF_TURN:
    RobotStatusCodeInfo(MX_ST_RT_TARGET_CONF_TURN, "MX_ST_RT_TARGET_CONF_TURN", is_error=False),
    MX_ST_RT_JOINT_POS:
    RobotStatusCodeInfo(MX_ST_RT_JOINT_POS, "MX_ST_RT_JOINT_POS", is_error=False),
    MX_ST_RT_CART_POS:
    RobotStatusCodeInfo(MX_ST_RT_CART_POS, "MX_ST_RT_CART_POS", is_error=False),
    MX_ST_RT_JOINT_VEL:
    RobotStatusCodeInfo(MX_ST_RT_JOINT_VEL, "MX_ST_RT_JOINT_VEL", is_error=False),
    MX_ST_RT_JOINT_TORQ:
    RobotStatusCodeInfo(MX_ST_RT_JOINT_TORQ, "MX_ST_RT_JOINT_TORQ", is_error=False),
    MX_ST_RT_CART_VEL:
    RobotStatusCodeInfo(MX_ST_RT_CART_VEL, "MX_ST_RT_CART_VEL", is_error=False),
    MX_ST_RT_CONF:
    RobotStatusCodeInfo(MX_ST_RT_CONF, "MX_ST_RT_CONF", is_error=False),
    MX_ST_RT_CONF_TURN:
    RobotStatusCodeInfo(MX_ST_RT_CONF_TURN, "MX_ST_RT_CONF_TURN", is_error=False),
    MX_ST_RT_ACCELEROMETER:
    RobotStatusCodeInfo(MX_ST_RT_ACCELEROMETER, "MX_ST_RT_ACCELEROMETER", is_error=False),
    MX_ST_RT_GRIPPER_FORCE:
    RobotStatusCodeInfo(MX_ST_RT_GRIPPER_FORCE, "MX_ST_RT_GRIPPER_FORCE", is_error=False),
    MX_ST_RT_EXTTOOL_STATUS:
    RobotStatusCodeInfo(MX_ST_RT_EXTTOOL_STATUS, "MX_ST_RT_EXTTOOL_STATUS", is_error=False),
    MX_ST_RT_GRIPPER_STATE:
    RobotStatusCodeInfo(MX_ST_RT_GRIPPER_STATE, "MX_ST_RT_GRIPPER_STATE", is_error=False),
    MX_ST_RT_VALVE_STATE:
    RobotStatusCodeInfo(MX_ST_RT_VALVE_STATE, "MX_ST_RT_VALVE_STATE", is_error=False),
    MX_ST_RT_CHECKPOINT:
    RobotStatusCodeInfo(MX_ST_RT_CHECKPOINT, "MX_ST_RT_CHECKPOINT", is_error=False),
    MX_ST_RT_WRF:
    RobotStatusCodeInfo(MX_ST_RT_WRF, "MX_ST_RT_WRF", is_error=False),
    MX_ST_RT_TRF:
    RobotStatusCodeInfo(MX_ST_RT_TRF, "MX_ST_RT_TRF", is_error=False),
    MX_ST_RT_CYCLE_END:
    RobotStatusCodeInfo(MX_ST_RT_CYCLE_END, "MX_ST_RT_CYCLE_END", is_error=False),
    MX_ST_CONNECTED:
    RobotStatusCodeInfo(MX_ST_CONNECTED, "MX_ST_CONNECTED", is_error=False),
    MX_ST_USER_ALREADY:
    RobotStatusCodeInfo(MX_ST_USER_ALREADY, "MX_ST_USER_ALREADY", is_error=True),
    MX_ST_UPGRADE_IN_PROGRESS:
    RobotStatusCodeInfo(MX_ST_UPGRADE_IN_PROGRESS, "MX_ST_UPGRADE_IN_PROGRESS", is_error=False),
    MX_ST_CMD_TOO_LONG:
    RobotStatusCodeInfo(MX_ST_CMD_TOO_LONG, "MX_ST_CMD_TOO_LONG", is_error=True),
    MX_ST_EOM:
    RobotStatusCodeInfo(MX_ST_EOM, "MX_ST_EOM", is_error=False),
    MX_ST_ERROR_MOTION:
    RobotStatusCodeInfo(MX_ST_ERROR_MOTION, "MX_ST_ERROR_MOTION", is_error=True),
    MX_ST_INIT_FAILED:
    RobotStatusCodeInfo(MX_ST_INIT_FAILED, "MX_ST_INIT_FAILED", is_error=True),
    MX_ST_EOB:
    RobotStatusCodeInfo(MX_ST_EOB, "MX_ST_EOB", is_error=False),
    MX_ST_END_OFFLINE:
    RobotStatusCodeInfo(MX_ST_END_OFFLINE, "MX_ST_END_OFFLINE", is_error=False),
    MX_ST_CANT_SAVE_OFFLINE:
    RobotStatusCodeInfo(MX_ST_CANT_SAVE_OFFLINE, "MX_ST_CANT_SAVE_OFFLINE", is_error=True),
    MX_ST_IGNORING_CMD:
    RobotStatusCodeInfo(MX_ST_IGNORING_CMD, "MX_ST_IGNORING_CMD", is_error=True),
    MX_ST_NO_OFFLINE_SAVED:
    RobotStatusCodeInfo(MX_ST_NO_OFFLINE_SAVED, "MX_ST_NO_OFFLINE_SAVED", is_error=True),
    MX_ST_OFFLINE_LOOP:
    RobotStatusCodeInfo(MX_ST_OFFLINE_LOOP, "MX_ST_OFFLINE_LOOP", is_error=False),
    MX_ST_ERROR_GRIPPER:
    RobotStatusCodeInfo(MX_ST_ERROR_GRIPPER, "MX_ST_ERROR_GRIPPER", is_error=True),
    MX_ST_ERROR_VBOX:
    RobotStatusCodeInfo(MX_ST_ERROR_VBOX, "MX_ST_ERROR_VBOX", is_error=True),
    MX_ST_MAINTENANCE_CHECK:
    RobotStatusCodeInfo(MX_ST_MAINTENANCE_CHECK, "MX_ST_MAINTENANCE_CHECK", is_error=True),
    MX_ST_INTERNAL_ERROR:
    RobotStatusCodeInfo(MX_ST_INTERNAL_ERROR, "MX_ST_INTERNAL_ERROR", is_error=True),
    MX_ST_EXCESSIVE_TRQ:
    RobotStatusCodeInfo(MX_ST_EXCESSIVE_TRQ, "MX_ST_EXCESSIVE_TRQ", is_error=True),
    MX_ST_CHECKPOINT_REACHED:
    RobotStatusCodeInfo(MX_ST_CHECKPOINT_REACHED, "MX_ST_CHECKPOINT_REACHED", is_error=False),
    MX_ST_TEXT_API_ERROR:
    RobotStatusCodeInfo(MX_ST_TEXT_API_ERROR, "MX_ST_TEXT_API_ERROR", is_error=True),
    MX_ST_PSTOP:
    RobotStatusCodeInfo(MX_ST_PSTOP, "MX_ST_PSTOP", is_error=True),
    MX_ST_NO_VALID_CFG:
    RobotStatusCodeInfo(MX_ST_NO_VALID_CFG, "MX_ST_NO_VALID_CFG", is_error=True),
    MX_ST_TRACE_LVL_CHANGED:
    RobotStatusCodeInfo(MX_ST_TRACE_LVL_CHANGED, "MX_ST_TRACE_LVL_CHANGED", is_error=False),
    MX_ST_TCP_DUMP_STARTED:
    RobotStatusCodeInfo(MX_ST_TCP_DUMP_STARTED, "MX_ST_TCP_DUMP_STARTED", is_error=False),
    MX_ST_TCP_DUMP_DONE:
    RobotStatusCodeInfo(MX_ST_TCP_DUMP_DONE, "MX_ST_TCP_DUMP_DONE", is_error=False),
}
