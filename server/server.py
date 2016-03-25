import sys
import SocketServer
from myTCPHandler import MyTCPHandler

host = 'localhost'
port = 8080

# Create the server, binding to localhost on port 8080
server = SocketServer.TCPServer((host, port), MyTCPHandler)

# Server will run forever
try:
    server.serve_forever()
except KeyboardInterrupt:
    sys.exit(0)
