# coding: utf-8

#Tkinter 라이브러리 임포트
import tkinter as tk

root = tk.Tk()

def func():
    label.config(text = 'Pushed')

def func_event():
    label.config(text = 'Push Button')

label = tk.Label(root, text='Push Button')
label.pack()

button = tk.Button(root, text = 'Push!', command = func)
button.pack()

button.bind('<Leave>', func_event)

root.mainloop()