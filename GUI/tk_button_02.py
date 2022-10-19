import tkinter as tk

# Tk 객체 인스턴스 생성
root = tk.Tk()

def func():
    label.config(text = 'Pushed!')

label = tk.Label(root, text='Push Button') #라벨 생성
label.pack() #라벨 배치

button = tk.Button(root, text = 'Push!', command = func) #버튼 생성
button.pack() #버튼 배치

root.mainloop() #root 표시