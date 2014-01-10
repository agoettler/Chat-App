#!/usr/bin/python           # This is client.py file

import socket               # Import socket module
import threading
from threading import Thread

def ClientMain(openPort, targetAddress, targetPort):

	# Create a socket and bind it to a port
	client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	client.bind((socket.getsockname(), openPort))

	dataToSend = "Hi, I'm a client!"

	client.sendto(dataToSend, targetAddress, targetPort)

	receivedData = client.recv(1024)

	print ("Data received:" + receivedData)

# Main code below

initOpenPort = 600
initTargetAddress = 
initTargetPort = 

ClientMain(initOpenPort, initTargetAddress, initTargetPort)