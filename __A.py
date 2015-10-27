#!/usr/bin/python
##################################################################################
import socket

##################################################################################

HOST = "192.168.0.1";
PORT = 2427;
MESSAGE = "NTFY"; # "AUCX"
BUFFER_SIZE = 1024;
BUFFER_SIZE = 8;

RECV_DATA = "";

   

"""
print(socket.getaddrinfo(HOST, PORT));

The function returns a list of 5-tuples with the following structure:

(family, socktype, proto, canonname, sockaddr)

[
    (2, 1, 6, '', ('192.168.0.1', 2427)), 
    (2, 2, 17, '', ('192.168.0.1', 2427)), 
    (2, 3, 0, '', ('192.168.0.1', 2427))
]
"""

"""
print(socket.getaddrinfo(HOST, PORT, 0, 0, socket.IPPROTO_TCP));


(2, 1, 6, '', ('192.168.0.1', 2427))]


"""


"""
SOCK_CONF = socket.getaddrinfo(HOST, PORT, 0, 0, socket.IPPROTO_TCP);
SK = socket.connect(SOCK_CONF);
"""
"""
#exit();

s = socket.socket(socket.AF_UNIX, socket.SOCK_RAW);
s.connect((HOST, PORT));
s.send(MESSAGE);
#RECV_DATA = s.recv(BUFFER_SIZE);
s.close();
print(RECV_DATA);

"""



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM); # UDP
s.connect((HOST, PORT));
s.send(MESSAGE);
RECV_DATA = s.recv(BUFFER_SIZE);
s.close();

print "received data:", RECV_DATA;



s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM); # UDP
s.connect((HOST, PORT));
s.bind((HOST, PORT));
  
while True:
    RECV_DATA, addr = s.recvfrom(BUFFER_SIZE) # buffer size isbytes
    print "received message:", RECV_DATA






exit();



#SK = socket.create_connection(HOST, PORT);

#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM); # TCP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM); # UDP


s.connect((HOST, PORT));
s.send(MESSAGE);
RECV_DATA = s.recv(BUFFER_SIZE);
s.close();

print "received data:", RECV_DATA;



s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM); # UDP
s.connect((HOST, PORT));
s.bind((HOST, PORT));
  
while True:
    RECV_DATA, addr = s.recvfrom(BUFFER_SIZE) # buffer size isbytes
    print "received message:", RECV_DATA


""" 
echo "hello" > /dev/tcp/192.168.0.1/2427
echo "hello" > /dev/udp/192.168.0.1/2427

sendip -v -p ipv4 -is 192.168.0.100 -p tcp -us 2427 -ud 2427 -d "NTFY"  -id 192.168.0.1

sendip -p ipv4 -is 192.168.0.100 -p udp -us 5070 -ud 2427 -d "NTFY" -v -id 192.168.0.1


"""


##################################################################################
