#!/usr/bin/env python

# skeleton from http://kmkeen.com/socketserver/2009-04-03-13-45-57-003.html

import socketserver, subprocess, sys
from threading import Thread
from pprint import pprint
import json
import re

my_unix_command = ['bc']
HOST = 'localhost'
PORT = 12321

class MapHandler:
    with open('gamemap.map', 'r') as content_file:
        serverMap = content_file.read()
    def refreshMap(self):
        with open('gamemap.map', 'r') as content_file:
            serverMap = content_file.read()

class SingleTCPHandler(socketserver.BaseRequestHandler):
    "One instance per connection.  Override handle(self) to customize action."
    def handle(self):
        print ("%s connected", self.client_address[0])
        MapHandler().refreshMap()
        sentMap = MapHandler().serverMap
        self.request.send(sentMap.encode())
        while True:
            data = self.request.recv(1024)
            if not data: break
            text = data.decode('utf-8')
            print("Client wrote: ", text)
            if text.startswith('getmap'):
                MapHandler().sendMap()
            else:
                pass
                #trukafaire la (reponse du client)
                #self.request.send(response.encode())
        print ("%s disconnected", self.client_address[0])
                            
class SimpleServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    daemon_threads = True
    allow_reuse_address = True
            
def __init__(self, server_address, RequestHandlerClass):
    socketserver.TCPServer.__init__(self, server_address, RequestHandlerClass)
                
if __name__ == "__main__":
    server = SimpleServer((HOST, PORT), SingleTCPHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        sys.exit(0)
