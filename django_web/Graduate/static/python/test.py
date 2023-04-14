import hmac
import json
import time
import requests
from base64 import urlsafe_b64encode
from jsonsearch import JsonSearch
import MySQLdb
t=time.time()

# 管理台获取accessKey、secretKey
accessKey = 'DGXn5LZ782seRxHYEjh6vIgNK9uPfCpJrwF0ilBT'
secretKey = '1Qt6g9RqFD47aZX83EjOwuVG5_nKUHWLJczxm0Bl'

# APP或管理台获取设备识别码
deviceName = 'C4ABBDA29LQ7'

# 存储数据的key
dataKey1 = 'temp'
dataKey2 = 'humi'
dataKey3 = 'echo'
dataKey4 = 'depth'
dataKey5 = 'M'
dataKey6 = 'F2'
dataKey7 = 'IR'

# token过期时间
expirationTime = int(time.time()) + 60 * 60

url1 = "https://storage.diandeng.tech/api/v1/ts?e={0}&device={1}&keyword={2}&quickDate=1h&queryType=avg".format(
    expirationTime, deviceName, dataKey1)
url3 = "https://storage.diandeng.tech/api/v1/ts?e={0}&device={1}&keyword={2}&quickDate=1h&queryType=avg".format(
    expirationTime, deviceName, dataKey5)

sign2 = urlsafe_b64encode(
    hmac.new(secretKey.encode("utf-8"),
             url1.encode("utf-8"), digestmod='sha1').digest()
).decode("utf-8")

token2 = accessKey + ":" + sign2
print(token2)


respson2 = requests.get(url3 + "&token="+token2)

b = respson2.json()
print(b)


# print(respson.json()[t]["value"])
def temp():
    url1 = "https://storage.diandeng.tech/api/v1/ts?e={0}&device={1}&keyword={2}&quickDate=1h&queryType=avg".format(
    expirationTime, deviceName, dataKey1)
    sign1 = urlsafe_b64encode(
    hmac.new(secretKey.encode("utf-8"),
             url1.encode("utf-8"), digestmod='sha1').digest()
).decode("utf-8")
    token1 = accessKey + ":" + sign1
    respson1 = requests.get(url1 + "&token=" + token1)
    a = respson1.json()
    result = a['detail']
    print(result)
    # time_local = time.localtime(result[-1]['date'])
    temp = result[-1]['value']
    # dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
    print("temp: ", temp)
    # print(dt)
    return temp

def humi():
    url2 = "https://storage.diandeng.tech/api/v1/ts?e={0}&device={1}&keyword={2}&quickDate=1h&queryType=avg".format(
        expirationTime, deviceName, dataKey2)
    sign2 = urlsafe_b64encode(
        hmac.new(secretKey.encode("utf-8"),
                 url1.encode("utf-8"), digestmod='sha1').digest()
    ).decode("utf-8")
    token2 = accessKey + ":" + sign2
    respson2 = requests.get(url2 + "&token=" + token2)
    b = respson2.json()
    result2 = b['detail']
    humi = result2[-1]['value']
    print("humi:", humi)
    return humi

def echo():
    url3 = "https://storage.diandeng.tech/api/v1/ts?e={0}&device={1}&keyword={2}&quickDate=1h&queryType=avg".format(
        expirationTime, deviceName, dataKey3)
    sign3 = urlsafe_b64encode(
        hmac.new(secretKey.encode("utf-8"),
                 url1.encode("utf-8"), digestmod='sha1').digest()
    ).decode("utf-8")
    token3 = accessKey + ":" + sign3
    respson3 = requests.get(url3 + "&token=" + token3)
    b = respson3.json()
    result3 = b['detail']
    echo = result3[-1]['value']
    print("echo:", echo)
    return echo

def depth():
    url4 = "https://storage.diandeng.tech/api/v1/ts?e={0}&device={1}&keyword={2}&quickDate=1h&queryType=avg".format(
        expirationTime, deviceName, dataKey4)
    sign4 = urlsafe_b64encode(
        hmac.new(secretKey.encode("utf-8"),
                 url1.encode("utf-8"), digestmod='sha1').digest()
    ).decode("utf-8")
    token4 = accessKey + ":" + sign4
    respson4 = requests.get(url4 + "&token=" + token4)
    b = respson4.json()
    result3 = b['detail']
    depth = result3[-1]['value']
    print("depth:", depth)
    return depth
def smoke():
    url5 = "https://storage.diandeng.tech/api/v1/ts?e={0}&device={1}&keyword={2}&quickDate=1h&queryType=avg".format(
        expirationTime, deviceName, dataKey5)
    sign5 = urlsafe_b64encode(
        hmac.new(secretKey.encode("utf-8"),
                 url1.encode("utf-8"), digestmod='sha1').digest()
    ).decode("utf-8")
    token5 = accessKey + ":" + sign5
    respson4 = requests.get(url5 + "&token=" + token5)
    b = respson4.json()
    result3 = b['detail']
    smoke = result3[-1]['value']
    print("smoke:", smoke)
    return smoke

def fire():
    url6 = "https://storage.diandeng.tech/api/v1/ts?e={0}&device={1}&keyword={2}&quickDate=1h&queryType=avg".format(
        expirationTime, deviceName, dataKey6)
    sign6 = urlsafe_b64encode(
        hmac.new(secretKey.encode("utf-8"),
                 url1.encode("utf-8"), digestmod='sha1').digest()
    ).decode("utf-8")
    token5 = accessKey + ":" + sign6
    respson4 = requests.get(url6 + "&token=" + token5)
    b = respson4.json()
    result3 = b['detail']
    fire = result3[-1]['value']
    print("fire:", fire)
    return fire

def D():
    url6 = "https://storage.diandeng.tech/api/v1/ts?e={0}&device={1}&keyword={2}&quickDate=1h&queryType=avg".format(
        expirationTime, deviceName, dataKey6)
    sign6 = urlsafe_b64encode(
        hmac.new(secretKey.encode("utf-8"),
                 url1.encode("utf-8"), digestmod='sha1').digest()
    ).decode("utf-8")
    token5 = accessKey + ":" + sign6
    respson4 = requests.get(url6 + "&token=" + token5)
    b = respson4.json()
    result4 = b['detail']
    date = result4[-1]['date']
    print("date:", date)
    return date

def data():
    t = temp()
    h = humi()
    e = echo()
    d = depth()
    s = smoke()
    f = fire()
    date = D()
    print(t)
    print("连接数据库")
    db = MySQLdb.connect("127.0.0.1", "root", "root", "django_graduate", charset='utf8')
    cursor = db.cursor()
    cursor.execute("TRUNCATE TABLE sensor_data")
    try:
        cursor.execute("insert ignore into sensor_data set tmp=('%f'),humi=('%f'),echo=('%f'),depth=('%f'),"
                       "smoke=('%d'),fire=('%d'),date=('%d')" % (
            float(t), float(h), float(e), float(d),float(s),float(f),float(date)
        ))
        db.commit()
    except KeyError:
        print("捕获到异常")
        pass
    print("输入完成，延时10秒")
    time.sleep(10)


def main():

    while True:
        data()
        # date()
if __name__ == '__main__':
    main()