import socket

HOST="10.0.3.167"
PORT=8080
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(2)                                      #2 Second Timeout
result = sock.connect_ex((HOST,PORT))
if result == 0:
  print 'port OPEN'
else:
  print 'port CLOSED, connect_ex returned: '+str(result)