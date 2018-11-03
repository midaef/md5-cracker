
#!/usr/bin/python
# -*- coding: utf-8 -*-

#<--Import lib
from ezprint import *
from tkinter import *
from cracker import *
from help.authors import *
from tkinter import filedialog as fd

v = None
label2 = None
firstFrame = None


def insertText():
	global label2

	file_name = fd.askopenfilename()
	list_name = file_name.split('/') 
	f = open(file_name)
	s = f.read()
	f.close()
	last_element = len(list_name) - 1
	label2.config(text='Your dictionary: ' + list_name[last_element])


def main():
	global label2
	global firstFrame

	#<--Settings for firstFrame
	firstFrame = Tk()

	firstFrame.title('MD5-CRACKER')

	firstFrame.resizable(0, 0)

	firstFrame.iconbitmap('docs/favicon.ico')

	#<--Elements
	label1 = Label(firstFrame, text = 'Input hash: ', fg='black')

	text_hash = Entry(firstFrame, width = 15)

	radio1 = Radiobutton(firstFrame, text = 'Number dictionary', variable=v, value=1)
	radio2 = Radiobutton(firstFrame, text = 'Mix dictionary', variable=v, value=2)

	label2 = Label(firstFrame, text = 'Your dictionary: ', fg='black')

	b1 = Button(firstFrame, text= 'Open file ', command = insertText)

	b2 = Button(firstFrame, text= 'Crack hash', command = crack_hash)

	#<--Configs
	label1.config(font = ('Arial', 15, 'bold'))

	text_hash.config(font = ('Arial', 15, 'bold'))

	radio1.config(fg = '#AA1D36')
	radio2.config(fg = '#AA1D36')

	label2.config(font = ('Arial', 15, 'bold'))

	b1.config(font = ('Arial', 10, 'bold'))
	b2.config(font = ('Arial', 10, 'bold'))

	#<--Grids
	label1.grid(column = 1, row = 0)

	text_hash.grid(column = 1, row = 1)

	radio1.grid(column = 1, row = 2)
	radio2.grid(column = 1, row = 3)

	label2.grid(column = 1, row = 4)

	b1.grid(column = 1, row = 5, sticky=W)
	b2.grid(column = 1, row = 5, sticky=E)

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