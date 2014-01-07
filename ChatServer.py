#!/usr/bin/python           # This is ChatServer.py file

import socket               # Import socket module
import threading
from threading import Thread

def serverSend(c, userName):
	global ActiveSession

	while ActiveSession:
		dataToSend = raw_input(userName + " ==> ")

		if dataToSend == "/exit":
			ActiveSession = False
			c.send("CC")
			break

		c.send(dataToSend)

def serverReceive(c, clientName):
	global ActiveSession

	while ActiveSession:
		dataReceived =  c.recv(1024)

		if dataReceived == "CC":
			ActiveSession = False
			break

		print clientName + " ==> " + dataReceived

def server(userName):
	global ActiveSession
	ActiveSession = True

	server = socket.socket()         # Create a socket object

	host = "192.168.0.104" #raw_input("Enter IP address: ") # socket.gethostname() # Get local machine name
	port = "12322" # raw_input("Enter port number: ")                # Reserve a port for your service.
	serverAddress = host + ":" + port

	port = int(port) # needed because raw input will result in a string for the port number; an integer is required

	server.bind((host,port)) # binds the socket to that address

	print("Waiting for client...")
	server.listen(5)

	connection, addr = server.accept() #how do I determine if connection was successful?
	if connection != -1:

		connection.send("CE")

		# get the client's name
		clientName = connection.recv(1024)

		# send the server's user name to the client
		connection.send(userName)

		print("User " + clientName + " connected.")

		sendingThread = threading.Thread(target = serverSend, args = (connection, userName))
		receivingThread = threading.Thread(target = serverReceive, args = (connection, clientName))

		sendingThread.start()
		receivingThread.start()

		sendingThread.join()
		receivingThread.join()

		# Close the socket when done
		connection.send("CC")
		connection.close()
		print("Connection closed.")
		
		server.close()
		print("Server shutting down.")

	else:
		print("Could not connect.")
		server.close()

# Main code below ***********************************************************************************	
		
userName = raw_input("Enter userName: ")
server(userName)
#server("Andrew")
