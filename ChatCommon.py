#!/usr/bin/python           # This is client.py file

###################################################
### Author: Nick Wade & Andrew Goettler
### Purpose: Common variables for 			 		
### Please provide credit where appropriate. 	
###################################################

# Use a class to represent chat signals
#
# Signal Definitions:
# "ReqConn" - Request Connection - sent to the server by the client to request a "connection"
# "AckConn" - Acknowledge Connection - sent from the server to the client when the client has been "connected"
# "ReqDisconn" - Request Disconnection - sent to the server by the client to request disconnection
# "AckDisconn" - Acknowledge Disconnection - sent from the server to the client when the client has been disconnected
#
# Two-letter signal codes may be modified later
#
class Signals:
	ReqConn = "CC"
	AckConn = "UC"
	ReqDisconn = "CE"
	AckDisconn = "UD"
