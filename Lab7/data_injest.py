import sys
import requests
import paho.mqtt.client as mqtt

topic = "id/yourname/sensor/evt/#"
server = "iotlab101.io7lab.com"
token="3w3R6eWoe_ifJQPhP8Aj7fbF_RWhoHfFO71na-s7FsG5nVxIg2R74ADPXC38GjlAMZrgECWiB5XH9tPIgOveLQ=="
headers={
    "Authorization" : f"Token {token}"
}


def on_connect(client, userdata, flags, rc):
    print("Connected with RC : " + str(rc))
    client.subscribe(topic)

URL = f"http://127.0.0.1:8086/write?db=bucket01"

def on_message(client, userdata, msg):
    value = float(msg.payload.decode('utf-8'))
    key = msg.topic.split('/')[4]
    d = f"ambient,location=room3 {key}={value}"
    r = requests.post(url=URL, data=d, headers=headers)
    print(f'rc : {r} for {msg.topic:38} {value: >5.1f}')

client = mqtt.Client()
client.connect(server, 1883, 60)
client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
