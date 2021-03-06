#coding=utf-8
import sys
from umessage.pushclient import PushClient
from umessage.androidpush import *
from umessage.iospush import *
from umessage.errorcodes import APIServerErrorCode
sysInputlist=[]

#注意andorid和ios是不同的appkey和appMasterSecret。 在不同需求下换成各自的appkey。或新增ioskey变量
appKey = 'xxxxxxx'
appMasterSecret = 'xxxxxxxxxx'
# 安卓客户端需要注意这部分的activity解析，厂商通道在app关闭的时候，收到推送使用这个配置
activityAfter='com.xxx.xxx.ui.activity.UmengPushHelperActivity'
custom='xxx' #如果使用了extraKey解析，custom可以忽略

#android
def sendAndroidUnicast():
    # 以英文逗号判断使用列推还是单推
    if ',' in deviceTokens:
        unicast=AndroidListcast(appKey, appMasterSecret)
    else:
        unicast = AndroidUnicast(appKey, appMasterSecret)
    unicast.setDeviceToken(deviceTokens)
    unicast.setDisplayType(AndroidNotification.DisplayType.NOTIFICATION)
    unicast.setTicker(inputdict['title']+':'+inputdict['text'])
    unicast.setTitle(inputdict['title'])
    unicast.setText(inputdict['text'])
    # 无论如何都打开这个activity，看具体你的客户端业务如何使用
    # unicast.goActivityAfterOpen(activityAfter)
    unicast.goCustomAfterOpen(custom)

    # 正式环境
    # unicast.setProductionMode()
    # 测试环境
    unicast.setTestMode()


    unicast.serExtra({inputdict["extraKey"]:inputdict["extraValue"]})
    # 虽然叫MiActivity 其实是所有厂商的推送通道，不只是小米
    unicast.setMiPush('true')
    unicast.setMiActivity(activityAfter)

    pushClient = PushClient()
    pushClient.send(unicast)

def sendAndroidBroadcast():
    broadcast = AndroidBroadcast(appKey, appMasterSecret)
    broadcast.setTicker(inputdict['title']+':'+inputdict['text']);
    broadcast.setTitle(inputdict['title']);
    broadcast.setText(inputdict['text']);
    # broadcast.goAppAfterOpen(activityAfter);
    broadcast.goCustomAfterOpen(custom);
    broadcast.setDisplayType(AndroidNotification.DisplayType.NOTIFICATION);
    # 正式环境
    # broadcast.setProductionMode()
    broadcast.setTestMode()
    #Set customized fields
    broadcast.serExtra({inputdict["extraKey"]: inputdict["extraValue"]});

    broadcast.setMiPush('true')
    broadcast.setMiActivity(activityAfter)

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

if __name__ == '__main__':
    try:
        for x in range(1, len(sys.argv)):
            sysInputlist.append(sys.argv[x])
        if sysInputlist[0] == '-h':
            print(-1, u'请输入title text extraKey extraValue deviceTokens 多个deviceTokens使用,分隔输入all则进行全量推送')
        else:
            listKeys = ['title', 'text', 'extraKey', 'extraValue', 'deviceTokens']
            inputdict = dict(zip(listKeys, sysInputlist))
            deviceTokens = inputdict['deviceTokens']
            if deviceTokens=='all':
                sendAndroidBroadcast()
            else:
                sendAndroidUnicast()
    except:
        print(-1, u'缺少输入信息')