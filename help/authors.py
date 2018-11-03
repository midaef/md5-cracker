
#!/usr/bin/python
# -*- coding: utf-8 -*-

#<--Import lib
from ezprint import *
from tkinter import *


def authors():
	#<--Settings for secondFrame
	fourthFrame = Tk()

	fourthFrame.title('Info')

	fourthFrame.resizable(0, 0)
	
	fourthFrame.iconbitmap('docs/favicon.ico')

	#<--Elements
	label1 = Label(fourthFrame, text = 'Authors:', fg='black')
	label2 = Label(fourthFrame, text = 'Midaef: midaef.ru', fg='black')

	#<--Configs
	label1.config(font = ('Arial', 15, 'bold'))
	label2.config(font = ('Arial', 15, 'bold'))

	#<--Grids
	label1.grid(column = 0, row = 0)
	label2.grid(column = 0, row = 1)

	#<--Start
	fourthFrame.mainloop()