import json
import time

import MySQLdb
import paho.mqtt.client as mqtt
import requests
# Client对象构造

# url = "https://iot.diandeng.tech/api/v1/user/device/diy/auth?authKey=011ffb817439&protocol=mqtts"
# response = requests.get(url)
# b = response.json()
# print(b)
#
# MQTTHOST = "broker.diandeng.tech"
# MQTTPORT = 1883
# mqttClient = mqtt.Client(b['detail']['deviceName'])
# mqttClient.username_pw_set(b['detail']['iotId'], b['detail']['iotToken'])
#
# msg ={
#     "btn-1":"tap"
# }
#
# # 连接MQTT服务器
# def on_mqtt_connect():
#     mqttClient.connect(MQTTHOST, MQTTPORT, 60)
#     mqttClient.loop_start()
#     print("connected")
# # publish 消息
# def on_publish(topic, payload, qos):
#     mqttClient.publish(topic, payload, qos)
#
#
# # 消息处理函数
# def on_message_come(lient, userdata, msg):
#
#     print(msg.topic + " " + ":" + str(msg.payload))
#     str_msg = str(msg.payload, encoding='utf-8')
#     dict_msg = eval(str_msg)
#     #获取数据
#     print(type(dict_msg))
#     # temp = dict_msg['data']['temp']['val']
#     # humi = dict_msg['data']['humi']['val']
#     # date = dict_msg['data']['temp']['date']
#     # #连接数据库
#     # print("连接数据库")
#     # db = MySQLdb.connect("127.0.0.1", "root", "root", "django_graduate", charset='utf8')
#     # cursor = db.cursor()
#     # cursor.execute("TRUNCATE TABLE sensor_data")
#     # try:
#     #     cursor.execute("insert ignore into sensor_data set tmp=('%d'),humi=('%d'),date=('%d')" % (
#     #         float(temp), float(humi), float(date)
#     #     ))
#     #     db.commit()
#     # except KeyError:
#     #     print("捕获到异常")
#     #     pass
#     # print("输入完成，延时5秒")
#     # time.sleep(10)
# # subscribe 消息
# def on_subscribe():
#     # 订阅监听自定义Topic
#     mqttClient.subscribe("/device/C4ABBDA29LQ7FAOK38Z7J3KX/s", 1)
#     # mqttClient.subscribe("/device/C4ABBDA29LQ7FAOK38Z7J3KX/r", 0)
#     mqttClient.on_message = on_message_come  # 消息到来处理函数
#
#
# def main():
#     on_mqtt_connect()
#
#     # 自定义Topic消息上行
#     on_publish("/device/C4ABBDA29LQ7FAOK38Z7J3KX/r",json.dumps(msg),1)
#     on_subscribe()
#     # mqttClient.subscribe("/device/C4ABBDA29LQ7FAOK38Z7J3KX/s", 0)
#
#
#     # while True:
#     #     pass
# if __name__ == '__main__':
#     main()