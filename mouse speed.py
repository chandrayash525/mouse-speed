from tkinter import *
from random import *

def do_event(event):
    print("{},{}".format(event.x,event.y))

def jump(event):
    app.hello_b.place(relx=random(),rely=random())

class App:
    def __init__(self,master):
        frame = Frame(master)
        master.geometry("160x160")
        master.title("My first program!")
        master.bind("<Button-1>",do_event)
        master.bind("<Button-1>",do_event)
        frame.pack()

        self.hello_b = Button(master,text="Quit",command=sys.exit)
        self.hello_b.bind("<Enter>",jump)
        self.hello_b.pack()




root = Tk()

root = Tk()
frame = Frame(root)
frame.pack()
bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )
redbutton = Button(frame, text = 'Red', fg ='red')
redbutton.pack( side = LEFT)
greenbutton = Button(frame, text = 'Brown', fg='brown')
greenbutton.pack( side = LEFT )
bluebutton = Button(frame, text ='Blue', fg ='blue')
bluebutton.pack( side = LEFT )
blackbutton = Button(bottomframe, text ='Black', fg ='black')
blackbutton.pack( side = BOTTOM)

app = App(root)

root.mainloop()
