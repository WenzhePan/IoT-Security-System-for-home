import hmac
import time
import requests
import pymysql
from base64 import urlsafe_b64encode

# 管理台获取accessKey、secretKey
accessKey = 'DGXn5LZ782seRxHYEjh6vIgNK9uPfCpJrwF0ilBT'
secretKey = '1Qt6g9RqFD47aZX83EjOwuVG5_nKUHWLJczxm0Bl'

# APP或管理台获取设备识别码
deviceName = 'C4ABBDA29LQ7'

# 存储数据的key
dataKey = 'temp'

# token过期时间
expirationTime = int(time.time()) + 60 * 60

url = "https://storage.diandeng.tech/api/v1/ts?e={0}&device={1}&keyword={2}&quickDate=1h&queryType=avg".format(
    expirationTime, deviceName, dataKey)

sign = urlsafe_b64encode(
    hmac.new(secretKey.encode("utf-8"),
             url.encode("utf-8"), digestmod='sha1').digest()
).decode("utf-8")
token = accessKey + ":" + sign
print(token)

respson = requests.get(url + "&token="+token)
print(respson.json())

class GetTmp():
    def __init__(self):
        # 管理台获取accessKey、secretKey
        self.accessKey = 'DGXn5LZ782seRxHYEjh6vIgNK9uPfCpJrwF0ilBT'
        self.secretKey = '1Qt6g9RqFD47aZX83EjOwuVG5_nKUHWLJczxm0Bl'

        # APP或管理台获取设备识别码
        self.deviceName = 'C4ABBDA29LQ7'
        # token过期时间
        self.expirationTime = int(time.time()) + 60 * 60

        def tmp(self):
            self.datakey = 'temp'
            url = "https://storage.diandeng.tech/api/v1/ts?e={0}&device={1}&keyword={2}&quickDate=1h&queryType=avg".format(
                self.expirationTime, self.deviceName, self.dataKey)
            sign = urlsafe_b64encode(
                hmac.new(secretKey.encode("utf-8"),
                         url.encode("utf-8"), digestmod='sha1').digest()
            ).decode("utf-8")
            token = accessKey + ":" + sign
            print(token)

            respson = requests.get(url + "&token=" + token)
            print(respson.json())

        def humi(self):
            self.datakey = 'humi'
            url = "https://storage.diandeng.tech/api/v1/ts?e={0}&device={1}&keyword={2}&quickDate=1h&queryType=avg".format(
                self.expirationTime, self.deviceName, self.dataKey)
            sign = urlsafe_b64encode(
                hmac.new(secretKey.encode("utf-8"),
                         url.encode("utf-8"), digestmod='sha1').digest()
            ).decode("utf-8")
            token = accessKey + ":" + sign
            print(token)

            respson = requests.get(url + "&token=" + token)
            print(respson.json())

        def echo(self):
            self.datakey = 'echo'
            url = "https://storage.diandeng.tech/api/v1/ts?e={0}&device={1}&keyword={2}&quickDate=1h&queryType=avg".format(
                self.expirationTime, self.deviceName, self.dataKey)
            sign = urlsafe_b64encode(
                hmac.new(secretKey.encode("utf-8"),
                         url.encode("utf-8"), digestmod='sha1').digest()
            ).decode("utf-8")
            token = accessKey + ":" + sign
            print(token)

            respson = requests.get(url + "&token=" + token)
            print(respson.json())

        def depth(self):
            self.datakey = 'depth'
            url = "https://storage.diandeng.tech/api/v1/ts?e={0}&device={1}&keyword={2}&quickDate=1h&queryType=avg".format(
                self.expirationTime, self.deviceName, self.dataKey)
            sign = urlsafe_b64encode(
                hmac.new(secretKey.encode("utf-8"),
                         url.encode("utf-8"), digestmod='sha1').digest()
            ).decode("utf-8")
            token = accessKey + ":" + sign
            print(token)

            respson = requests.get(url + "&token=" + token)
            print(respson.json())

        def main():
            tmp()
            humi()
            echo()