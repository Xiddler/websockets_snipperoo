# websockets_snipperoo
** lanner with websockets using Flask

This little app provides a utility to copy snippets between devices on the same LAN.
e.g. If using a laptop and you want to copy a (long) URL to your phone this does it instantly.

This app is built with Flask and SocketIO.

Usage:

clone to your machine.
edit the templates/index.html to show the internal IP of the device you are serving from. This needs to be done only once.
var socket = io.connect('http://192.168.11.101:5000');  shows the IP of my laptop at home.
-> % python main.py


Browse to localhost:5000 on the laptop and to http://192.168.11.101:5000 on the other device.

This app is based on the ideas for a chat app but put to a different use.

2018-11-21
