#!/usr/bin/python           # This is client.py file

###################################################
### Author: Nick Wade & Andrew Goettler
### Purpose: A python chatroom server			 		
### Please provide credit where appropriate. 	
###################################################

import socket               # Import socket module
import threading
from threading import Thread
from collections import namedtuple

# Attempting to use named tuples to simplify management of connection signals
#
# Signal Definitions:
# "ReqConn" - Request Connection - sent to the server by the client to request a "connection"
# "AckConn" - Acknowledge Connection - sent from the server to the client when the client has been "connected"
# "ReqDisconn" - Request Disconnection - sent to the server by the client to request disconnection
# "AckDisconn" - Acknowledge Disconnection - sent from the server to the client when the client has been disconnected
#
# Two-letter signal codes may be modified later
#
Signals = namedtuple('Signals', ['ReqConn', 'AckConn', 'ReqDisconn', 'AckDisconn'] )
signals = Signals("CC", "UC", "CE", "UD")

def ClientMain(openPort, host, port):
	global signals

	# Create a socket and bind it to a port
	client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	client.bind((socket.getsockname(), openPort))

	# Request a connection from the server
	client.sendto(signals.ReqConn, host, port)

	# If the server responds to the request, we can proceed
	receivedData = client.recv(1024)
	if receivedData == signals.AckConn
		print ("Connected to server at " + host + ":" + port)

		# Probably do some other stuff in here

		# Request to be disconnected from the server
		client.sendto(signals.ReqDisconn, host, port)
		if client.recv(1024) == signals.AckDisconn
			print("Server acknowledged shutdown request.")
			client.shutdown(SHUT_WR)
			client.close()
			print("Connection closed".)
		else
			# We requested to be disconnected from the server, but it didn't respond. This may be a problem.
			print ("We requested to be disconnected from the server, but it didn't respond. This may be a problem.")
	else
		print("Server never responded.")
		client.shutdown(SHUT_RDWR)
		client.close
		print("Connection closed")

# Main code below

initOpenPort = 0
inithost = 0
initport = 0

#placeholder values used currently

ClientMain(initOpenPort, inithost, initport)
