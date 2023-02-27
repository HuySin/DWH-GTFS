import paho.mqtt.client as mqtt
import time, random, json
import MESSAGE


def on_publish(client, userdata, mid):
	print('Message %s is published\n' % mid)

#MQTT Client
user = "user1"
topic = "test"
client = mqtt.Client(client_id="client1")
client.username_pw_set(user, "123")
client.on_publish = on_publish
broker = '127.0.0.1'
port = 1883
client.connect(broker,port)


while True:
	DESdata = MESSAGE.DES().jSon()

	LOGdata = MESSAGE.LOG().jSon()

	METdata = MESSAGE.MET().jSon()

	SWRdata = MESSAGE.SWR().jSon()

	DATA = random.choice([DESdata , LOGdata, METdata, SWRdata])

	print('Message content:', json.dumps(DATA))
	info = client.publish(topic,json.dumps(DATA))

	time.sleep(10)