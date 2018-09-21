#coding=utf-8
from umessage.umengnotification import *
class AndroidNotification(UmengNotification):

    PAYLOAD_KEYS = ["display_type","extra"]
    BODY_KEYS = ["ticker", "title", "text", "builder_id", "icon", "largeIcon", "img", "play_vibrate", "play_lights", "play_sound",
			"sound", "after_open", "url", "activity", "custom"]
    EXTRA_KEYS=['key','value']

    class DisplayType:
        message = 'message'  # 简单消息
        NOTIFICATION = 'notification'  # 复杂通知

    class AfterOpenType:
        go_app = 'go_app'
        go_url = 'go_url'
        go_activity = 'go_activity'
        go_custom = 'go_custom'

    def setPredefinedKeyValue(self, key, value):
        if key in self.ROOT_KEYS:
            self.rootJson[key] = value
        elif key in self.PAYLOAD_KEYS:
            payloadJson = json.loads('{}')
            if "payload" in self.rootJson:
                payloadJson = self.rootJson["payload"]
            else:
                self.rootJson["payload"] = payloadJson
            payloadJson[key] = value
        elif key in self.BODY_KEYS:
            bodyJson = json.loads('{}')
            payloadJson = json.loads('{}')
            if "payload" in self.rootJson:
                payloadJson = self.rootJson["payload"]
            else:
                self.rootJson["payload"] = payloadJson
            if "body" in payloadJson:
                bodyJson = payloadJson["body"]
            else:
                payloadJson["body"] = bodyJson
            bodyJson[key] = value
        elif key in self.POLICY_KEYS:
            policyJson = json.loads('{}')
            if "policy" in self.rootJson:
                policyJson = self.rootJson["policy"]
            else:
                self.rootJson["policy"] = policyJson
            policyJson[key] = value
        else:
            if key in ["payload","aps","policy"]:
                print ("You don't need to set value for %s, just set values for the sub keys in it." % key)
            else:
                print ("Unknownd key: %s" % key)
        return True
    def serExtra(self,dic={}):
        self.setPredefinedKeyValue("extra", dic)

    def setDisplayType(self, displayType):
        self.setPredefinedKeyValue("display_type", displayType)

    def setTicker(self, ticker):
        self.setPredefinedKeyValue("ticker", ticker)

    def setTitle(self, title):
        self.setPredefinedKeyValue("title", title)

    def setText(self, text):
        self.setPredefinedKeyValue("text", text)

    def setBuilderId(self, builderId):
        self.setPredefinedKeyValue("builder_id", builderId)

    def setIcon(self, icon):
        self.setPredefinedKeyValue("icon", icon)

    def setLargeIcon(self, largeIcon):
        self.setPredefinedKeyValue("largeIcon", largeIcon)

    def setImg(self, img):
        self.setPredefinedKeyValue("img", img)

    def setIcon(self, playVibrate):
        self.setPredefinedKeyValue("play_vibrate", playVibrate)

    def setPlayLights(self, playLights):
        self.setPredefinedKeyValue("play_lights", playLights)

    def setPlaySound(self, playSound):
        self.setPredefinedKeyValue("play_sound", playSound)

    #点击"通知"的后续行为，默认为打开app。
    def goUrlAfterOpen(self, url):
        self.setAfterOpenAction(self.AfterOpenType.go_url)
        self.setUrl(url)

    def goAppAfterOpen(self,):
        self.setAfterOpenAction(self.AfterOpenType.go_app)

    def goCustomAfterOpen(self, custom):
        self.setAfterOpenAction(self.AfterOpenType.go_custom)
        self.setCustomField(custom)

    def goActivityAfterOpen(self, activity):
        self.setAfterOpenAction(self.AfterOpenType.go_activity)
        self.setActivity(activity);

    #点击"通知"的后续行为，默认为打开app。原始接口
    def setAfterOpenAction(self, action):
        self.setPredefinedKeyValue("after_open", action)

    def setUrl(self, url):
        self.setPredefinedKeyValue("url", url)

    def setActivity(self, activity):
        self.setPredefinedKeyValue("activity", activity)

    def setCustomField(self, custom):
        self.setPredefinedKeyValue("custom", custom)