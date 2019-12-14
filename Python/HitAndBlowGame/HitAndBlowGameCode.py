# coding: utf-8
import tkinter as tk
import tkinter.messagebox as tmsg
import random
import re

# 확인버튼을 누르거나 Enter키를 눌렀을 때의 처리
def ButtonClick(event=None):
    # entry의 문자열을 가져옴
    num = editbox1.get()

    # 네자리 숫자인지 판별함
    isok = False
    if len(num) != 4:
        tmsg.showerror("오류", "네 자릿수의 숫자인지를 판정한다.")
    else:
        if not re.match(r"^\d\d\d\d$", num):
            tmsg.showerror("오류", "네 자릿수의 숫자인지를 판정한다.")
        else:
            isok = True

    # 히트와 블로를 판정함
    if isok:
        hit = 0
        blow = 0
        for i in range(4):
            for j in range(4):
                if answer[i] == int(num[i]):
                    hit = hit + 1
                    break
                elif answer[i] == int(num[j]):
                    blow = blow + 1
                    break
                
        # 맞췄을 경우
        if hit == 4:
            tmsg.showinfo("정답", "축하합니다. 맞췄습니다.")
            root.destroy()
            
        # 맞추지 못했을 경우
        else:
            historybox.insert(tk.END, num + "/ H:" + str(hit) + " B:" + str(blow) + "\n")
            editbox1.delete(0, 4)


# 메인 프로그램
# 랜덤 수 생성
answer = [random.randint(0, 9),
          random.randint(0, 9),
          random.randint(0, 9),
          random.randint(0, 9)]
# print(answer)

# 윈도우
root = tk.Tk()
root.geometry("600x400")
root.title("히트 & 블로 게임")

# 이력 표시 텍스트 박스
historybox = tk.Text(root, font=("나눔스퀘어", 11))
historybox.place(x = 400, y = 0, width = 200, height = 400)

# 라벨
label1 = tk.Label(root, text="숫자를 입력하세요.", font=("나눔스퀘어", 11))
label1.place(x = 20, y = 20)

# 입력
editbox1 = tk.Entry(width = 4, font=("나눔스퀘어", 20))
editbox1.place(x = 100, y = 50)
editbox1.bind('<Return>', ButtonClick) 

# 버튼
button1 = tk.Button(root, text = "확인", font = ("나눔스퀘어", 12), command = ButtonClick)
button1.place(x = 180, y = 50)

root.mainloop()
