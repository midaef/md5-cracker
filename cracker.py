
#!/usr/bin/python
# -*- coding: utf-8 -*-

#<--Import lib
import hashlib
import sys
import os

from ezprint import *
from tkinter import *
from main import *
from tkinter import filedialog as fd
		
time = None


def crack_hash(v, text_hash, label1, b2, file_name = ''):
	hash_text = text_hash.get()
	hash_text = hash_text.lstrip().rstrip()
	if hash_text != '':
		b2.config(state = DISABLED)
		if v.get() == 1:
			start_frame = threading.Thread(target= lambda : check_hash(text_hash, label1, b2, file_name = 'numbers.txt'))
			start_frame.start()
		elif v.get() == 2:
			start_frame = threading.Thread(target= lambda : check_hash(text_hash, label1, b2, file_name = 'rockyou.txt'))
			start_frame.start()
		elif v.get() == 3:
			start_frame = threading.Thread(target= lambda : check_hash(text_hash, label1, b2, file_name = file_name))
			start_frame.start()
	else:
		label1.config(text='Input password!')


def check_hash(text_hash, label1, b2, file_name = ''):
	f = open(file_name, 'r')
	haw = hashlib.md5()
	our_hash = text_hash.get()
	label1.config(text='Your password:')
	for i in f:
		password = i.lstrip().rstrip()
		haw = str(hashlib.md5(password.encode("utf-8")).hexdigest())
		text_hash.delete(0, END)
		text_hash.insert(0, password)
		if our_hash == haw:
			b2.config(state = NORMAL)
			break
	else:
		text_hash.delete(0, END)
		label1.config(text='Password not found!')
		b2.config(state = NORMAL)
	f.close()