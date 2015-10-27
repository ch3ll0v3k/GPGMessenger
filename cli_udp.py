#!/usr/bin/python
##################################################################################
import socket
import sys
from hashlib import md5

##################################################################################
HOST = "127.0.0.99";
PORT = 5435;
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
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM); # UDP
    s.connect((HOST, PORT));

    RAW_STR             = sys.argv[1];
    CHECK_SUM_LEN       = 10;
    CHECK_SUM           = _calcDigest(RAW_STR, _bytes=CHECK_SUM_LEN)
    DATA_TO_SEND        = CHECK_SUM + SYP_CHR + RAW_STR + SYP_CHR + str(CHECK_SUM_LEN) + SYP_CHR;

    s.send(DATA_TO_SEND);

else:
    print(" No data:");

# ---------- >>>

#exit();

while True:
    RECV_DATA, addr = s.recvfrom(BUFFER_SIZE) # buffer size isbytes
    print(RECV_DATA);
    break;

##################################################################################
