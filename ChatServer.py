#!/usr/bin/python
 
###################################################
### Author: Nick Wade & Andrew Goettler
### Purpose: A python chatroom server			 		
### Please provide credit where appropriate. 	
###################################################

import socket
import threading
from threading import Thread

def main(openPort):
	handshake = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	handshake.bind((socket.getsockname(),openPort))
	while True:
		data, addr = s.recvfrom(1024)
	    # insert fancy logic here
	    reply = "fancy message"
	    s.sendto(reply , addr)

###################################################
### Main Entry Point
###################################################
if __name__ == "__main__":
	initPort = 5555
    main(initPort)