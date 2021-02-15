from socket import *

serverName = ''
serverPort = 12000

# creates the client's socket called clientSocket. 
# The first parameter again indicates that the underlying network is using IPv4. 
# The second parameter indicates that the socket is of type SOCK_STREAM, meaning it is a TCP Socket
# Note: Here I am not specifying the port number of the client socket when creating it; I'm instead letting the
# operating system do this for me. 
clientSocket = socket(AF_INET, SOCK_STREAM)

# before the client can send data to the server or vice versa, using a TCP socket,
# a TCP connection must first be established between the client and server
# line 19 initiates teh TCP connection between the client and server
# the parameter of the connect() method is the address of the server side of the connection 
# after this line is executed, the three0way handshake is perfomed and the TCP connection is
# established between the client and server
clientSocket.connect((serverName, serverPort))

# same as the UDPClient script, this obtains a sentence from the user. The string
# sentence continues to gather characters until the user ends the line by typing a carriage return 
sentence = raw_input('Input lowercase sentence:')

# the code in line 2- sends the string sentence through the client's socket and into the TCP
# connection. Note that the program does not explicity create a packet and attach the 
# destination address to the packet, as was the case with UDP sockets. 
# Instead the client program simply drops the bytes in the string sentence into the TCP connection
# The client then waits to recieve bytes from the server.
clientSocket.send(sentence)

# when characters arrive from the server, they get placed into the string modifiedSentence.
# Characters continue to accumulate in modifiedSentence until the ilne ends with a carriage return character.
modifiedSentence = clientSocket.recv(1024)


print('From Server:', modifiedSentence)

# After printing the capitalized setence, we close the client's socket
# Yes, this closes the TCP connection between the client and the server. 
# When the connection is terminated, it causes TCP in the client to send a TCP 
# message to the TCP in the server. 
clientSocket.close()
