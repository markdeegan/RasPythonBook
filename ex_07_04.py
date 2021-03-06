#!/usr/bin/python
#ex_07_04
#temperature converter

from tkinter import *
from converters import *


class App:
  def __init__(self, master):
    # create a ScaleAndOffsetConverter
    self.t_conv=ScaleAndOffsetConverter('C','F',1.8,32)

    # create the Frame
    frame = Frame(master)
    frame.pack()

    #create label 1, celsius
    label1 = Label(frame, text='deg C')
    label1.grid(row=0, column=0)

    # define the celsius cariable
    self.c_var = DoubleVar()

    #create the entry 1 field to accept temperature
    entry1 = Entry(frame, textvariable=self.c_var)
    entry1.grid(row=1, column=1)

    #create label 2, fahrenheit
    label2 = Label(frame, text='deg F')
    label2.grid(row=0, column=1)


    #define the fahrenheit variable
    self.result_var = DoubleVar()

    # create the result label
    label3 = Label(frame, textvariable=self.result_var)
    label3.grid(row=1, column=1)

    # create the convert button1
    button1 = Button(frame, text='Convert', command=self.convert)
    button1.grid(row=2, columnspan=2)

  def convert(self):
      c = self.c_var.get()
      self.result_var.set(self.t_conv.convert(c))
      print('now implemented')
      print(self.result_var.get())
      print(self.t_conv)

root = Tk()
root.wm_title('Temp Converter')
root.geometry('800x480')
app = App(root)
root = mainloop()
