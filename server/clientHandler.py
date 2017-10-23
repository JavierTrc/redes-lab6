import socketserver
import os
import time
import math
import chardet
import sys
BUFFER_SIZE = 1024
from socket import timeout


def getFiles(dir):
    return os.listdir("./registry/" + dir)


class UDPClientHandler(socketserver.BaseRequestHandler):
    """Docs of UDPClient Handler"""

    def handle(self):
        client = self.client_address[0].replace(".", "-")
        datos = self.request[0]
        data = str(datos.strip(),"utf-8").split(";")
        if "obj" in data and len(data) == 5:
            data = str(datos.strip(),"utf-8").split(";")
            time_group, tot_mens, seq_num, time_sent,type = data

            # Time diference between the time it arrives and it leaves
            time_diff = (time.time() - float(time_sent)) * 1000

            # Creating thr folder if it doesn't exists
            filepath = "./registry/{}".format(client)
            if not os.path.isdir(filepath):
                os.mkdir("./registry/{}".format(client))

            filename = str(math.floor(float(time_group)))

            if filename in getFiles(client):
                with open("registry/" + client + "/" + filename, "a") as f:
                    registry = "{0}:{1} ms\n".format(seq_num, time_diff)
                    f.write(registry)
            else:
                with open("registry/" + client + "/" + filename, "w+") as f:
                    registry = "{0}:{1} ms\n".format(seq_num, time_diff)
                    f.write("{}\n".format(tot_mens))
                    f.write(registry)

        elif "files" in data and len(data) == 3:
            # Creating thr folder if it doesn't exists
            file,filename,type = data
            filepath = "./repo/{}".format(client)
            if not os.path.isdir(filepath):
                os.mkdir("./repo/{}".format(client))
            f = open("repo/" + client + "/" + filename, 'wb')
            print ("Received part of File:", filename)
            while (datos):
                f.write(datos)
                datos, addr = self.request
