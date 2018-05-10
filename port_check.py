import socket
import sys
import HTML 
import os

HOST=sys.argv[1]
PORT=sys.argv[2]
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(2)                                      #2 Second Timeout
result = sock.connect_ex((HOST,int(PORT)))
if result == 0:
  result="port %s is open" %PORT
    #print ("port OPEN on %s" %HOST)
else:
  result="port %s is closed" %PORT
  #print ("port CLOSED on %s" %HOST)

t = HTML.Table(header_row=['HOST', 'RESULT'])
t.rows.append(['%s' %HOST, '%s' %result])
htmlcode = str(t)
sys.stdout=open("result.html","w")
print htmlcode
sys.stdout.close()