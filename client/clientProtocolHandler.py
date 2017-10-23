import sys
import socket
import time


def handler(sock, address, num_mens):
    timestamp_now = time.time()
    for i in range(0, num_mens):
        timestamp_s = time.time()
        msj = "{0};{1};{2};{3};{4}".format(timestamp_now,num_mens, i, timestamp_s,"obj")
        sock.sendto(bytes(msj, "utf-8"), address)

def client(ip, port, num_obj=5):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        handler(sock, (ip, port), num_obj)


if __name__ == "__main__":
    IP, PORT = sys.argv[1], int(sys.argv[2])
    client(IP, PORT)
