# coding: utf-8

# Tkinter 라이브러리 임포트
import tkinter as tk

# Tk 객체 인스턴스 생성
root = tk.Tk()

# 레이블 생성
label = tk.Label(root, text='Hello world')

# 레이블 배치
label.pack()

# root 표시
root.mainloop()