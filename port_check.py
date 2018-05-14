import socket
import sys
import HTML 
import json


result=None
test_results = {}
with open('/home/arpit/my_workspace/python/python-git/port_details.json') as data_file:    
    data = json.load(data_file)


def check(HOST, PORT, result):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(20) 
    result = sock.connect_ex((HOST,int(PORT)))
    sock.close()
    if result == 0:
        result="OPEN"
    else:
        result="CLOSED"  
    test_results[PORT]=result
    result_colors = {
        'OPEN':      'lime',
        'CLOSED':      'red',
        }
    t = HTML.Table(header_row=['PORT', 'result'])
    color = result_colors[test_results[PORT]]
    colored_result = HTML.TableCell(test_results[PORT], bgcolor=color)
    t.rows.append([PORT, colored_result])
    htmlcode2 = str(t)
    sys.stdout=open("result.html","a+")
    print htmlcode2
    sys.stdout.close()


for HOST, PORT_fst_iter in data.iteritems():
    s = HTML.Table(header_row=[HOST])
    htmlcode = s
    sys.stdout=open("result.html","a+")
    print htmlcode
    sys.stdout.close()
    PORT_2nd_iter = PORT_fst_iter
    for PORT in PORT_2nd_iter:
        check(HOST, PORT, result)        
    sys.stdout=open("result.html","a+")
    print "------------------------------------------------------------------------------------------------------------------"
    sys.stdout.close()
