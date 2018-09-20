#coding=utf-8
import json
# from umengnotification import UmengNotification
from umessage.umengnotification import UmengNotification

class IOSNotification(UmengNotification):

    APS_KEYS = ["alert", "badge", "sound", "content-available"]

    def setPredefinedKeyValue(self, key, value):
        if key in self.ROOT_KEYS:
            self.rootJson[key] = value
        elif key in self.APS_KEYS:
            apsJson = json.loads('{}')
            payloadJson = json.loads('{}')
            if "payload" in self.rootJson:
                payloadJson = self.rootJson["payload"]
            else:
                self.rootJson["payload"] = payloadJson
            if "aps" in payloadJson:
                apsJson = payloadJson["aps"]
            else:
                payloadJson["aps"] = apsJson
            apsJson[key] = value
        elif key in self.POLICY_KEYS:
            policyJson = json.loads('{}')
            if "policy" in self.rootJson:
                policyJson = self.rootJson["policy"]
            else:
                self.rootJson["policy"] = policyJson
            policyJson[key] = value
        else:
            if key in ["payload","aps","policy"]:
                print("You don't need to set value for %s, just set values for the sub keys in it." % key)
            else:
                print("Unknownd key: %s" % key)

    def setAlert(self, alert):
        self.setPredefinedKeyValue("alert", alert)

    def setBadge(self, badge):
        self.setPredefinedKeyValue("badge", badge)

    def setSound(self, sound):
        self.setPredefinedKeyValue("sound", sound)

    def setContentAvailable(self, contentAvailable):
        self.setPredefinedKeyValue("content-available", contentAvailable)

    def setCustomizedField(self, key, value):
        payloadJson = json.loads('{}')
        if "payload" in self.rootJson:
            payloadJson = self.rootJson["payload"]
        else:
            self.rootJson["payload"] = payloadJson
        payloadJson[key] = value