from socket import *

# if we use a hostname below instead of an IP address, then a DNS lookup will automatically be performed to get the IP address
serverName = '' # sets the string serverName to hostname: provide a string containing either the IP address ("128.138.32.126") <-- (this is an example IP.. use your own ip address..) of the or hostname ("cis.poly.edu") of the server
serverPort = 12000 # don't change this lol

# the first parameter in socket() indicates the address family, where AF_INET indicates that the uderlying network is using IPv4
# the second parameter indicates that the socket is of type SOCK_DGRAM, which means it is a UDP socket
clientSocket = socket(AF_INET,SOCK_DGRAM) # create socket
# note that I'm not specifying the port number of the client socket when it's created, instead letting the operatin system do this for us


# raw_python() is a built-in python function. Upon execution, the user at the client is prompted with the words "Input data:",
# then using her keyboard to input the a line, which is put into the variable message
message = raw_input('Input lowercase sentence:')



# the sendto() method attaches the destination address 
# (comprising the serverName and serverPort) to the 
# message and sends the resulting packet into the 
# process' socket, clientSocket
clientSocket.sendto(message,(serverName, serverPort)) 

# when the packet arrives from the internet at the client's socket, the packet's data is put into the variable 
# modifiedMessage and the packet's source address is put into the variable serverAddress
# serverAddress carries both the server's IP address and port number
# the method recvfrom also takes the buffer size 2048 as input (this buffer size works for most purposes)
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

# this should print out the modifiedMessage string, yielding the same input string but with all caps
print(modifiedMessage)

# closes the socket, then the process terminates 
clientSocket.close()
