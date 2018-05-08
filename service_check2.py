import socket
import sys

HOST=sys.argv[1]
PORT=sys.argv[2]
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(2)                                      #2 Second Timeout
result = sock.connect_ex((HOST,PORT))
if result == 0:
  print ("port OPEN on %s" %HOST)
else:
  print ("port CLOSED on %s" %HOST)

