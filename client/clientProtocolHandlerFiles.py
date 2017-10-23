import sys
import socket
import time
import os
from tkinter import *


BUFFER_SIZE = 1024

def handler(sock, address, size, filename,frameFiles):
    timestamp_now = time.time()
    timestamp_ms = time.time() * 1000
    f = open("files/" + size + "/" + filename, "rb")
    data = f.read(BUFFER_SIZE)
    gettext = Text(frameFiles, height=10, width=80, wrap=WORD)
    msj = "{0};{1};{2}".format(data, filename,"files")
    while (data):
        if (sock.sendto(bytes(msj,"utf-8"), address)):
            data = f.read(BUFFER_SIZE)
            msj = "{0};{1};{2}".format(data, filename,"files")
    gettext.insert(END, "Finished... Closed the connection. Bye! \n")
    sock.close()
    f.close()

def client(ip, port, size,filename, gettext):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        handler(sock, (ip, port), size,filename,gettext)


if __name__ == "__main__":
    IP, PORT = sys.argv[1], int(sys.argv[2])
    client(IP, PORT)
