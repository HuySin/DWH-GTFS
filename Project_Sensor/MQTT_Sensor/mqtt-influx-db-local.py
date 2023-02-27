
##Initialize the Client
from datetime import datetime
import paho.mqtt.client as mqtt
import parseMESSAGE
import push_to_QUEUE

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import json
from influxdb import InfluxDBClient

#InfluxDB Local
INFLUXDB_DATABASE = 'mqtt_sensor'
influx_client = InfluxDBClient('localhost', 8086, '', '', None)

#MQTT Client
topic = "test"
user = "user2"
client = mqtt.Client(client_id="client2")
client.username_pw_set(user, "123")
broker = '127.0.0.1'
port = 1883

#MESSAGE QUEUE
MODEL_1 = [[0]*4]
MODEL_2 = [[0]*4]
MODEL_3 = [[0]*4]
MODEL_4 = [[0]*4]
MODEL_5 = [[0]*4]


def _init_influxdb_database():
    databases = influx_client.get_list_database()
    if len(list(filter(lambda x: x['name'] == INFLUXDB_DATABASE, databases))) == 0:
        influx_client.create_database(INFLUXDB_DATABASE)
    influx_client.switch_database(INFLUXDB_DATABASE)


def connect_mqtt() -> mqtt:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client.on_connect = on_connect
    client.connect(broker,port)
    return client

def writeDB(MODEL):
    for i in range(len(MODEL)):
        if MODEL[i][0] != 0 and MODEL[i][1] != 0 and MODEL[i][2] != 0 and MODEL[i][3] != 0:

            data = parseMESSAGE.parseDES(MODEL[i][0])
            for j in range(len(data)):
                influx_client.write_points([data[j]])
                print("Wrote DES messange from MODEL {} to influxDB\n".format(data[j]['tags']['modelVersion']))

            data = parseMESSAGE.parseMET(MODEL[i][1])
            for j in range(len(data)):
                influx_client.write_points([data[j]])
                print("Wrote MET messange from MODEL {} to influxDB\n".format(data[j]['tags']['modelVersion']))

            data = parseMESSAGE.parseSWR(MODEL[i][2])
            for j in range(len(data)):
                influx_client.write_points([data[j]])
                print("Wrote SWR messange from MODEL {} to influxDB\n".format(data[j]['tags']['modelVersion']))

            data = parseMESSAGE.parseLOG(MODEL[i][3])
            for j in range(len(data)):
                influx_client.write_points([data[j]])
                print("Wrote LOG messange from MODEL {} to influxDB\n".format(data[j]['tags']['modelVersion']))

            MODEL.pop(i)

            break
            
def subscribe(client: mqtt):
    def on_message(client, userdata, msg):
        msg_decode=json.loads(str(msg.payload.decode("utf-8","ignore")))
        print(f"MQTT: Received `{msg_decode}` from `{msg.topic}` topic\n")

        push_to_QUEUE.push_to_QUEUE(MODEL_1, MODEL_2, MODEL_3, MODEL_4, MODEL_5, msg_decode)

        writeDB(MODEL_1)
        writeDB(MODEL_2)
        writeDB(MODEL_3)
        writeDB(MODEL_4)
        writeDB(MODEL_5)
        
    client.subscribe(topic)
    client.on_message = on_message


def run():
    _init_influxdb_database()
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()



