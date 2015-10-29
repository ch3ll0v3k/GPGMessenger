#!/usr/bin/python
##################################################################################
import socket, IN
import sys
from hashlib import md5
import time
##################################################################################

CLIENT = True;
# --------------------------------
if CLIENT: # CLIENT
    #LOC_IP = "192.168.0.220";
    #LOC_IP = "192.168.0.100";
    LOC_IP = "127.0.0.1";
    LOC_TCP_PORT = 0;
    
    #REM_IP = "141.134.167.110"; # <<<<< REM-NET
    #REM_IP = "192.168.0.100";   # <<<<< LOC-NET
    REM_IP = "127.0.0.1";
    REM_TCP_PORT = 5555;

else: # SERVER
    #LOC_IP = "192.168.0.220";
    #LOC_IP = "192.168.0.100";
    LOC_IP = "127.0.0.1";
    LOC_TCP_PORT = 5555;

    #REM_IP = "141.134.167.110"; # <<<<< REM-NET
    #REM_IP = "192.168.0.100";   # <<<<< LOC-NET
    REM_IP = "127.0.0.1";
    REM_TCP_PORT = 0;
# --------------------------------
BUFFER_SIZE = 10240;
RECV_DATA = "";
SYP_CHR = "<<||>>";

##################################################################################
def _calcDigest(_str, _bytes=4):
    # ---------------------------------------------------
    return md5(_str).hexdigest()[0:_bytes];
    # ---------------------------------------------------
##################################################################################
_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM); # TCP
_SOCK.bind((LOC_IP, LOC_TCP_PORT));

# ------------------------------------------------------------
OWN_IP, OWN_PORT = _SOCK.getsockname();

#_SOCK.listen(1);
#exit();

#_SOCK.accept();


_SOCK.connect((REM_IP, REM_TCP_PORT));
#_SOCK.setblocking(0); # This will rais an error if thereis no data
# ------------------------------------------------------------
_R = " \033[01;31m ";
_G = " \033[01;32m ";
_B1 = " \033[01;34m ";
_B2 = " \033[01;36m ";
_W = " \033[01;37m ";
_EN = " \033[0m ";
_Y = " \033[01;33m ";


# print(" ARGV: "+sys.argv[1]); exit;

_CL = None;
_DELAY = None;

if sys.argv[1] == "1":
    _CL = _W;
    _DELAY = 1;

elif sys.argv[1] == "2":
    _CL = _B1;
    _DELAY = 1;

elif sys.argv[1] == "3":
    _CL = _Y;
    _DELAY = 1;

FIRST_INIT_SEND = _G+" TCP_CLI: "+str(OWN_IP)+":"+str(OWN_PORT)+_EN+"\n";

print(FIRST_INIT_SEND);
print(_CL+": "+str(OWN_PORT)+_EN)
# ------------------------------------------------------------
_SOCK.send(FIRST_INIT_SEND);
# ------------------------------------------------------------

#exit();

# ------------------------------------------------------------
while True:

    # --------------------------------------------------------
    #RECV_DATA, ADDR = _SOCK.recv(BUFFER_SIZE) # buffer size in bytes
    RECV_DATA = _SOCK.recv(BUFFER_SIZE) # buffer size in bytes

    print(RECV_DATA);
    time.sleep(_DELAY);

    #REM_IP          = ADDR[0];
    #REM_TCP_PORT    = ADDR[1];

    
    _SOCK.send(_CL+"  :> RESP: "+RECV_DATA+_EN);
    time.sleep(_DELAY);

    # --------------------------------------------------------
    #time.sleep(1);
    # --------------------------------------------------------
    
##################################################################################
