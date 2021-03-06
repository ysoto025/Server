import sys
import socket
from sys import argv
import threading
import signal

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.settimeout(10.0)

if (len(argv) < 2) | (len(argv) > 2):
    sys.stderr.write("missing arguments or too many Arguments")
    sys.exit()

if argv[1] == "":
    sys.stderr.write("ERROR: empty string")
    sys.exit(1)

if (int(argv[1]) < 0) | (int(argv[1]) > 65535):
    sys.stderr.write("ERROR: Overflow error")
    sys.exit(1)

con = []
sock.bind(('0.0.0.0', int(argv[1])))
sock.listen(1)
data = ''
var = 0

def connector(d, e):
    global con
    global data
    word = 'accio\r\n'
    global var
    var = 0
    while True:
        d.send(bytes(word.encode()))
        a = d.recv(1).decode("utf-8")
        var = var + 1
        #print(var)
        if not a:
            con.remove(d)
            d.close()
            break


def signal_handler(sig, frame):
    sys.stderr.write("ERROR: SignalInterrupted")
    sys.exit(0)


try:

    while True:
        x, v = sock.accept()
        signal.signal(signal.SIGINT, signal_handler)
        cThread = threading.Thread(target=connector, args=(x, v))
        cThread.daemon = True
        cThread.start()
        con.append(x)
        print(var)

except socket.timeout:
    sys.stderr.write("ERROR: timeout")
    sys.exit(1)