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
    return md5(_str).hexdigest()[0:_bytes];
    # ---------------------------------------------------
##################################################################################



s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM); # UDP
#s.connect((HOST, PORT));
s.bind((HOST, PORT));

print(" Serving on");
  
while True:
    RECV_DATA, ADDR = s.recvfrom(BUFFER_SIZE) # buffer size isbytes

    RECV_DATA_ARR = RECV_DATA.split(SYP_CHR);
    
    uBytes = int(RECV_DATA_ARR[2]);

    CHECK_SUM = _calcDigest(RECV_DATA_ARR[1], _bytes=uBytes);
    # ---------------------------------------------------------------------------------------------
    #print("----------------------------------------------------------------------------");
    if RECV_DATA_ARR[0] == CHECK_SUM:
        print(" Got correct mesage with signature from: "+str(ADDR));
        print("\t | "+RECV_DATA_ARR[0]+" | "+RECV_DATA_ARR[1]+" | "+RECV_DATA_ARR[2]+" |");
    else:
        print(" Error: Checksum is incorrect!");
        print("\t | "+RECV_DATA_ARR[0]+" | "+RECV_DATA_ARR[1]+" | "+RECV_DATA_ARR[2]+" |");
    # ---------------------------------------------------------------------------------------------
    # extra info 

    REM_IP      = ADDR[0];
    REM_PORT    = ADDR[1];

    
    if CHECK_SUM == RECV_DATA_ARR[0]:
        s.sendto("200: "+RECV_DATA_ARR[1], ADDR);
    else:
        s.sendto("500: Incorrect CHECK_SUM: "+RECV_DATA_ARR[0], ADDR);

    # ---------------------------------------------------------------------------------------------
    

    #(DATA_TO_SEND += CHECK_SUM + SYP_CHR + RAW_STR SYP_CHR + SYP_CHR + CHECK_SUM_BYTES_LEN + SYP_CHR)



    #print "received message:", RECV_DATA
    #.send("200 - Recvd: "+RECV_DATA);
##################################################################################
