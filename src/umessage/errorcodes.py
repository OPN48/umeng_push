#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Last modified: Wang Tai (i@wangtai.me)

__revision__ = '0.1'

__all__ = [
    'HTTPStatusCode',
    'APIServerErrorCode',
    'UMPushError',
    'UMHTTPError'
]

class UMPushError(Exception):

    error_code = 0
    error_msg = ''

    def __init__(self, error_code, params):
        error_msg = '{} ==== {}'.format(API_SERVER_ERROR_CODE_MESSAGE[error_code], params)
        super(UMPushError, self).__init__(error_msg)

        self.error_code = error_code.value
        self.error_msg = API_SERVER_ERROR_CODE_MESSAGE[error_code]


class UMHTTPError(Exception):
    def __init__(self, http_code):
        super(UMHTTPError, self).__init__("HTTP Code {}".format(http_code))


class HTTPStatusCode(object):
    OK = 200
    CREATED = 201
    ACCEPTED = 202
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    INTERNAL_SERVER_ERROR = 500


class APIServerErrorCode(object):
    NO_APP_KEY = 1000
    NO_PAY_LOAD = 1001
    NO_PAY_LOAD_BODY = 1002
    NO_CUSTOM = 1003
    NO_DISPLAY_TYPE = 1004
    WRONG_IMG_URL = 1005
    WRONG_SOUND_URL = 1006
    WRONG_URL = 1007
    NO_TICKER_IN_BODY = 1008
    NO_TITLE_IN_BODY = 1009
    NO_TEXT_IN_BODY = 1010
    WRONG_PLAY_VIBRATE = 1011
    WRONG_PLAY_LIGHTS = 1012
    WRONG_PLAY_SOUND = 1013
    NO_TASK_ID = 1014
    NO_DEVICE_TOKENS = 1015
    NO_TYPE = 1016
    WRONG_PRODUCTION_MODE = 1017
    WRONG_APP_KEY_NO_PUSH = 1018
    WRONG_DISPLAY_TYPE = 1019
    NO_APPLICATION_ADDED = 1020

    DISABLED_APPLICATION = 2000
    WRONG_EXPIRATION_TIME = 2001
    WRONG_REGULAR_TIME = 2002
    WRONG_EXPIRATION_TIME_FOR_REGULAR_TIME = 2003
    NO_WHITE_LIST = 2004
    NO_MESSAGE_EXIST = 2005
    WRONG_VALIDATION_TOKEN = 2006
    WRONG_KEY_OR_MASTER_SECRET = 2007
    WRONG_JSON = 2008
    FILL_IN_ALIAS_OR_FILE_ID = 2009
    NULL_DEVICE_TOKEN = 2010
    ALIAS_GREATER_THAN_FIFTY = 2011
    APP_KEY_GREATER_THAN_THREE = 2012
    MESSAGE_IN_LINE = 2013
    MESSAGE_CANCEL_FAILED = 2014
    DEVICE_TOKENS_GREATER_THAN_FIFTY = 2015
    FILL_IN_FILTER = 2016
    ADDED_TAG_FAILED = 2017
    FILL_IN_FILE_ID = 2018
    NO_FILE_EXIST = 2019
    SERVICE_UPGRADE = 2020
    NO_APP_KEY_EXIST = 2021
    PAY_LOAD_TOO_LONG = 2022
    FILE_UPLOAD_FAILED = 2023
    SPEED_LIMIT_NO_POSITIVE_INTEGER = 2024
    NULL_APS = 2025
    SEND_MORE_THAN_TEN_PER_MINUTE = 2026
    WRONG_SIGNATURE = 2027
    TIMESTAMP_EXPIRED = 2028
    NULL_CONTENT = 2029
    WRONG_LAUNCH_FROM_DATE = 2030
    WRONG_FILTER_FORMAT = 2031
    NULL_RPODUCTION_IOSCERT = 2032
    NULL_DEVELOPMENT_IOSCERT = 2033
    CERTIFICATE_EXPIRED = 2034
    CERTIFICATE_EXPIRED_TIMER = 2035
    WRONG_TIMESPAN_FORMAT = 2036
    WRONG_UPLOAD_FILE = 2038
    WRONG_TIME_FORMAT = 2039
    EXPIRED_TIME_TOLONG = 2040

    DATABASE_ERROR_ONE = 3000
    DATABASE_ERROR_TWO = 3001
    DATABASE_ERROR_THREE = 3002
    DATABASE_ERROR_FOUR = 3003
    DATABASE_ERROR_FIVE = 3004

    SYSTEM_ERROR = 4000
    SYSTEM_BUSY = 4001
    OPERATION_FAILED = 4002
    WRONG_APP_KEY_FORMAT = 4003
    WRONG_MESSAGE_TYPE_FORMAT = 4004
    WRONG_MSG_FORMAT = 4005
    WRONG_BODY_FORMAT = 4006
    WRONG_DELIVER_POLICY_FORMAT = 4007
    WRONG_INVALID_TIME_FORMAT = 4008
    FULL_QUEUE = 4009
    WRONG_DEVICE_NUMBER_FORMAT = 4010
    INVALID_MESSAGE_EXPANDED_FIELD = 4011
    NO_ACCESS_AUTHORITY = 4012
    ASYNCHRONOUS_SEND_MESSAGE_FAILED = 4013
    WRONG_APP_KEY_TO_DEVICE_TOKENS = 4014
    NO_APPLICATION_INFO = 4015
    WRONG_FILE_CODE = 4016
    WRONG_FILE_TYPE = 4017
    WRONG_FILE_REMOTE_ADDRESS = 4018
    WRONG_FILE_DESCRIPTION = 4019
    WRONG_DEVICE_TOKEN = 4020
    HSF_TIME_OUT = 4021
    APP_KEY_REGISTER = 4022
    SERVER_NET_ERROR = 4023
    ILLEGAL_ACCESS = 4024
    DEVICE_TOKEN_ALL_FAILED = 4025
    DEVICE_TOKEN_PART_FAILED = 4026
    PULL_FILE_FAILED = 4027

    DEVICE_TOKEN_ERROR = 5000
    NO_CERTIFICATE = 5001
    UMENG_RESERVED_FIELD = 5002
    NULL_ALERT = 5003
    WRONG_ALERT = 5004
    WRONG_DEVICE_TOKEN_FORMAT = 5005
    CREATE_SOCKET_ERROR = 5006
    WRONG_CERTIFICATE_REVOKED = 5007
    WRONG_CERTIFICATE_UNKOWN = 5008
    WRONG_HANDSHAKE_FAILURE = 5009

    @classmethod
    def errorMessage(self, errorCode):
        if errorCode in API_SERVER_ERROR_CODE_MESSAGE:
            return API_SERVER_ERROR_CODE_MESSAGE[errorCode]
        else:
            return  "error code not defined"


