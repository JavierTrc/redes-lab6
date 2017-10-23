from tkinter import *
import clientProtocolHandler
import clientProtocolHandlerFiles
import os


class App:
    paso = 1

    def getFiles(self, dir):
        return os.listdir("./files/" + dir)

    def __init__(self, master):

        frame = Frame(master)
        frameFiles = Frame(master)

        frame.grid(row=0, column=0, sticky='news')
        frameFiles.grid(row=0, column=0, sticky="news")

        # Server selection input
        Label(frame, text="Server IP: ").grid(row=0, stick=W)
        Label(frame, text="Server Port: ").grid(row=1, stick=W)
        Label(frame, text="# of Objects: ").grid(row=2, stick=W)

        self.ip_input = Entry(frame)
        self.ip_input.grid(row=0, column=1)

        self.port_input = Entry(frame)
        self.port_input.grid(row=1, column=1)

        self.num_input = Entry(frame)
        self.num_input.grid(row=2, column=1)

        Button(frame, text='Go to frame 2', command=lambda: self.raise_frame(frameFiles)).grid(row=5)
        confirm = Button(frame, text="Send Messages", command=self.send).grid(row=4)
        self.raise_frame(frame)
        Label(frameFiles, text="Server IP: ").grid(row=0, stick=W)
        Label(frameFiles, text="Server Port: ").grid(row=1, stick=W)
        self.ip_input2 = Entry(frameFiles)
        self.ip_input2.grid(row=0, column=1)

        self.port_input2 = Entry(frameFiles)
        self.port_input2.grid(row=1, column=1)
        Button(frameFiles, text="BACK", fg='red',command=lambda: self.raise_frame(frame)).grid(row=5, column=2)

        Button(frameFiles, text="SEND", command=lambda: self.SendFiles(frameFiles)).grid(row=5, column=1)

        Entry(frameFiles, width=60).grid(row=5, column=0)

        self.sendtext = Entry(frameFiles, width=60)
        self.sendtext.grid(row=5, column=0)

        gettext = Text(frameFiles, height=10, width=80, wrap=WORD)
        self.gettext = gettext
        gettext.grid(row=3, columnspan=3)
        gettext.insert(END, 'Connection ongoing with server\n')
        # Receive the folders available
        # First send to the server which folder to ask for
        gettext.insert(END, "Size of folder to send: \n")
        # Send the avaiable folders
        folders = " ".join(self.getFiles(""))
        gettext.insert(END,folders)
        gettext.configure(state='disabled')

    def send(self):
        ip = self.ip_input.get()
        port = int(self.port_input.get())
        num = int(self.num_input.get())

        clientProtocolHandler.client(ip, port, num)

    def SendFiles(self, frameFiles):
        if(self.paso == 1):
            self.gettext.configure(state='normal')
            text = self.sendtext.get()
            self.size = text
            self.gettext.insert(END, '%s\n' % text)
            self.sendtext.delete(0, END)
            self.gettext.configure(state='disabled')
            response = self.getFiles(text)
            self.gettext.configure(state='normal')
            self.gettext.insert(END, '%s\n' % response)
            self.gettext.insert(END, 'File to send to server? (From the list): \n')
        if(self.paso == 2):
            ip = self.ip_input2.get()
            port = int(self.port_input2.get())
            size = self.size
            filename = self.sendtext.get()
            self.gettext.configure(state='disabled')
            self.sendtext.delete(0, END)
            self.gettext.configure(state='disabled')
            clientProtocolHandlerFiles.client(ip, port,size,filename, frameFiles)
        self.paso = self.paso + 1

    def raise_frame(self, frame):
        frame.tkraise()

root = Tk()
root.title(string="Client")

app = App(root)

root.mainloop()
