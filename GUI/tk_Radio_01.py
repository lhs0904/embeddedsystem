import tkinter as tk

root = tk.Tk()
root.title('Radio Button')
root.geometry('640x640')

def func():
    selection = "You selected the option" + str(sel.get())
    label.config(text = selection)

sel = tk.IntVar() #라디오 버튼 값을 저장하는 정수형 Variable 객체 생성

R1 = tk.Radiobutton(root, text = "Option 1", variable = sel, value = 1, command = func)
R1.pack(anchor=tk.W)

R2 = tk.Radiobutton(root, text = "Option 2", variable = sel, value = 2, command=func)
R2.pack(anchor=tk.W)

label = tk.Label(root)
label.pack()

root.mainloop()