from tkinter import *
root = Tk()
root.title("Nado GUI")  
root.geometry("640x480") # 가로 * 세로

label = Label(root, text="메뉴를 선택하세요").pack()

burger_var = IntVar()
btn_burger1 = Radiobutton(root, text="치즈케이크", value=1, variable=burger_var)
btn_burger1.select()
btn_burger2 = Radiobutton(root, text="아이스박스", value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="티라미수 케이크크", value=3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

# 위에서 선택 처리를 하였으나 나중에 나온 선택해제 처리로 gui상 선택이 해제 되어있음

label = Label(root, text="주문하실 음료를 선택해주세요")
label.pack()

drink_var = StringVar()
btn_drink1 = Radiobutton(root, text="아이스티", value=4, variable=drink_var)
btn_drink1.select()
btn_Drink2 = Radiobutton(root, text="아이스아메리카노", value=5, variable=drink_var)

btn_drink1.pack()
btn_Drink2.pack()



def btncmd():
    print(burger_var.get()) # 선택된 라디오 항목의 값(value)을 출력
    print(drink_var.get()) # 선택된 라디오 항목의 값(value)을 출력

btn = Button(root, text="주문", width=30, command=btncmd)
btn.pack()

root.mainloop() 
# 창이 실행된다고 생각
