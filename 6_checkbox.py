from tkinter import *
root = Tk()
root.title("Nado GUI")  
root.geometry("640x480") # 가로 * 세로

chkvar1 = IntVar() # chkvar에 int형으로 값을 저장
chkbox1 = Checkbutton(root, text="24시간동안 보지 않기", variable=chkvar1)
#chkvar.select() # 선택택/
#chkvar.deselect() # 선택 해제
chkbox1.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="일주일동안 보지 않기", variable=chkvar2)
chkbox2.pack()


# 위에서 선택 처리를 하였으나 나중에 나온 선택해제 처리로 gui상 선택이 해제 되어있음


def btncmd():
    print(chkvar1.get()) # 0: 해제, 1: 선택
    print(chkvar2.get()) # 0: 해제, 1: 선택

btn = Button(root, text="클릭", width=30, command=btncmd)
btn.pack()

root.mainloop() 
# 창이 실행된다고 생각
