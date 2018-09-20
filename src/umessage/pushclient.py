#coding=utf-8

import time
import hashlib
import requests

class PushClient(object):

    USER_AGENT = "Mozilla/5.0"
    HOST = "http://msg.umeng.com"
    UPLOAD_PATH = "/upload"
    POST_PATH = "/api/send"

    API_URL = HOST+POST_PATH

    def __md5(self, s):
        if isinstance(s, str):
            m = hashlib.md5(s.encode())
        else:
            m = hashlib.md5(s)
        return m.hexdigest()

    def send(self, msg):
        timestamp = int(time.time() * 1000)
        msg.setPredefinedKeyValue("timestamp", timestamp);
        postBody = msg.getPostBody()
        sign = self.__md5('{}{}{}{}'.format('POST', self.API_URL, postBody, msg.appMasterSecret))
        #print sign, postBody
        print(postBody)
        r = requests.post(self.API_URL + '?sign=' + sign, data=postBody)
        print (r.status_code, r.text)
        return r