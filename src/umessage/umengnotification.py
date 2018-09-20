#coding=utf-8
import json

class MsgType(object):
    uniCast = 'unicast'
    listCast = 'listcast'
    fileCast = 'filecast'
    broadCast = 'broadcast'
    groupCast = 'groupcast'
    customizedCast = 'customizedcast'

class UmengNotification(object):

    #status from response
    CONSTR_STATUS_SUCCESS = "SUCCESS"
    CONSTR_STATUS_FAIL = "FAIL"

    #root key constartion string
    CONSTR_APPKEY = "appkey"
    CONSTR_TIMESTAMP = "timestamp"
    CONSTR_TYPE = "type"
    CONSTR_DEVICE_TOKENS = "device_tokens"
    CONSTR_ALIAS = "alias"
    CONSTR_ALIAS_TYPE = "alias_type"
    CONSTR_FILE_ID = "file_id"
    CONSTR_FILTER = "filter"
    CONSTR_PRODUCTION_MODE = "production_mode"
    CONSTR_FEEDBACK = "feedback"
    CONSTR_DESCRIPTION = "description"
    CONSTR_THIRDPARTY_ID = "thirdparty_id"

    # policy key constartion string
    CONSTR_START_TIME = "start_time"
    CONSTR_EXPIRE_TIME = "expire_time"
    CONSTR_MAX_SEND_NUM = "max_send_num"

    #empty json
    CONSTR_EMPTY_JSON = '{}'

    #ROOT_KEYS = ["appkey", "timestamp", "type", "device_tokens", "alias", "alias_type", "file_id",
	#		"filter", "production_mode", "feedback", "description", "thirdparty_id"]
    #POLICY_KEYS = ["start_time", "expire_time", "max_send_num"]
    ROOT_KEYS = [CONSTR_APPKEY, CONSTR_TIMESTAMP, CONSTR_TYPE, CONSTR_DEVICE_TOKENS, CONSTR_ALIAS, CONSTR_ALIAS_TYPE,
                 CONSTR_FILE_ID, CONSTR_FILTER, CONSTR_PRODUCTION_MODE, CONSTR_FEEDBACK, CONSTR_DESCRIPTION, CONSTR_THIRDPARTY_ID]
    POLICY_KEYS = [CONSTR_START_TIME, CONSTR_EXPIRE_TIME, CONSTR_MAX_SEND_NUM]

    rootJson = json.loads(CONSTR_EMPTY_JSON);

    def __init__(self,
                 appKey,
                 appMasterSecret,
                 ):

        if appKey is None or appMasterSecret is None:
            raise ValueError('APP_KEY or APP_MASTER_SECRET is None')

        self.appKey = appKey
        self.appMasterSecret = appMasterSecret
        self.devices = []
        self.type = None
        self.display_type = None
        self.custom = None
        self.content = None
        self.productionMode = True
        self.notification = None
        self.msg = ""
        self.errorCode = ""
        self.statuCode = ""
        self.msgId = ""

        self.setPredefinedKeyValue( self.CONSTR_APPKEY, appKey)

    def setPredefinedKeyValue(self, key, value):
        return True

    def setAppMasterSecret(self, secret):
        self.appMasterSecret = secret

    def setAppKey(self, appkey):
        self.appKey = appkey

    def setProductionMode(self):
        self.productionMode = True
        self.setPredefinedKeyValue(self.CONSTR_PRODUCTION_MODE, "true")

    def setTestMode(self):
        self.productionMode = False
        self.setPredefinedKeyValue(self.CONSTR_PRODUCTION_MODE, "false")

    def getPostBody(self):
        return json.dumps(self.rootJson)