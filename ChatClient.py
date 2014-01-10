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

# attempting to use named tuples to simplify management of connection signals
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

def ClientMain(openPort, targetAddress, targetPort):

	# Create a socket and bind it to a port
	client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	client.bind((socket.getsockname(), openPort))

	#request a connection from the server
	
# Main code below

initOpenPort = 0
initTargetAddress = 0
initTargetPort = 0

#placeholder values used currently

ClientMain(initOpenPort, initTargetAddress, initTargetPort)