API_SERVER_ERROR_CODE_MESSAGE = {
    # NO.1000~1020
    APIServerErrorCode.NO_APP_KEY: '请求参数没有appkey',
    APIServerErrorCode.NO_PAY_LOAD: '请求参数没有payload',
    APIServerErrorCode.NO_PAY_LOAD_BODY: '请求参数payload中没有body',
    APIServerErrorCode.NO_CUSTOM: 'display_type为message时，请求参数没有custom',
    APIServerErrorCode.NO_DISPLAY_TYPE: '请求参数没有display_type',
    APIServerErrorCode.WRONG_IMG_URL: 'img url格式不对，请以https或者http开始',
    APIServerErrorCode.WRONG_SOUND_URL: 'sound url格式不对，请以https或者http开始',
    APIServerErrorCode.WRONG_URL: 'url格式不对，请以https或者http开始',
    APIServerErrorCode.NO_TICKER_IN_BODY: 'display_type为notification时，body中ticker不能为空',
    APIServerErrorCode.NO_TITLE_IN_BODY: 'display_type为notification时，body中title不能为空',
    APIServerErrorCode.NO_TEXT_IN_BODY: 'display_type为notification时，body中text不能为空',
    APIServerErrorCode.WRONG_PLAY_VIBRATE: 'play_vibrate的值只能为true或者false',
    APIServerErrorCode.WRONG_PLAY_LIGHTS: 'play_lights的值只能为true或者false',
    APIServerErrorCode.WRONG_PLAY_SOUND: 'play_sound的值只能为true或者false',
    APIServerErrorCode.NO_TASK_ID: 'task-id没有找到',
    APIServerErrorCode.NO_DEVICE_TOKENS: '请求参数中没有device_tokens',
    APIServerErrorCode.NO_TYPE: '请求参数没有type',
    APIServerErrorCode.WRONG_PRODUCTION_MODE: 'production_mode只能为true或者false',
    APIServerErrorCode.WRONG_APP_KEY_NO_PUSH: 'appkey错误：指定的appkey尚未开通推送服务',
    APIServerErrorCode.WRONG_DISPLAY_TYPE: 'display_type填写错误',
    APIServerErrorCode.NO_APPLICATION_ADDED: '应用组中尚未添加应用',
    # NO.2000~2040
    APIServerErrorCode.DISABLED_APPLICATION: '该应用已被禁用',
    APIServerErrorCode.WRONG_EXPIRATION_TIME: '过期时间必须大于当前时间',
    APIServerErrorCode.WRONG_REGULAR_TIME: '定时发送时间必须大于当前时间',
    APIServerErrorCode.WRONG_EXPIRATION_TIME_FOR_REGULAR_TIME: '过期时间必须大于定时发送时间',
    APIServerErrorCode.NO_WHITE_LIST: 'IP白名单尚未添加, 请到网站后台添加您的服务器IP白名单',
    APIServerErrorCode.NO_MESSAGE_EXIST: '该消息不存在',
    APIServerErrorCode.WRONG_VALIDATION_TOKEN: 'validation token错误',
    APIServerErrorCode.WRONG_KEY_OR_MASTER_SECRET: 'appkey或app_master_secret错误',
    APIServerErrorCode.WRONG_JSON: 'json解析错误',
    APIServerErrorCode.FILL_IN_ALIAS_OR_FILE_ID: '请填写alias或者file_id',
    APIServerErrorCode.NULL_DEVICE_TOKEN: '与alias对应的device_tokens为空',
    APIServerErrorCode.ALIAS_GREATER_THAN_FIFTY: 'alias个数已超过50',
    APIServerErrorCode.APP_KEY_GREATER_THAN_THREE: '此appkey今天的广播数已超过3次',
    APIServerErrorCode.MESSAGE_IN_LINE: '消息还在排队，请稍候再查询',
    APIServerErrorCode.MESSAGE_CANCEL_FAILED: '消息取消失败，请稍候再试',
    APIServerErrorCode.DEVICE_TOKENS_GREATER_THAN_FIFTY: 'device_tokens个数已超过50',
    APIServerErrorCode.FILL_IN_FILTER: '请填写filter',
    APIServerErrorCode.ADDED_TAG_FAILED: '添加tag失败',
    APIServerErrorCode.FILL_IN_FILE_ID: '请填写file_id',
    APIServerErrorCode.NO_FILE_EXIST: '与此file_id对应的文件不存在',
    APIServerErrorCode.SERVICE_UPGRADE: '服务正在升级中，请稍候再试',
    APIServerErrorCode.NO_APP_KEY_EXIST: 'appkey不存在',
    APIServerErrorCode.PAY_LOAD_TOO_LONG: 'payload长度过长',
    APIServerErrorCode.FILE_UPLOAD_FAILED: '文件上传失败，请重试',
    APIServerErrorCode.SPEED_LIMIT_NO_POSITIVE_INTEGER: '限速值必须为正整数',
    APIServerErrorCode.NULL_APS: 'aps字段不能为空',
    APIServerErrorCode.SEND_MORE_THAN_TEN_PER_MINUTE: '1分钟内发送次数超出10次',
    APIServerErrorCode.WRONG_SIGNATURE: '签名不正确',
    APIServerErrorCode.TIMESTAMP_EXPIRED: '时间戳已过期',
    APIServerErrorCode.NULL_CONTENT: 'content内容不能为空',
    APIServerErrorCode.WRONG_LAUNCH_FROM_DATE: 'launch_from/not_launch_from条件中的日期须小于发送日期',
    APIServerErrorCode.WRONG_FILTER_FORMAT: 'filter格式不正确	',
    APIServerErrorCode.NULL_RPODUCTION_IOSCERT: '未上传生产证书，请到Web后台上传',
    APIServerErrorCode.NULL_DEVELOPMENT_IOSCERT: '未上传开发证书，请到Web后台上传',
    APIServerErrorCode.CERTIFICATE_EXPIRED: '证书已过期',
    APIServerErrorCode.CERTIFICATE_EXPIRED_TIMER: '定时任务证书过期',
    APIServerErrorCode.WRONG_TIMESPAN_FORMAT: '时间戳格式错误',
    APIServerErrorCode.WRONG_UPLOAD_FILE: '文件上传失败',
    APIServerErrorCode.WRONG_TIME_FORMAT: '时间格式必须是yyyy - MM - dd HH:mm:ss',
    APIServerErrorCode.EXPIRED_TIME_TOLONG: '过期时间不能超过7天',

# NO.3000~3004
    APIServerErrorCode.DATABASE_ERROR_ONE: '数据库错误',
    APIServerErrorCode.DATABASE_ERROR_TWO: '数据库错误',
    APIServerErrorCode.DATABASE_ERROR_THREE: '数据库错误',
    APIServerErrorCode.DATABASE_ERROR_FOUR: '数据库错误',
    APIServerErrorCode.DATABASE_ERROR_FIVE: '数据库错误',
    # NO.4000~4027
    APIServerErrorCode.SYSTEM_ERROR: '系统错误',
    APIServerErrorCode.SYSTEM_BUSY: '系统忙',
    APIServerErrorCode.OPERATION_FAILED: '操作失败',
    APIServerErrorCode.WRONG_APP_KEY_FORMAT: 'appkey格式错误',
    APIServerErrorCode.WRONG_MESSAGE_TYPE_FORMAT: '消息类型格式错误',
    APIServerErrorCode.WRONG_MSG_FORMAT: 'msg格式错误',
    APIServerErrorCode.WRONG_BODY_FORMAT: 'body格式错误',
    APIServerErrorCode.WRONG_DELIVER_POLICY_FORMAT: 'deliverPolicy格式错误',
    APIServerErrorCode.WRONG_INVALID_TIME_FORMAT: '失效时间格式错误',
    APIServerErrorCode.FULL_QUEUE: '单个服务器队列已满',
    APIServerErrorCode.WRONG_DEVICE_NUMBER_FORMAT: '设备号格式错误',
    APIServerErrorCode.INVALID_MESSAGE_EXPANDED_FIELD: '消息扩展字段无效',
    APIServerErrorCode.NO_ACCESS_AUTHORITY: '没有权限访问',
    APIServerErrorCode.ASYNCHRONOUS_SEND_MESSAGE_FAILED: '异步发送消息失败',
    APIServerErrorCode.WRONG_APP_KEY_TO_DEVICE_TOKENS: 'appkey和device_tokens不对应',
    APIServerErrorCode.NO_APPLICATION_INFO: '没有找到应用信息',
    APIServerErrorCode.WRONG_FILE_CODE: '文件编码有误',
    APIServerErrorCode.WRONG_FILE_TYPE: '文件类型有误',
    APIServerErrorCode.WRONG_FILE_REMOTE_ADDRESS: '文件远程地址有误',
    APIServerErrorCode.WRONG_FILE_DESCRIPTION: '文件描述信息有误',
    APIServerErrorCode.WRONG_DEVICE_TOKEN: 'device_token有误(注意，友盟的device_token是严格的44位字符串)',
    APIServerErrorCode.HSF_TIME_OUT: 'HSF异步服务超时',
    APIServerErrorCode.APP_KEY_REGISTER: 'appkey已经注册',
    APIServerErrorCode.SERVER_NET_ERROR: '服务器网络异常',
    APIServerErrorCode.ILLEGAL_ACCESS: '非法访问',
    APIServerErrorCode.DEVICE_TOKEN_ALL_FAILED: 'device-token全部失败',
    APIServerErrorCode.DEVICE_TOKEN_PART_FAILED: 'device-token部分失败',
    APIServerErrorCode.PULL_FILE_FAILED: '拉取文件失败',
    # NO.5000~5009
    APIServerErrorCode.DEVICE_TOKEN_ERROR: 'device_token错误',
    APIServerErrorCode.NO_CERTIFICATE: '证书不存在',
    APIServerErrorCode.UMENG_RESERVED_FIELD: 'p,d是umeng保留字段',
    APIServerErrorCode.NULL_ALERT: 'alert字段不能为空',
    APIServerErrorCode.WRONG_ALERT: 'alert只能是String类型',
    APIServerErrorCode.WRONG_DEVICE_TOKEN_FORMAT: 'device_token格式错误',
    APIServerErrorCode.CREATE_SOCKET_ERROR: '创建socket错误',
    APIServerErrorCode.WRONG_CERTIFICATE_REVOKED: 'certificate_revoked错误',
    APIServerErrorCode.WRONG_CERTIFICATE_UNKOWN: 'certificate_unkown错误',
    APIServerErrorCode.WRONG_HANDSHAKE_FAILURE: 'handshake_failure错误',
}

