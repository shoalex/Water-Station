from tkinter import *
from db import dbconnect
import threading
import queue


mainWindow=Tk()
button=Button(mainWindow,text="test")
button.grid(row=0,column=0)
txt=Text(mainWindow, height = 1, width = 10)
txt.grid(row=1,column=0)
button1=Button(mainWindow,text="test")
button1.grid(row=2,column=0)

button1=Button(mainWindow,text="test")
button1.grid(row=3,column=1)
#button1.pack()
#button.pack()
mainWindow.mainloop()


"""
file=open("status.txt","r")
for line in file:
    print(line)
file.close()


db=dbconnect("data.db")
t=threading.Thread(target=db.connect)
t.start()
t.join()

t=threading.Thread(target=db.insert(2,0,1))
t.start()
t.join()


myqueue=queue.Queue()
t=threading.Thread(target=db.select,args=(2,myqueue))
t.start()
t.join()
if not myqueue.empty():
    print(myqueue.get())
else:
    print("empty")
myqueue.queue.clear()

"""