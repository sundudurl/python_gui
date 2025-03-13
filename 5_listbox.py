from tkinter import *
root = Tk()
root.title("Nado GUI")  
root.geometry("640x480") # 가로 * 세로

listbox = Listbox(root, selectmode="extended", height=0) 
#extended - 여러개 선택, single - 하나만 선택
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()

def btncmd():
    # listbox.delete(END) # 맨 뒤에 항목을 삭제

    # 갯수 확인
    print("리스트 내", listbox.size(), "보유")

    # 항목 확인 (시작 idx, 끝 idx)
    print("1-3번째 항목목: ", listbox.get(0, 2)) 

    # 선택된 항목 확인 (위치로 반환 (ex) (1, 2, 3))
    print("선택 항목" , listbox.curselection())   

btn = Button(root, text="클릭", width=30, command=btncmd)
btn.pack()

root.mainloop() 
# 창이 실행된다고 생각
