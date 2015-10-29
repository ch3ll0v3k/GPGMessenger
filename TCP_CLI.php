<?php

/* Get the port for the WWW service. */

$service_port = getservbyname('www', 'tcp');

/*if you already know the destination port, you don't need getservbyname, 
you can do this: $service_port = port;

Example: $service_port="10000″;*/

/* Get the IP address for the target host. */

$address = gethostbyname('www.example.com');

/*if you already know the ip of the destination, you don't need gethostbyname, you can do this: $address = ip address;

Example: $address = 192.168.10.1 */

/* Create a TCP/IP socket. */

$socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP); // SOCK_DGRAM

if ($socket === false) {

    echo "socket_create() failed: reason: " . socket_strerror(socket_last_error()) . "\n";

} else {

    echo "OK.\n";

}

echo "Attempting to connect to '$address' : '$service_port'…";

$result = socket_connect($socket, $address, $service_port);

if ($result === false) {

    echo "socket_connect() failed.\nReason: ($result) " . socket_strerror(socket_last_error($socket)) . "\n";

} else {

    echo "OK.\n";

}

$in = "message to send\n";

$out = "";

echo "Sending message…";

socket_write($socket, $in, strlen($in));

echo "OK.\n";

echo "Reading response:\n\n";

$out = socket_read($socket, 2048);

echo $out;

$in = "second message\n";

echo "write: second message\n";

socket_write($socket, $in, strlen($in));

echo "Reading response:\n\n";

socket_read($socket, strlen($in));

echo $out;

echo "Closing socket…";

socket_close($socket);

echo "OK.\n\n";

?>