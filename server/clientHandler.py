import socketserver
import os
import time
import math


def getFiles(dir):
    return os.listdir("./registry/" + dir)


class UDPClientHandler(socketserver.BaseRequestHandler):
    """Docs of UDPCliet Handler"""

    def handle(self):
        client = self.client_address[0].replace(".", "-")
        data = str(self.request[0].strip(), "utf-8").split(";")
        time_group, tot_mens, seq_num, time_sent = data

        # Time diference between the time it arrives and it leaves
        time_diff = (time.time() - float(time_sent))*1000

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
