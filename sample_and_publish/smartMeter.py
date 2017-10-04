#!/usr/bin/python

import time
import math
import Adafruit_ADS1x15
import sys
import os
import serial

adc = Adafruit_ADS1x15.ADS1115()

conversion = 4096/32767.00

ser = serial.Serial(
    port='/dev/ttyS0',
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

if __name__ == "__main__":
	power = 0

	sys.stdout.write(str(power) + '\n')
	sys.stdout.flush()

	adc.start_adc(0,1,860)

	while True:
		#os.system('cls' if os.name == 'nt' else 'clear')

		#adc.start_adc(0,1,860)
		adc0 = []
		start = time.time()
	
		try:
 			while (time.time() - start) <= 1.0:
                        	adc0.append(adc.get_last_result())
		except IOError as e: # catch *all* exceptions
			#print("Start adc - exception occurred")
			adc.start_adc(0,1,860)	
			continue
		#while (time.time() - start) <= 1.0:
		#	adc0.append(adc.get_last_result())
			
		voltage = (max(adc0)*conversion)/1000

		current = ((voltage-2.5122)/0.625)*15

		currentRms  = current/math.sqrt(2)

		power = ((currentRms)*220)
		power = round(power,2)

		if power < 0:
			power = 0.00
		#print "----------"
		#print currentRms
		#print voltage 
		#print power
		#print "-------------"
		#ser.write("n0.val=1")
		#ser.write(0xFF)
		sys.stdout.write(str(power) + '\n')
        	sys.stdout.flush()
	
	
	
	

	

