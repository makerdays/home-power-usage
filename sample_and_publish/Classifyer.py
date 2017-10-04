#!/usr/bin/python

from __future__ import print_function
import paho.mqtt.client as mqtt
import time,json
import random

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, rc, x):
    print("Connected with result code " + str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    # client.subscribe(app_eui+"/devices/+/up")
    client.subscribe("dvg_json")

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed " + str(mid) + " " + str(granted_qos))

    

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    #print("On message: " + msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    data = json.loads(msg.payload.decode())
    
    global toTestSwitch
    if toTestSwitch:
        toTestSwitch = False
        return
    else:
        toTestSwitch = True
    
    
    usage = data["usage"]
    difference = usage - buffer[0]
    buffer[0] = buffer[1]
    buffer[1] = usage

    if difference < 0:
        switchOn="Off"
    else:
        switchOn="On"
    global change
    change["switchOn"] = switchOn
    
    size = float(abs(difference))
    
    global appliances
    for i,appliance in enumerate(appliances):
        if usage < 10:
            for appliance in appliances:
                appliance[2] = "Off"
            change = {}
            break
            
        elif size < appliance[0]:
            change["Name"] = appliance[1]
            appliance[2] = switchOn
            break

if __name__ == "__main__":
    username = "knjzgzlj"
    password = "G5LsafT9APcU"

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_subscribe = on_subscribe
    client.username_pw_set(username, password)
    client.connect("m20.cloudmqtt.com", 11108, 60)

    
    appliances = [[30,"Lights","Off"],
    [820,"Geyser","Off"],
    [2000,"Heater","Off"]]
    buffer = [0.0,0.0]
    
    toTestSwitch = True
    
    change = {}
    
    publish = 1
    loop = True
    while loop:
        client.loop()
        publish = publish + 1       

        if change != {}:
            #client.publish("appl_json",'{"'+change["Name"] + '":"'+change["switchOn"]+'"}' )
            jsonString = json.dumps(change)
            client.publish("appl_json",jsonString)
            data = {}
            data[change["Name"]] = change["switchOn"]
            jsonString2 = json.dumps(data)
            client.publish("appl2_json",jsonString2)
        time.sleep(1)
        change = {}
        print("Appliances2:",appliances)
        if publish % 60 == 0:
            publish = 0
            for appliance in appliances:
                change["switchOn"] = appliance[2]
                change["Name"] = appliance[1]
            
                jsonString = json.dumps(change)
                client.publish("appl_json",jsonString)
                data = {}
                data[change["Name"]] = change["switchOn"]
                jsonString2 = json.dumps(data)

                client.publish("appl2_json",jsonString2)
            
            change = {}
