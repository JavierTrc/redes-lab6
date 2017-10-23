import sys
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
        hash_object = hashlib.sha1(data).hexdigest()
        msj = "{0};{1};{2};{3}".format(data, filename, hash_object, "files")
        while (data):
            if (sock.sendto(bytes(msj,"utf-8"), address)):
                data = f.read(BUFFER_SIZE)
                hash_object = hashlib.sha1(data).hexdigest()
                msj = "{0};{1};{2};{3}".format(data, filename,hash_object,"files")
    sock.close()
    f.close()

def client(ip, port, size,filename,buffer):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        handler(sock, (ip, port), size,filename, buffer)


if __name__ == "__main__":
    IP, PORT = sys.argv[1], int(sys.argv[2])
    client(IP, PORT)
