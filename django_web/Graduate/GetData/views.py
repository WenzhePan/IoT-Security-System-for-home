from django.shortcuts import render
from .models import GetData
from django.http import HttpResponse, HttpResponseRedirect
from django.db import connection
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
import time
from .models import *
import MySQLdb
import json
import paho.mqtt.client as mqtt
import requests

def index(request):
    # context = {}
    # return render(request, "index.html", context)
    all_info = GetData.objects.all()
    return render(request, 'index.html', {'all_info': all_info})

def get_id(request):
    all_info = GetData.objects.all()
    temp = []
    humi = []
    date = []
    for info in all_info:
        temp.append(info.tmp)
        humi.append(info.humi)
        date.append(info.date)
    result = all_info
    # getdata = GetData.objects.get(id=id)
    # return  render(request, 'index.html',{'temp':temp, 'humi':humi,'date':date})
    return result

@csrf_exempt
def ajax_humi(request):
    with connection.cursor() as c:
        c.execute("select humi from sensor_data")
        humi = c.fetchall()

    return JsonResponse(humi,safe=False)

@csrf_exempt
def ajax_temp(request):
    with connection.cursor() as c:
        c.execute("select tmp from sensor_data")
        tmp = c.fetchall()

    return JsonResponse(tmp,safe=False)

@csrf_exempt
def ajax_date(request):
    with connection.cursor() as c:
        c.execute("select date from sensor_data")
        tmp = c.fetchall()
        tmp = int(tmp[0][0])
        dateArray = time.localtime(tmp)
        datetime = time.strftime("%Y-%m-%d %H:%M:%S",dateArray)
        print(datetime)
    return JsonResponse(datetime,safe=False)
 
@csrf_exempt
def ajax_depth(request):
    with connection.cursor() as c:
        c.execute("select depth from sensor_data")
        depth = c.fetchall()

    return JsonResponse(depth,safe=False)

@csrf_exempt
def ajax_echo(request):
    with connection.cursor() as c:
        c.execute("select echo from sensor_data")
        echo = c.fetchall()
    return JsonResponse(echo,safe=False)
@csrf_exempt
def ajax_smoke(request):
    with connection.cursor() as c:
        c.execute("select smoke from sensor_data")
        smoke = c.fetchall()
    return JsonResponse(smoke,safe=False)
@csrf_exempt
def ajax_fire(request):
    with connection.cursor() as c:
        c.execute("select fire from sensor_data")
        fire = c.fetchall()
        print("-------------------------")
    return JsonResponse(fire,safe=False)


url = "https://iot.diandeng.tech/api/v1/user/device/diy/auth?authKey=011ffb817439&protocol=mqtts"
response = requests.get(url)
b = response.json()
print(b)

MQTTHOST = "broker.diandeng.tech"
MQTTPORT = 1883
mqttClient = mqtt.Client(b['detail']['deviceName'])
mqttClient.username_pw_set(b['detail']['iotId'], b['detail']['iotToken'])

msg ={
    "btn-1":"tap"
}

msg2 ={
    "btn-2":"tap"
}

# 连接MQTT服务器
def on_mqtt_connect():
    mqttClient.connect(MQTTHOST, MQTTPORT, 60)
    mqttClient.loop_start()
    print("connected")
# publish 消息
def on_publish(topic, payload, qos):
    mqttClient.publish(topic, payload, qos)


# 消息处理函数
def on_message_come(lient, userdata, msg):

    print(msg.topic + " " + ":" + str(msg.payload))
    str_msg = str(msg.payload, encoding='utf-8')
    dict_msg = eval(str_msg)
    #获取数据
    print(type(dict_msg))

# subscribe 消息
def on_subscribe():
    # 订阅监听自定义Topic
    mqttClient.subscribe("/device/C4ABBDA29LQ7FAOK38Z7J3KX/s", 1)
    # mqttClient.subscribe("/device/C4ABBDA29LQ7FAOK38Z7J3KX/r", 0)
    mqttClient.on_message = on_message_come  # 消息到来处理函数

def ctrl(request):
    if request.method == "POST":
        if 'ctrl' in request.POST:
            on_mqtt_connect()
            # 自定义Topic消息上行
            on_publish("/device/C4ABBDA29LQ7FAOK38Z7J3KX/r", json.dumps(msg), 1)
            print("打开")
            return render(request, 'index.html')

def close(request):
    if request.method == "POST":
        if 'close' in request.POST:
            on_mqtt_connect()
            # 自定义Topic消息上行
            on_publish("/device/C4ABBDA29LQ7FAOK38Z7J3KX/r", json.dumps(msg2), 1)
            print("关闭")
            return render(request, 'index.html')