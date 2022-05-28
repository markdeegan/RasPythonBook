#!/usr/bin/python
#ex_07_02

from tkinter import *

class App:
  def __init__(self, master):
    frame = Frame(master)
    frame.pack()
    label1 = Label(frame, text='deg C')
    label1.grid(row=0, column=0)
    
    button1 = Button(frame, text='Convert', command=self.convert)
    button1.grid(row=1)
    
    def convert(self):
      print('not yet implemented')
      
root = Tk()
root.wm_title('Temp Converter')
app = App(root)
root = mainloop()
