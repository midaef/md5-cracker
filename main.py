
#!/usr/bin/python
# -*- coding: utf-8 -*-

#<--Import lib
import threading
import time
import os

from ezprint import *
from tkinter import *
from cracker import *
from help.authors import *
from tkinter import filedialog as fd

v = None
firstFrame = None
start_frame = None


def main():
	global v
	global firstFrame

	#<--Settings for firstFrame
	firstFrame = Tk()

	firstFrame.title('MD5-CRACKER')

	firstFrame.resizable(0, 0)

	firstFrame.iconbitmap('docs/favicon.ico')

	v = IntVar()
	
	#<--Elements
	label1 = Label(firstFrame, text = 'Input hash: ', fg='black')

	text_hash = Entry(firstFrame, width = 15)

	radio1 = Radiobutton(firstFrame, text = 'Number dictionary', variable=v, value=1)
	radio2 = Radiobutton(firstFrame, text = 'Mix dictionary', variable=v, value=2)
	radio3 = Radiobutton(firstFrame, text = 'Your dictionary', variable=v, value=3, command = lambda : insertText(radio3, v, text_hash))

	b2 = Button(firstFrame, text= 'Crack hash', command = lambda : check_args(v, text_hash))

	#<--Configs
	label1.config(font = ('Arial', 15, 'bold'))

	text_hash.config(font = ('Arial', 15, 'bold'))

	radio1.config(fg = '#AA1D36')
	radio2.config(fg = '#AA1D36')
	radio3.config(fg = '#AA1D36')

	b2.config(font = ('Arial', 10, 'bold'))

	#<--Grids
	label1.grid(column = 1, row = 0)

	text_hash.grid(column = 1, row = 1)

	radio1.grid(column = 1, row = 2)
	radio2.grid(column = 1, row = 3)
	radio3.grid(column = 1, row = 4)

	b2.grid(column = 1, row = 6)

	radio1.select()

	#<--Panel
	main_menu = Menu(firstFrame)
	firstFrame.config(menu = main_menu)
	info_menu = Menu(main_menu)
	main_menu.add_cascade(label="Info", menu = info_menu)
	info_menu.add_command(label="Authors", command = authors)

	#<--Start
	firstFrame.mainloop()


if __name__ == '__main__':
	main()