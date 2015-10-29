#!/usr/bin/python
##################################################################################
import socket
import sys
from hashlib import md5

##################################################################################
#IP = "192.168.0.100";
#IP = "192.168.0.220";
#IP = "141.134.167.110";

LOC_IP = "192.168.0.100";
REM_IP = "141.134.167.110";


REM_UDP_PORT = 10000;
LOC_UDP_PORT = 10000;

BUFFER_SIZE = 10240;
RECV_DATA = "";

SYP_CHR = "<<||>>";

##################################################################################
def _calcDigest(_str, _bytes=4):
    # ---------------------------------------------------
    return str(md5(_str).hexdigest())[0:_bytes];
    # ---------------------------------------------------

##################################################################################
if len(sys.argv) > 1:
    
    _SOCK = socket.socket(socket.AF_INET, socket.SOCK_DGRAM); # UDP
    
    _SOCK.bind((LOC_IP, LOC_UDP_PORT));
    _SOCK.connect((REM_IP, REM_UDP_PORT));

    RAW_STR             = sys.argv[1];
    CHECK_SUM_LEN       = 10;
    CHECK_SUM           = _calcDigest(RAW_STR, _bytes=CHECK_SUM_LEN)
    DATA_TO_SEND        = CHECK_SUM + SYP_CHR + RAW_STR + SYP_CHR + str(CHECK_SUM_LEN) + SYP_CHR;

    _SOCK.send(DATA_TO_SEND);


else:
    print(" No data:");

# ---------- >>>
CURRENT_IP, CURRENT_PORT = _SOCK.getsockname();

print("LOC_SET: "+str(CURRENT_IP)+":"+str(CURRENT_PORT));
#exit();

while True:
    
    print("START_RECV >>>");
    RECV_DATA, addr = _SOCK.recvfrom(BUFFER_SIZE) # buffer size isbytes
    print(RECV_DATA);
    print("<<< END_RECV");
    #break;

    RECV_DATA+"-A"

    CHECK_SUM           = _calcDigest(RECV_DATA, _bytes=CHECK_SUM_LEN)
    DATA_TO_SEND        = CHECK_SUM + SYP_CHR + RECV_DATA + SYP_CHR + str(CHECK_SUM_LEN) + SYP_CHR;    
    _SOCK.send(DATA_TO_SEND);

##################################################################################
