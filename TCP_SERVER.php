<?php

/* Allow the script to hang around waiting for connections. */

set_time_limit(0);

/* Turn on implicit output flushing so we see what we're getting as it comes in. */

ob_implicit_flush();

$LOC_IP = '100.220.110.5';
$LOC_IP = '192.168.0.100';

$LOC_PORT = 10000;

// SOCK_DGRAM
// SOCK_STREAM

// If the desired protocol is TCP, or UDP the corresponding constants 
// SOL_TCP, and SOL_UDP can also be used. 

if (($sock = socket_create(AF_INET, SOCK_STREAM, SOL_TCP)) === false) {

    echo "socket_create() failed: reason: " . socket_strerror(socket_last_error()) . "\n";

}

if (socket_bind($sock, $LOC_IP, $LOC_PORT) === false) {

    echo "socket_bind() failed: reason: " . socket_strerror(socket_last_error($sock)) . "\n";

}else{
    echo "SERVER_START @ $LOC_IP:$LOC_PORT\n";
}

if (socket_listen($sock, 5) === false) {

    echo "socket_listen() failed: reason: " . socket_strerror(socket_last_error($sock)) . "\n";

}else{
    echo "SERVER_LISTEN @ $LOC_IP:$LOC_PORT\n";
}

do {

    if (($msgsock = socket_accept($sock)) === false) {

        echo "socket_accept() failed: reason: " . socket_strerror(socket_last_error($sock)) . "\n";
        break;

    }else{
        echo "string";
    }

    do {

        if (false === ($buf = socket_read($msgsock, 2048, PHP_NORMAL_READ))) {

            echo "socket_read() failed: reason: " . socket_strerror(socket_last_error($msgsock)) . "\n";
            break 2;
        }

        $talkback = "PHP: You said '$buf'.\n";

        socket_write($msgsock, $talkback, strlen($talkback));

        echo "$buf\n";

    } while (true);


    socket_close($msgsock);

} while (true);

socket_close($sock);

?>