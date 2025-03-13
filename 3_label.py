from tkinter import *
root = Tk()
root.title("Nado GUI")

Label1 = Label(root, text="안녕하세요")
Label1.pack()

photo = PhotoImage(file="python_gui/peace.png")
Label2 = Label(root, image=photo)
Label2.pack()

def change():
    Label1.config(text="또 만나요")

    global photo2 # 전역변수로 선언해야함 안그럼 지움
    photo2 = PhotoImage(file="python_gui/no.png")
    Label2.config(image=photo2)

btn = Button(root, text="클릭", command=change)
btn.pack()



root.mainloop()
