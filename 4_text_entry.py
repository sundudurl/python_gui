from tkinter import *
root = Tk()
root.title("Nado GUI")  
root.geometry("640x480") # 가로 * 세로

txt= Text(root, width=30)
txt.pack()
txt.insert(END, "ID")

e=Entry(root, width=30)
e.pack()
e.insert(0, "PASSWORD")

def btncmd():
    print(txt.get("1.0", END)) # 1: 첫번째 라인, 0: 0번째 column 위치
    print(e.get())

    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="클릭", width=30, command=btncmd)
btn.pack()

root.mainloop() # 창이 실행된다고 생각
