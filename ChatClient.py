#!/usr/bin/python           # This is client.py file

import socket               # Import socket module
import threading
from threading import Thread



def clientSend(s, userName):
	global ActiveSession

	while ActiveSession:
		dataToSend = raw_input(userName + " ==> ")

		if dataToSend == "/exit":
			ActiveSession = False
			s.send("CC")
			break

		s.send(dataToSend)

def clientReceive(s, peerName):
	global ActiveSession

	while ActiveSession:
		dataReceived =  s.recv(1024)

		if dataReceived == "CC":
			ActiveSession = False
			break

		print peerName + " ==> " + dataReceived

def client(userName):

	global ActiveSession
	ActiveSession = True

	client = socket.socket()         # Create a socket object

	host = "192.168.0.104" #raw_input("Enter IP address: ") # socket.gethostname() # Get local machine name

	port = "12322" # raw_input("Enter port number: ")                # Reserve a port for your service.

	serverAddress = host + ":" + port

	port = int(port)

	client.connect((host, port))

	# indicate that the connection has been established
	if(client.recv(1024)) == "CE":

		# send the user name to the server
		client.send(userName)

		# get the peer's user name
		peerName = client.recv(1024)

		# indicate that the connection was successful and that the session is active
		print("Connected to " + peerName + " at " + serverAddress + " successfully.")

		sendingThread = threading.Thread(target = clientSend, args = (client, userName))
		receivingThread = threading.Thread(target = clientReceive, args = (client, peerName))

		sendingThread.start()
		receivingThread.start()

		sendingThread.join()
		receivingThread.join()

		# Close the socket when done
		client.send("CC")
		client.close
		print("Connection closed.") 

	# if connection could not be established, close the connection and send "CC" just in case
	else:
		# Close the socket when done
		client.close
		print("Could not connect")

# Main code below ***********************************************************************************	
		
# userName = raw_input("Enter userName: ")
 # client(userName)
client("Andrew")