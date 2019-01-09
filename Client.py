from tkinter import *
import socket
import time

def Server():

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            for i in FileContent:
                time.sleep(1)
                text.insert(END, 'send to server {}\n'.format(i))
                s.sendall(i.encode())
                data = s.recv(1024)
                text.insert(END, 'Received ftom server {}\n'.format(data.decode()))
                text.see(END)
    except:
        text.insert(END, "please connect to the server\n")
        text.see(END)
        print("please connect to the server")



HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

mainWindow=Tk()
mainWindow.title("Water Station")
scrollbar = Scrollbar(mainWindow)
scrollbar.pack(side=RIGHT, fill=Y)
text=Text(mainWindow)
text.config(yscrollcommand=scrollbar.set)
text.pack()
scrollbar.config(command=text.yview)
StartButton=Button(mainWindow,text="start",command=Server)
StartButton.pack()

file=""
try:
    text.insert(END,"try to open file status.txt\n")
    file=open("status.txt","r")
    text.insert(END, "files opened\n")
    FileContent=file.read()
    text.insert(END,FileContent)
    FileContent=FileContent.split("\n")
    text.insert(END, "\ncontent file saved and closed\n")
except:
    text.insert(END, "file status.txt not exist\n")
finally:
    if not file.closed:
        file.close()
text.insert(END, "Press Start and Please wait for server answer\n")
mainWindow.mainloop()