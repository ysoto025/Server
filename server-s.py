import sys
import socket
from sys import argv
import threading

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

try:
    while True:
        clientSock, address = sock.accept()
        file = clientSock.recv(1024).decode("utf-8")
        print(file)

        clientSock.close()
        sock.close()
except socket.timeout:
    sys.stderr.write("ERROR: timeout")
    sys.exit(1)

