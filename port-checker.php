<?php 
    
    $address=$_SERVER['REMOTE_ADDR'];

    if (isset($_REQUEST['port']) and (!strlen($_REQUEST['port'])==0))
        $port=$_REQUEST['port'];
    else
        unset($port);
     
    if (isset($port)){
        
        if($socket=socket_create(AF_INET, SOCK_STREAM, SOL_TCP){
            if(socket_connect($socket, $address, $port))){
                
                $text="Connection successful on IP $address, port $port";
                socket_close($socket);
            
            }
        }
    }else{
      $text = 'Unable to connect<pre>'.socket_strerror(socket_last_error()).'</pre>';
    }
     

     
    echo '<html><head></head><body>'.
         $text.
         '</body></html>';


?>