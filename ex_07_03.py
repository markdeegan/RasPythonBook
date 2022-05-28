#!/usr/bin/python
#ex_07_03

from tkinter import *

class App:
  def __init__(self, master):
    #define the celsius cariable
    self.c_var = DoubleVar()

    #define the fahrenheit cariable
    self.result_var = DoubleVar()

    # create the Frame
    frame = Frame(master)
    frame.pack()

    #create label 1, celsius
    label1 = Label(frame, text='deg C')
    label1.grid(row=0, column=0)

    #create label 2, fahrenheit
    label2 = Label(frame, text='deg F')
    label1.grid(row=1, column=1)


    #create the entry 1 field to accept temperature
    entry1 = Entry(frame, textvariable=self.c_var)
    entry1.grid(row=1, column=0)

    # create button1 to convert
    button1 = Button(frame, text='Convert', command=self.convert)
    button1.grid(row=1)

  def convert(self):
      print('not yet implemented')

root = Tk()
root.wm_title('Temp Converter')
app = App(root)
root = mainloop()