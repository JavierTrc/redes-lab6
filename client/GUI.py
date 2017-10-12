from tkinter import *
import clientProtocolHandler


class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

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

        confirm = Button(frame, text="Send Messages", command=self.send)
        confirm.grid(row=3, columnspan=2)

    def send(self):
        ip = self.ip_input.get()
        port = int(self.port_input.get())
        num = int(self.num_input.get())

        clientProtocolHandler.client(ip, port, num)


root = Tk()
root.title(string="Client")

app = App(root)

root.mainloop()
