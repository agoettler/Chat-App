#!/usr/bin/python
 
###################################################
### Author: Nick Wade & Andrew Goettler
### Purpose: A python chatroom server			 		
### Please provide credit where appropriate. 	
###################################################
from ChatCommon import Signals
import socket
import threading
from threading import Thread

class ServerClass:
	clients = []
	serverPort = 0
	def __init__(self,initPort):   
		ServerClass.serverPort = initPort

	def addClient(self,clientSock):
		clients.append(clientSock)

	def rmClient(self,clientSock):
		clients.remove(clientSock)

	def numClient(self):
   		return len(ServerClass.clients)

   	def isConnected(clientSock):
   		if clientSock in ServerClass.clients:
   			return True
   		else:
   			return False

def main(serverInstance):
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((socket.gethostbyname(socket.gethostname()),serverInstance.serverPort))
	while True:
		data, addr = s.recvfrom(1024)
		if serverInstance.isConnected(addr):
			#Perform this later
			if data == Signals.ReqDisconn:
				serverInstance.rmClient(addr)
				s.sendto(Signals.AckDisconn, addr)
		elif data == Signals.ReqConn:
			serverInstance.addClient(addr)
			s.sendto(Signals.AckConn, addr)

###################################################
### Main Entry Point
###################################################
if __name__ == "__main__":
	serverInstance = ServerClass(5555)
	main(serverInstance)