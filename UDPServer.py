from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)

# anyone who sends a packet to the port 12000 at the IP address of the server, that packet will be directed to this socket
serverSocket.bind(('',serverPort)) # binds the port number 12000 to the server's socket
print("The server is ready to receieve..aka.. she's ready")

# UDPServer then enters a while loop; the while loop will allow UDPServer to recieve and process packets from
# clients indefinitely. In this loop, UDPServer waits for a packet to arrive
while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMesage = message.upper() # modifies the input message by making the characters upper case
    serverSocket.sendto(modifiedMesage, clientAddress)
    
    