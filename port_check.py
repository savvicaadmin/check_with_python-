import socket
import sys
import HTML 
import os


HOST, PORT, result, htmlcode = None,None,None,None
API_PORT_list = [80,443,22,9001,6556]
PORT_list = [22,9001,6556]
test_results = {}

with open("/home/arpit/my_workspace/python/python-git/API_host_name") as file1:
    API_host_list = [line.strip() for line in file1]
with open("/home/arpit/my_workspace/python/python-git/DB_host_name") as file2:
    DB_host_list = [line.strip() for line in file2]


def check(HOST, PORT, result):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5) 
    result = sock.connect_ex((HOST,int(PORT)))
    sock.close()
    if result == 0:
        result="OPEN"
    else:
        result="CLOSED"  
    # dictionary of test results, indexed by test id:
    test_results[PORT]=result
    # dict of colors for each result:
    result_colors = {
        'OPEN':      'lime',
        'CLOSED':      'red',
        }
    t = HTML.Table(header_row=['PORT', 'result'])
    #for test_id in sorted(test_results):
    # create the colored cell:
    color = result_colors[test_results[PORT]]
    colored_result = HTML.TableCell(test_results[PORT], bgcolor=color)
    # append the row with two cells:
    t.rows.append([PORT, colored_result])
    htmlcode2 = str(t)
    sys.stdout=open("result.html","a")
    print htmlcode2
#    pint "------------------------------------------------------------------------------------------------------------------"
    sys.stdout.close()


for HOST in API_host_list:
    s = HTML.Table(header_row=[HOST])
#    s.rows.append([HOST])
    htmlcode = str(s)
    sys.stdout=open("result.html","a")
    print htmlcode
    sys.stdout.close()
    for PORT in API_PORT_list:
        check(HOST, PORT, result)        
        continue
    sys.stdout=open("result.html","a")
    print "------------------------------------------------------------------------------------------------------------------"
    sys.stdout.close()

for HOST in DB_host_list:
    del PORT_list[-1]
    s = HTML.Table(header_row=[HOST])
#    s.rows.append([HOST])
    htmlcode = str(s)
    sys.stdout=open("result.html","a")
    print htmlcode
    sys.stdout.close()
    if HOST == "stgadmindb.fliplearn.com":
        PORT_list.append(27017)
    else:
        pass
    PORT_list.append(3306)
    for PORT in PORT_list:
        check(HOST, PORT, result)
        continue
    sys.stdout=open("result.html","a")
    print "------------------------------------------------------------------------------------------------------------------"
    sys.stdout.close()
        
        
        
    
