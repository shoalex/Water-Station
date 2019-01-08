from tkinter import *
import socket
import threading
import time

def Server():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))

            for i in FileContent:
                time.sleep(1)
                text.insert(END, 'send to server {} {}'.format(i, "\n"))
                s.sendall(i.encode())
                data = s.recv(1024)
                text.insert(END, 'Received ftom server {} {}'.format(data.decode(), "\n"))
                # print('Received', data.decode())
    except:
        text.insert(END, "please connect to the server\n")
        print("please connect to the server")
        # exit(1)



HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

mainWindow=Tk()
mainWindow.title("Water Station")
text=Text(mainWindow)
text.pack()
StartButton=Button(mainWindow,text="start",command=Server)
StartButton.pack()


try:
    text.insert(END,"try to open file status.txt\n")
    file=open("status.txt","r")
    text.insert(END, "files opened\n")
    FileContent=file.read()

    text.insert(END,FileContent)
    FileContent=FileContent.split("\n")
    file.close()
    text.insert(END, "\ncontent file saved and closed\n")
except:
    text.insert(END, "file status.txt not exist\n")
    #exit(1)

mainWindow.mainloop()