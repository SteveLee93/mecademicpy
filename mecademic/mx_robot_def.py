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
MX_ROBOT_MODEL_UNKNOWN = 0
MX_ROBOT_MODEL_M500_R1 = 1
MX_ROBOT_MODEL_M500_R2 = 2
MX_ROBOT_MODEL_M500_R3 = 3
MX_ROBOT_MODEL_M1000_R1 = 10
MX_ROBOT_MODEL_SCARA_R1 = 20
MX_EVENT_SEVERITY_SILENT = 0
MX_EVENT_SEVERITY_WARNING = 1
MX_EVENT_SEVERITY_PAUSE_MOTION = 2
MX_EVENT_SEVERITY_CLEAR_MOTION = 3
MX_EVENT_SEVERITY_ERROR = 4
MX_EVENT_SEVERITY_INVALID = 4294967295
MX_TORQUE_LIMITS_DETECT_ALL = 0
MX_TORQUE_LIMITS_DETECT_SKIP_ACCEL = 1
MX_TORQUE_LIMITS_INVALID = 4294967295
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
MX_MOTION_CMD_TYPE_SETCONFMULTITURN = 25
MX_MOTION_CMD_TYPE_SETAUTOCONFMULTITURN = 26
MX_MOTION_CMD_TYPE_SETTORQUELIMITS = 27
MX_MOTION_CMD_TYPE_SETTORQUELIMITSCFG = 28
MX_MOTION_CMD_TYPE_START_OFFLINE_PROGRAM = 100
MX_MOTION_CMD_TYPE_SETDBG = 1000
MX_ST_BUFFER_FULL = 1000
MX_ST_UNKNOWN_CMD = 1001
MX_ST_SYNTAX_ERR = 1002
MX_ST_ARG_ERR = 1003
MX_ST_NOT_ACTIVATED = 1005
MX_ST_NOT_HOMED = 1006
MX_ST_JOINT_OVER_LIMIT = 1007
MX_ST_VEL_OVER_LIMIT = 1008
MX_ST_ACCEL_OVER_LIMIT = 1009
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
MX_ST_GET_AUTO_CONF_MULTITURN = 2031
MX_ST_SET_CORNERING = 2032
MX_ST_CLR_CORNERING = 2033
MX_ST_AUTOCONF_ON = 2034
MX_ST_AUTOCONF_OFF = 2035
MX_ST_GET_CONF_MULTITURN = 2036
MX_ST_ACT_POS_FEED = 2038
MX_ST_DEACT_POS_FEED = 2039
MX_ST_ACT_JOINTS_FEED = 2040
MX_ST_DEACT_JOINTS_FEED = 2041
MX_ST_PAUSE_MOTION = 2042
MX_ST_RESUME_MOTION = 2043
MX_ST_CLEAR_MOTION = 2044
MX_ST_SIM_ON = 2045
MX_ST_SIM_OFF = 2046
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
MX_ST_ENABLE_JOINT_LIMITS = 2093
MX_ST_DISABLE_JOINT_LIMITS = 2094
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
MX_ST_RT_NC_JOINT_POS = 2200
MX_ST_RT_NC_CART_POS = 2201
MX_ST_RT_NC_JOINT_VEL = 2202
MX_ST_RT_NC_JOINT_TORQ = 2203
MX_ST_RT_NC_CART_VEL = 2204
MX_ST_RT_NC_CONF = 2208
MX_ST_RT_NC_CONF_MULTITURN = 2209
MX_ST_RT_DRIVE_JOINT_POS = 2210
MX_ST_RT_DRIVE_CART_POS = 2211
MX_ST_RT_DRIVE_JOINT_VEL = 2212
MX_ST_RT_DRIVE_JOINT_TORQ = 2213
MX_ST_RT_DRIVE_CART_VEL = 2214
MX_ST_RT_DRIVE_CONF = 2218
MX_ST_RT_DRIVE_CONF_MULTITURN = 2219
MX_ST_RT_ACCELEROMETER = 2220
MX_ST_RT_GRIPPER_TORQ = 2221
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
MX_ST_INVALID = 4294967295
