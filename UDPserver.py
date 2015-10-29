#!/usr/bin/python
##################################################################################
import socket, IN
import sys
from hashlib import md5
import time
##################################################################################
#IP = "127.0.0.99";
#IP = socket.INADDR_BROADCAST;
#IP = socket.INADDR_ANY;
LOC_IP = "192.168.0.100";
#IP = "192.168.0.220";
REM_IP = "141.134.167.110";


UDP_PORT = 5555;
BUFFER_SIZE = 10240; # ???????????????????????????????
RECV_DATA = "";

SYP_CHR = "<<||>>";

##################################################################################
def _calcDigest(_str, _bytes=4):
    # ---------------------------------------------------
    return md5(_str).hexdigest()[0:_bytes];
    # ---------------------------------------------------
##################################################################################
_SOCK = socket.socket(socket.AF_INET, socket.SOCK_DGRAM); # UDP
#_SOCK.setblocking(0); # This will rais an error if thereis no data


# ------------------------------------------------------------
#setsockopt() and getsockopt()

#_SOCK.setsockopt();
'''
try:
    _SOCK.setsockopt(socket.SOL_SOCKET, IN.SO_BINDTODEVICE, "eth1"+'\0');
except Exception as _sock_err:
    print _sock_err
    exit();
'''





# ------------------------------------------------------------
#_SOCK.connect((IP, UDP_PORT));
_SOCK.bind((IP, UDP_PORT));
CURRENT_IP, CURRENT_PORT = _SOCK.getsockname();

#print CURRENT_IP,':',CURRENT_PORT 
#_SOCK.listen(10); # ????????????????
#exit();
# ------------------------------------------------------------
print(" Serving on: "+str(CURRENT_IP)+':'+str(CURRENT_PORT));
# ------------------------------------------------------------
while True:
    RECV_DATA, ADDR = _SOCK.recvfrom(BUFFER_SIZE) # buffer size in bytes

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
    REM_UDP_PORT    = ADDR[1];

    time.sleep(1);
    
    if CHECK_SUM == RECV_DATA_ARR[0]:
        _SOCK.sendto("200: "+RECV_DATA_ARR[1], ADDR);
    else:
        _SOCK.sendto("500: Incorrect CHECK_SUM: "+RECV_DATA_ARR[0], ADDR);

    # ---------------------------------------------------------------------------------------------
    time.sleep(1);
    # ---------------------------------------------------------------------------------------------
    
##################################################################################
