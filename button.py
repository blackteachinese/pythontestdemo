#!/usr/bin/python
import Tkinter as tk
window = tk.Tk()
count = 0
def buttonClick():
	print "Beep!"
	global count
	count += 1
	button.config(text=str(count))

button = tk.Button(window,text = "Click me!", command=buttonClick)
button.pack()
window.mainloop()
print "end!"
