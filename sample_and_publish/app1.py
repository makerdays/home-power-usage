#!/usr/bin/python
from __future__ import print_function
import argparse
import paho.mqtt.client as mqtt
import json
import sys, os
import time
import usage_pb2
import json
import random
import sqlite3
import signal
import sys
from sqlite3 import Error
import smartMeter
from globals import MyGlobals
import subprocess, sys
import os

# Database connection
db = sqlite3.connect('/home/pi/homepowerusage/homepowerusage.db')

def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    try:
        db.close()
    except Error as e:
        print(e)
    sys.exit(0)

# Register Kill Handler
signal.signal(signal.SIGINT, signal_handler)

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, rc, x):
    print("Connected with result code " + str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    # client.subscribe(app_eui+"/devices/+/up")
    client.subscribe("dvg_json")
    client.subscribe("req_data")


def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed " + str(mid) + " " + str(granted_qos))


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("On message: " + msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    if msg.topic == 'req_data':
        body = json.loads(msg.payload)
        time = body["time"]
        queryData(db, time)


def queryData(conn, time):
    usages = []

    cur = conn.cursor()
    cur.execute("SELECT time,usage FROM usage WHERE time>=?", (time,))
    rows = cur.fetchall()
    cols = [x[0] for x in cur.description]

    for row in rows:
        usage = {}
        for prop, val in zip(cols, row):
            usage[prop] = val
        usages.append(usage)

    # Create a string representation of your array of songs.
    usageJSON = json.dumps(usages)
    # print(usageJSON)
    client.publish("resp_data", usageJSON)

if __name__ == "__main__":

    INTERVAL = 1
    print("start....")
    username = "knjzgzlj"
    password = "G5LsafT9APcU"

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_subscribe = on_subscribe
    client.username_pw_set(username, password)
    client.connect("m20.cloudmqtt.com", 11108, 60)

    #process = subprocess.Popen("./smartMeter.py",  shell=True)
    process = subprocess.Popen( "/home/pi/homepowerusage/smartMeter.py", stdout=subprocess.PIPE)

    #process = subprocess.Popen(['echo', '123'], stdout=subprocess.PIPE)
#    stdout = process.communicate()[0]
#    print ('STDOUT:{}'.format(stdout))

    start = time.time()

    publish = 1
    loop = True
    power = 0
    while loop:
        client.loop()
        publish = publish + 1

        # print("PUBLISH: " + str(publish))

	if (False):#process.poll() is None):
		print("process poll is NONE")
	else:
	    	#print("Read the out:")
	    	output = process.stdout.readline()
	    	#print(output)
	    	#print(process.poll())
            	if output == '' and process.poll() is not None:
             		power = 0
            	if output:
			#print(output)
            		power = float(output)
    	    #rc = process.poll()

	if (time.time() - start) > INTERVAL:
	    start = time.time()

	#if (publish % INTERVAL == 0):
            print("PUBLISH IT ON CHANNEL")
            usage = usage_pb2.Usage()
            usage.time = float(time.time())
	    usage.usage = power

 
            publish = 1

            # Insert into the database
            db.execute("INSERT INTO usage (time, usage) VALUES ({time}, {usage})".format(time=usage.time, usage=usage.usage))
            db.commit()

            # Protobuf!
            client.publish("dvg_buff", usage.SerializeToString())
            # JSON
            client.publish("dvg_json", '{"time":' + str(usage.time) + ', "usage":' + str(usage.usage) + '}')
        #time.sleep(0.5)


