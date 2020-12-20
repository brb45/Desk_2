#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 1 - search4.py

import socket
sock = socket.socket()
sock.connect(('maps.google.com', 80))
sock.sendall(
   'GET /maps/place/157+Beacon+Dr,+Milpitas,+CA+95035/@37.4347988,-121.87844,17z/data=!3m1!4b1!4m5!3m4!1s0x808fcee0d56d0779:0xf374dd6c54102161!8m2!3d37.4347988!4d-121.8762513'
   '&output=json&oe=utf8&sensor=false HTTP/1.1\r\n'
   'Host: maps.google.com:80\r\n'
   'User-Agent: search4.py\r\n'
   'Connection: close\r\n'
   '\r\n')
rawreply = sock.recv(4096)
print rawreply

import socket
hostname = 'www.litepoint.com'
addr = socket.gethostbyname(hostname)
print('The address of', hostname, 'is', addr)