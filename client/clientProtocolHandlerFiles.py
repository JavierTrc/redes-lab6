import sys
from socket import *
import socket
import time
import os
from tkinter import *
import hashlib

BUFFER_SIZE = 1024

def handler(sock, address, size, filename, buffer):
    timestamp_now = time.time()
    timestamp_ms = time.time() * 1000
    if (buffer != ""):
        BUFFER_SIZE = buffer
    with open("files/" + size + "/" + filename, "rb") as f:
        data = f.read(BUFFER_SIZE)
        timestamp_s = time.time()
        hash_object = hashlib.sha1(data).hexdigest()
        msj = "{0};{1};{2};{3};{4}".format(data, filename, hash_object, "files",timestamp_s)
        try:
            while (data):
                timestamp_s = time.time()
                sock.settimeout(2)
                if (sock.sendto(bytes(msj,"utf-8"), address)):
                    data = f.read(BUFFER_SIZE)
                    msj = "{0};{1};{2};{3};{4}".format(data, filename,hash_object,"files",timestamp_s)
                    hash_object = hashlib.sha1(data).hexdigest()
        except timeout:
            f.close()
            sock.close()
            print ("File Downloaded")

def client(ip, port, size,filename,buffer):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        handler(sock, (ip, port), size,filename, buffer)


if __name__ == "__main__":
    IP, PORT = sys.argv[1], int(sys.argv[2])
    client(IP, PORT)
