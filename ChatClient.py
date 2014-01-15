#!/usr/bin/python           # This is client.py file

###################################################
### Author: Nick Wade & Andrew Goettler
### Purpose: A python chatroom client			 		
### Please provide credit where appropriate. 	
###################################################
from ChatCommon import Signals
import socket               # Import socket module
import threading
from threading import Thread

def ClientMain(openPort, host, port):
	# Create a socket and bind it to a port
	client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	client.bind((socket.gethostbyname(socket.gethostname()),openPort))

	# Request a connection from the server
	isConnected = False
	client.sendto(Signals.ReqConn, (host, port))

	# If the server responds to the request, we can proceed
	if client.recv(1024) == Signals.AckConn:
		print ("Connected to server at " + host + ":" + port)
		isConnected = True
	else:
		print("Server never responded.")
		client.shutdown(SHUT_RDWR)
		client.close
		print("Connection closed")
		isConnected = False

	# If we connected successfully, we can transmit data to the server
	while isConnected
		dataToSend = raw_input(">>")

		if dataToSend == "/exit":
			# Send request to be disconnected from the server
			client.sendto(Signals.ReqDisconn, host, port)

			# Keep checking the incoming data for acknowledgement
			while isConnected:
				if client.recv(1024) == Signals.AckDisconn:
					print("Server acknowledged shutdown request.")
					client.shutdown(SHUT_WR)
					client.close()
					print("Connection closed.")
					isConnected = False
		else:
			client.sendto(dataToSend, host, port)


# Main code below

initOpenPort = 5555
inithost = "127.0.0.1"
initport = 5556

#placeholder values used currently

ClientMain(initOpenPort, inithost, initport)
