from socket import *


serverPort = 12000

# line 7 creates a TCP socket using AF_INET to indicate IPv4 and SOCK_STEAM to indicate a TCP connection
serverSocket = socket(AF_INET, SOCK_STREAM)

# here I'm associating/binding the server port number serverPort with this socket
serverSocket.bind(('', serverPort))

# with TCP, serverSocket will be our welcoming socket. After establishing this 
# welcome door, it will wait and listen for some client to "knock on the door"
# This line has the server listen for TCP connection requests from the client. 
# The parameter specifies the maximum number of queued connections (at least 1)
serverSocket.listen(1)


print('The server is ready to receive')

while 1:
    
    # when a client knocks on this door, the program invokes the accept() 
    # method for serverSocket. This creates a new socket in the server, 
    # called connectionSocket. This socket will be dedicated to 
    # this particular client.
    # after the client and server finish the handshake, and create a TCP connection
    # the client's clientSocket and the server's connectionSocket
    # with the TCP connection established, the client and server can now send bytes
    # to each other over the connection.
    # With TCP, all bytes sent from one side are not only 
    # guaranteed to arrive at the other side but also guaranteed 
    # to arrive in order. 
    connectionSocket, addr = serverSocket.accept()
    
    
    sentence = connectionSocket.recv(1024)
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence)
    
    # after sending the modified sentence to the client, 
    # the connection socket is terminated/closed but since serverSocket remains
    # open, another client can now knock on the door and send the server a sentence 
    # to modify 
    connectionSocket.close()