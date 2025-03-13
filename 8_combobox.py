import tkinter.ttk as ttk
from tkinter import *
root = Tk()
root.title("Nado GUI")  
root.geometry("640x480") # 가로 * 세로



combobox = ttk.Combobox(root, height=6, values="카드결제일" )
combobox.pack()
combobox.set("카드 결제일")

values = [str(i) + "일" for i in range(1,32)]
readonly_combobox = ttk.Combobox(root, height=6, values=values, state = "readonly" )
readonly_combobox.current(0)
readonly_combobox.pack()



def btncmd():
    print(combobox.get())
    print(readonly_combobox.get())


btn = Button(root, text="선택택", width=30, command=btncmd)
btn.pack()

root.mainloop() 
# 창이 실행된다고 생각
