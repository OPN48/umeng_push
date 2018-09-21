#coding=utf-8
import json,sys
from umessage.pushclient import PushClient
from umessage.androidpush import *
from umessage.iospush import *
from umessage.errorcodes import UMPushError, APIServerErrorCode
sysInputlist=[]

#注意andorid和ios是不同的appkey和appMasterSecret。 在不同需求下换成各自的appkey。或新增ioskey变量
appKey = 'xxxxxxx'
appMasterSecret = 'xxxxxxxxx'

try:
    for x in range(1,len(sys.argv)):
        sysInputlist.append(sys.argv[x])
except:
    print (-1,u'缺少输入信息')
if sys.argv[1]=='-h':
    print (-1,u'请输入title text extraKey extraValue deviceTokens')
else:
    listKeys=['title','text','extraKey','extraValue','deviceTokens']
    inputdict=dict(zip(listKeys,sysInputlist))
    deviceTokens = inputdict['deviceTokens']

#android
def sendAndroidUnicast():
    # 以英文都好判断使用列推还是单推
    if ',' in deviceTokens:
        unicast=AndroidListcast(appKey, appMasterSecret)
    else:
        unicast = AndroidUnicast(appKey, appMasterSecret)
    unicast.setDeviceToken(deviceTokens)
    unicast.setDisplayType(AndroidNotification.DisplayType.NOTIFICATION)
    unicast.setTicker(inputdict['title']+':'+inputdict['text'])
    unicast.setTitle(inputdict['title'])
    unicast.setText(inputdict['text'])
    # unicast.goActivityAfterOpen('指定Activity')
    unicast.goActivityAfterOpen('')
    unicast.setTestMode()
    unicast.serExtra({inputdict["extraKey"]:inputdict["extraValue"]})
    pushClient = PushClient()
    pushClient.send(unicast)

def sendAndroidBroadcast():
    broadcast = AndroidBroadcast(appKey, appMasterSecret)
    broadcast.setTicker(inputdict['title']+':'+inputdict['text']);
    broadcast.setTitle(inputdict['title']);
    broadcast.setText(inputdict['text']);
    broadcast.goAppAfterOpen();
    broadcast.setDisplayType(AndroidNotification.DisplayType.NOTIFICATION);
    broadcast.setTestMode()
    #Set customized fields
    broadcast.setExtraField("test", "helloworld");
    pushClient = PushClient()
    pushClient.send(broadcast)

#ios
def sendIOSUnicast():
    unicast = IOSUnicast(appKey, appMasterSecret)
    unicast.setDeviceToken(deviceTokens)
    unicast.setAlert("这个是一个iOS单播测试")
    unicast.setBadge(1234)
    unicast.setCustomizedField("test", "helloworld");
    unicast.setProductionMode()
    pushClient = PushClient()
    ret = pushClient.send(unicast)
    unicast.statuCode = ret.status_code;
    printResult(ret)

def sendIOSBroadcast():
    broadcast = IOSBroadcast(appKey, appMasterSecret)
    broadcast.setAlert("这个是一个iOS广播测试")
    broadcast.setBadge(1234)
    broadcast.setTestMode()
    pushClient = PushClient()
    pushClient.send(broadcast)

def sendIOSCustomizedcast():
    customizedcast = IOSCustomizedcast(appKey, appMasterSecret)
    customizedcast.setAlias("alias", "alias_type");
    customizedcast.setAlert("这个是一个iOS个性化测试")
    customizedcast.setBadge(1234)
    customizedcast.setTestMode()
    pushClient = PushClient()
    pushClient.send(customizedcast)

def sendIOSFilecast():
    #fileId = client.uploadContents(appkey, appMasterSecret, "aa" + "\n" + "bb");
    fileId = "fileid1"
    filecast = IOSFilecast(appKey, appMasterSecret)
    filecast.setFileId(fileId);
    filecast.setAlert("这个是一个iOS组播测试")
    filecast.setBadge(1234)
    filecast.setTestMode()
    pushClient = PushClient()
    pushClient.send(filecast)

def sendIOSListcast():
    listcast = IOSListcast(appKey, appMasterSecret)
    listcast.setDeviceToken("xxx,yyy,zzz")
    listcast.setAlert("这个是一个iOS列播测试")
    listcast.setBadge(1234)
    listcast.setTestMode()
    pushClient = PushClient()
    pushClient.send(listcast)

def sendIOSGroupcast():
    #condition:
    #"where":
    #{
    #  	"and":
    #		[
    #			{"tag" :"iostest"}
    #		]
    #	} /

    groupcast = IOSGroupcast(appKey, appMasterSecret)

    filterJson = json.loads('{}')
    whereJson = json.loads('{}')
    testTag = json.loads('{}')
    testTag['tag'] = "iostest"
    tagArray = [testTag]
    whereJson['and'] = tagArray
    filterJson['where'] = whereJson
    groupcast.setFilter(filterJson)
    groupcast.setAlert("IOS 组播测试")
    groupcast.setBadge(1);
    groupcast.setSound("default")
    groupcast.setTestMode()
    pushClient = PushClient()
    ret = pushClient.send(groupcast)
    printResult(ret)

def printResult(ret):
    print ("http status code: %s" % ret.status_code)

    if ret.text != "":
        ret_json = json.loads(ret.text)
        if ret_json["ret"] == IOSNotification.CONSTR_STATUS_SUCCESS:
            if 'msg_id' in ret_json['data']:
                print ("msgId: %s" % ret_json['data']['msg_id'])
            if 'task_id' in ret_json['data']:
                print ("task_id: %s" % ret_json['data']['task_id'])
        elif ret_json["ret"] == IOSNotification.CONSTR_STATUS_FAIL:
            errorcode = int(ret_json["data"]["error_code"])
            print ("error Code: %s, detail: %s" % (errorcode, APIServerErrorCode.errorMessage(errorcode)));

# if __name__ == '__main__':
    #sendIOSUnicast()
    #sendIOSBroadcast()
    # sendIOSGroupcast()

if deviceTokens=='all':
    sendAndroidBroadcast()
else:
    sendAndroidUnicast()