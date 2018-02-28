#!/usr/bin/python
import Tkinter as tk
window = tk.Tk();

def changeString():
	stringToCopy = entry.get()
	stringToCopy = stringToCopy[::-1] #字符串反转
	entry.delete(0,tk.END) #把文本框从头到尾删掉
	entry.insert(0,stringToCopy)

entry = tk.Entry(window)
button = tk.Button(window, text = "Change",command = changeString)
entry.pack()
button.pack()
window.mainloop()