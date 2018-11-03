
#!/usr/bin/python
# -*- coding: utf-8 -*-

#<--Import lib
import os

from ezprint import *
from tkinter import *
from main import *
from tkinter import filedialog as fd
	# f = open(file_name)
	# s = f.read()
	# f.close()

def insertText(radio3, v, text_hash):
	file_name = fd.askopenfilename()
	list_name = file_name.split('/')
	last_element = len(list_name) - 1
	if file_name == '':
		radio3.config(text = 'Your dictionary')
	else:
		fs = os.path.getsize(file_name)
		if fs == 0:
			radio3.config(text = 'Your dictionary')
		else:
			radio3.config(text = list_name[last_element])
			check_args(v, text_hash)


def check_args(v, text_hash):
	if v.get() == 1:
		print('1')
	elif v.get() == 2:
		print('2')
	elif v.get() == 3:
		print('3')


def crack_hash(v, text_hash):
	pass