#!/usr/bin/python           # This is server.py file

import thread
import socket               # Import socket module

#server initialization and activation
server = socket.socket()         # Create a socket object
myHost = "192.168.0.123" # Get local machine name
myPort = 10010                # Reserve a port for your service.
server.bind((myHost, myPort))        # Bind to the port
activeSession = True

def serverLoop(connection, addr):
	global activeSession
	print 'Got connection from', addr
	while True:
		message = raw_input(">>")
		connection.send(message)
		if message == "exit":
			break
	connection.close()                # Close the connection
	activeSession = False

def clientLoop(client, dummy):
	global activeSession
	while True:
		message = client.recv(1024)
		print message
		if message == "exit":
			break
	activeSession = False
	




theirHost = "192.168.0.166"   # Get local machine name
theirPort = 10015   # Reserve a port for your service.
client = socket.socket()         # Create a socket object
client.connect((theirHost, theirPort))
thread.start_new_thread(clientLoop, (client, "string"))

server.listen(5)                 	# Now wait for client connection.

thread.start_new_thread(serverLoop, (server.accept()))


while activeSession == True:
	pass
client.close()                     # Close the socket when done
server.close()




