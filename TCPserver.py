#!/usr/bin/python
##################################################################################
import socket, IN
import sys
from hashlib import md5
import time
from threading import Thread, Lock

##################################################################################
##################################################################################

class TCP_SERVER(object):
    # ======================================================================
    def __init__(self, arg=None):
        
        # ------------------------------------------------------------------
        self.arg                                    = arg;
        # ------------------------------------------------------------------
        # Server SETTINGS
        self.IS_CLIENT                              = False;

        self.BUFFER_SIZE                            = 10240;
        self.RECV_DATA                              = "";
        self.SYP_CHR                                = "<<||>>";

        self._ThreadLock                            = None;
        self._Thread                                = None;

        self._SOCKET                                = None;
        self._SOCK_OPT                              = { "no_blocking": True };

        self._MAIN_LOOP_DELAY                       = 0.25;
        # ------------------------------------------------------------------
        # Connection info
        self.LOC_IP                                 = None;
        self.LOC_TCP_PORT                           = None;
        
        self.REM_IP                                 = None;
        self.REM_TCP_PORT                           = None;

        #self.REM_IP                                = "141.134.167.110"; # <<<<< REM-NET
        #self.REM_IP                                = "192.168.0.100";   # <<<<< LOC-NET

        self.OWN_PORT                               = None;
        self.IP                                     = None;
        # ------------------------------------------------------------------
        self.CLIENTS_CONNS                          = [];
        self.CLIENTS_ADDRS                          = [];

        # ------------------------------------------------------------------
        self._R = " \033[01;31m ";
        self._G = " \033[01;32m ";
        self._B1 = " \033[01;34m ";
        self._B2 = " \033[01;36m ";
        self._W = " \033[01;37m ";
        self._Y = "\033[01;33m";

        self._EN = " \033[0m ";
        # ------------------------------------------------------------------
        return None;
        # ------------------------------------------------------------------

    # ======================================================================
    def _initParams(self):

        # ------------------------------------------------------------------
        try:

            if self.IS_CLIENT: # CLIENT

                print(self._G+" Configuring: CLIENT"+self._EN);
                #self.LOC_IP = "192.168.0.220";
                #self.LOC_IP = "192.168.0.100";
                self.LOC_IP = "127.0.0.1";
                self.LOC_TCP_PORT = 0;
                
                #self.REM_IP = "141.134.167.110"; # <<<<< REM-NET
                #self.REM_IP = "192.168.0.100";   # <<<<< LOC-NET
                self.REM_IP = "127.0.0.1";
                self.REM_TCP_PORT = 5555;

            else: # SERVER

                print(self._G+" Configuring: SERVER"+self._EN );
                #self.LOC_IP = "192.168.0.220";
                #self.LOC_IP = "192.168.0.100";
                self.LOC_IP = "127.0.0.1";
                self.LOC_TCP_PORT = 5555;

                #self.REM_IP = "141.134.167.110"; # <<<<< REM-NET
                #self.REM_IP = "192.168.0.100";   # <<<<< LOC-NET
                self.REM_IP = "127.0.0.1";
                self.REM_TCP_PORT = 0;

                return True;

        except Exception as _INIT_PARAMS_err:

            print(self._R+" _INIT_PARAMS_err: "+str(_INIT_PARAMS_err)+self._EN);
            return False;
        # ------------------------------------------------------------------

    # ======================================================================
    def _initSocket(self):

        # ------------------------------------------------------------------
        try:

            self._SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM); # TCP
            self._SOCK.bind((self.LOC_IP, self.LOC_TCP_PORT));
            
            if True:
                pass;
                #self._SOCK.setblocking(0); # This will rais an error if thereis no data
            
            self.OWN_IP, self.OWN_PORT = self._SOCK.getsockname();
            print(self._G+" TCP_SERVER: "+str(self.OWN_IP)+":"+str(self.OWN_PORT)+self._EN);
            print(" ------------------------------------------------ ");
            self._SOCK.listen(100);
            
            return True;

        except Exception as _SOCK_err:

            print(self._R+" _SOCK_err: "+str(_SOCK_err)+self._EN);
            return False;
        # ------------------------------------------------------------------

    # ======================================================================
    def _initThread(self):

        # ------------------------------------------------------------------
        try:

            self._ThreadLock = Lock();
            self._Thread = Thread(target=self._acceptNewConn, args=(1,1));
            self._Thread.start();
            return True;

        except Exception as _THREAD_err:

            print(self._R+" _THREAD_err: "+str(_THREAD_err)+self._EN);
            return False;

        # ------------------------------------------------------------------


    # ======================================================================
    def _acceptNewConn(self, P_1, P_2):

        # ------------------------------------------------------------------
        try:
            
            #print(" NEW_START:")
            #self._ThreadLock.acquire();

            RAW = self._SOCK.accept();
            print(self._G+" NEW_TCP_CLIENT: ["+str(RAW[1])+"]"+self._EN)
            #exit();
            self.CLIENTS_CONNS.append(RAW[0]);
            self.CLIENTS_ADDRS.append(RAW[1]);

            #self._ThreadLock.release();
            #print(" NEW_END:")
            self._acceptNewConn(0,0);

        except Exception as _ACCEPT_CONN_err:

            #print(str(_ACCEPT_CONN_err));
            print(self._R+" _ACCEPT_CONN_err: "+str(_ACCEPT_CONN_err)+self._EN);
            #return False;
            sleep(self._MAIN_LOOP_DELAY);
            self._acceptNewConn(0,0);
        # ------------------------------------------------------------------
    
    # ======================================================================
    def _calcDigest(self, _str, _bytes=4):
        
        # ------------------------------------------------------------------
        try:

            return md5(_str).hexdigest()[0:_bytes];

        except Exception as _CALC_DIGEST_err:

            print(self._R+" _CALC_DIGEST_err: "+str(_CALC_DIGEST_err)+self._EN);
            return False;
        # ------------------------------------------------------------------
    
    # ======================================================================
    def _run(self):
        
        # ------------------------------------------------------------------
        _passed = 0;
        # ------------------------------------------------------------------
        try:
            """ -------------------------------------------------------- """
            
            #print(" TCP-Server @ "+str(self.OWN_IP)+":"+str(self.OWN_PORT));
            # ------------------------------------------------------------
            while True:

                # --------------------------------------------------------
                #if True:
                try:

                    """ ------------------------------------------------- """
                    if len(self.CLIENTS_CONNS) != 0:
                        
                        LAST = 0;
                        for x in xrange(0, len(self.CLIENTS_CONNS)):

                            try:

                                LAST = x;
                                print(" ::> "+self.CLIENTS_CONNS[x].recv(self.BUFFER_SIZE));

                            except Exception as _RECIEVE_err_:

                                print(self._R+" CLIENT:RECV: "+str(self.CLIENTS_ADDRS[LAST])+" EXIT"+self._EN)
                                self.CLIENTS_CONNS[LAST].close();
                                
                                self.CLIENTS_CONNS.pop(LAST);
                                self.CLIENTS_ADDRS.pop(LAST); #.pop();
                                
                                #print("_RECIEVE_err_: "+str(_RECIEVE_err_));


                        try:
                            LAST = 0;
                            for x in xrange(0, len(self.CLIENTS_CONNS)):

                                LAST = x;
                                self.CLIENTS_CONNS[x].send("["+str(self.CLIENTS_ADDRS[x])+"]");

                        except Exception as _SENDerr_:

                            print(self._R+" CLIENT:SEND: "+str(self.CLIENTS_ADDRS[LAST])+" EXIT"+self._EN)
                            self.CLIENTS_CONNS[LAST].close();
                            
                            self.CLIENTS_CONNS.pop(LAST);
                            self.CLIENTS_ADDRS.pop(LAST); #.pop();
                            
                            #print("_SENDerr_: "+str(_SENDerr_))

                    else:
                        print(self._B1+" No-clints available."+self._EN)
                    """ ------------------------------------------------- """
                    
                    '''
                    print("GET: "+str(_passed))
                    RAW = _SOCK.accept();

                    print(" NEW_TCP_CLIENT: ["+str(RAW[1])+"]")
                    #exit();
                    
                    CLIENTS_CONN.append(RAW[0]);
                    CLIENTS_ADDR.append(RAW[1]);

                    RECV_DATA = RAW[0].recv(BUFFER_SIZE) # buffer size in bytes

                    print(RECV_DATA);
                    
                    RAW[0].send(" Welcome ["+str(RAW[1])+"]");
                    '''

                    time.sleep(self._MAIN_LOOP_DELAY);
                    """ ------------------------------------------------- """

                except Exception as _err:

                    _passed += 1;

                    print("_err: "+str(_err))
                    print("_passed: "+str(_passed))
                    time.sleep(self._MAIN_LOOP_DELAY);

                # --------------------------------------------------------
                #time.sleep(1);
                # --------------------------------------------------------

            """ -------------------------------------------------------- """
        except Exception as _RUN_err:

            print(" _RUN_ERR: "+str(_RUN_err));
            return False;
        finally:

            print("finally")
            '''
            for x in xrange(0, len(self.CLIENTS_CONNS)):

                try:

                    self.CLIENTS_CONNS[x].close();
                    self.CLIENTS_CONNS[x].pop();
                    self.CLIENTS_ADDRS[x].pop();
                    

                except Exception as _CLOSE_err_:
                    print("_CLOSE_err_");
            '''
        # ------------------------------------------------------------------        

    # ======================================================================
    # ======================================================================

##################################################################################    
##################################################################################
if __name__ == '__main__':

    TCPServer = TCP_SERVER();

    if TCPServer._initParams():

        if TCPServer._initSocket():

            if TCPServer._initThread():

                TCPServer._run();
            else:
                print(TCPServer._R+"TCPServer._initThread()"+TCPServer._EN);

        else:
            print(TCPServer._R+"TCPServer._initSocket()"+TCPServer._EN);

    else:
        print(TCPServer._R+"TCPServer._initParams()"+TCPServer._EN);


