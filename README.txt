********** A simple client-server application using TCP ********** 

 ---------- NOTES ON TCP SOCKETS & PROGRAMMING WITH TCP ----------
  TCP (Transmission Control Protocol): The Transmission Control Protocol is one of
  the main protocols of the Internet protocol suite. It originated in the initial 
  network implementation in which it complemented the Internet Protocol. 
  Therefore, the entire suite is commonly referred to as TCP/IP.

  Use cases: The Transmission Control Protocol (TCP) is a communications standard 
  that enables application programs and computing devices to exchange messages 
  over a network. It is designed to send packets across the internet and ensure 
  the successful delivery of data and messages over networks.

  UDP/TCP disparity: TCP is a connection-oriented protocol, 
  whereas UDP is a connectionless protocol. The speed for TCP is 
  slower while the speed of UDP is faster. ... TCP does error checking and 
  also makes error recovery, on the other hand, UDP performs error checking, 
  but it discards erroneous packets.

  When creating the TCP connection, we associate 
  with it the client socket address (IP address and port number) 
  and the server socket address (IP address and port number). 
  With the TCP connection established, when one side wants to send 
  data to the other side, it just drops the data into the TCP connection 
  via its socket. *** This is different from UDP, for which the server must 
  attach a destination address to the packet before dropping it into the socket. ***

  In server programs using TCP, the client has the job of initiating contact with the server.
  In order for the server to be able to react to the client's initial contact, the server has
  to be ready. This implies two things: first, as in the case of UDP, the TCP
  server must be running as a process before the client attempts to initiate contact. 
  Second, the server program must have a special door.. aka a special socket that welcomes
  some initial contact from a client process running on an arbitrary host.

   With the server process running, the client process can initiate a TCP connection
   to the server. This is done in the client program by creating a TCP socket. 
   When the client creates its TCP socket, it specifies the address of the welcoming 
   socket in the server, namely, the IP address of the server host and the port 
   number of the socket. After creating its socket, the client initiates a 
   three-way handshake and establishes a TCP connection with the server. 
   The three-way handshake, which takes place within the transport layer, 
   is completely invisible to the client and server programs.

   During the three-way handshake, the client process knocks on the welcoming 
   door of the server process. When the server “hears” the knocking, 
   it creates a new door— more precisely, a new socket that is dedicated 
   to that particular client. 

   ***** FOR STUDENTS NEW TO TCP SOCKETS:
   try not to confuse the welcoming socket (which is the initial point of contact for all 
   clients wanting to communicate with the server), and each newly created 
   server-side connection socket that is subsequently created for communicating 
   with each client. *****

 ---------- WHAT THIS APPLICATION DOES ----------
The client sends one line of data to the server, 
the server capitalizes the line and sends it back to the client..
just like in our UDP program except this time we're using a TCP connection. 


 --------- HOW TO RUN THIS PROGRAM ---------
To test the pair of programs, you install and compile TCPClient.py 
in one host and TCPServer.py in another host. Be sure to include the 
proper hostname or IP address of the server in TCPClient.py. Next, you 
execute TCPServer.py, the com- piled server program, in the server host. 
This creates a process in the server that idles until it is contacted by 
some client. Then you execute UDPClient.py, the com- piled client program, 
in the client. This creates a process in the client. Finally, to use the 
application at the client, you type a sentence followed by a carriage return.
To develop your own UDP client-server application, you can begin by slightly 
modifying the client or server programs. For example, instead of con- verting 
all the letters to uppercase, the server could count the number of times the 
letter s appears and return this number. Or you can modify the client so that 
after receiving a capitalized sentence, the user can continue to send more 
sentences to the server.
