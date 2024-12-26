import sys
import paho.mqtt.client as mqtt
server = "iotlab101.io7lab.com" 

client = mqtt.Client()
client.connect(server, 1883, 60)

if len(sys.argv) <= 1:
    print("Usage : "+sys.argv[0]+" message")
    exit()
else:
    client.publish("lab1/yourname", str(sys.argv[1]))
