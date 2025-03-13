from tkinter import *
root = Tk()
root.title("Nado GUI")

btn1 = Button(root, text="버튼1")
btn1.pack() # pack() 함수를 호출해야만 화면에 나타남


btn2 = Button(root, padx=5, pady=10, text="버튼2") # padx, pady: 버튼 내 여백 x- 가로, y- 세로
btn2.pack()


btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

btn4 = Button(root, width=10, height=3, text="버튼4") # width, height: 버튼 크기 width- 가로, height- 세로
btn4.pack()

btn5 = Button(root, fg="blue", bg="red", text="버튼5") # fg: 글자색, bg: 배경색
btn5.pack()

photo = PhotoImage(file="ausomr/peace.png")
btn6 = Button(root, image=photo)
btn6.pack()

def btncmd():
    print("버튼이 클릭되었어요")

btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()

root.mainloop()
