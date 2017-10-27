import socketserver
import os
import time
import math
import sys
from socket import *
import hashlib


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
                    print("Han llegado " + str(self.file_len(f.name)) +" de " +str(tot_mens)+ " mensajes.")
            else:
                with open("registry/" + client + "/" + filename, "w+") as f:
                    registry = "{0}:{1} ms\n".format(seq_num, time_diff)
                    f.write("{}\n".format(tot_mens))
                    f.write(registry)

        elif "files" in data and len(data) == 5:
            file,filename,hash,type,currentTime = data
            filepath = "./repo/{}".format(client)
            if not os.path.isdir(filepath):
                os.mkdir("./repo/{}".format(client))
            dta = bytes(file,"utf-8")
            hash_object = hashlib.sha1(dta).hexdigest()
            time_diff = time.time() - float(currentTime)
            with open("repo/" + client + "/" + filename, 'wb') as f:
                if(time_diff != 0.0):
                #if hash == hash_object:
                    f.write(dta)
                    print("Se ha transferido parte del archivo en " + str(time_diff) + " milisegundos.")
                    time_diff = time.time() - float(currentTime)
                else:
                    datos = self.request[0]
                    data = str(datos.strip(), "utf-8").split(";")
                    file, filename, hash, type, currentTime = data
                    dta = bytes(file, "utf-8")
                    hash_object = hashlib.sha1(dta).hexdigest()
                    time_diff = time.time() - float(currentTime)
                    f.write(dta)
                    print("Se ha transferido parte del archivo en " + str(time_diff) + " segundos.")
    def file_len(self,fname):
        non_blank_count = 0
        with open(fname) as infp:
            for line in infp:
                if line.strip():
                    non_blank_count += 1
        return non_blank_count