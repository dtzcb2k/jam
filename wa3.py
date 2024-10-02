from distutils.command.config import config
from tkinter import*
import random
tk = Tk()
tk.title('window')
tk.geometry('1920x1080')
canvas = Canvas(tk,width=1920,height=1080)
canvas.pack(side=TOP)
x1 = int()
y1 = int()
def null():
    pass
def mathfuntion1():
    canvas.create_text(120, 180, text='哈哈哈WA',fill='#000000', font=('Arial', 18))
    bt_next['text'] = '下二步'
    bt_next.config(command=mathfuntion2)
def mathfuntion2():
    canvas.create_rectangle(560, 160, 0, 200, fill='#ffffff',width=0)
    canvas.create_text(150, 180, text='繼續努力阿',fill='#000000', font=('Arial', 18))
    bt_next['text'] = '下三步'
    bt_next.config(command=mathfuntion3)
def mathfuntion3():
    canvas.create_rectangle(560, 160, 0, 200, fill='#ffffff',width=0)
    canvas.create_text(160, 180, text='學那麼久還WA',fill='#000000', font=('Arial', 18))
    bt_next['text'] = '返回'
    bt_next.config(command=mathfuntion4)
def mathfuntion4():
    canvas.create_rectangle(560, 160, 0, 200, fill='#ffffff',width=0)
    canvas.create_text(200, 180, text='你不夠格阿，不夠格',fill='#000000', font=('Arial', 18))
    bt_next['text'] = '下二步'
    bt_next.config(command=mathfuntion5)
def mathfuntion5():
    canvas.create_rectangle(560, 160, 0, 200, fill='#ffffff',width=0)
    canvas.create_text(200, 180, text='你一直Try也不會過啦',fill='#000000', font=('Arial', 18))
    bt_next['text'] = '返回'
    bt_next.config(command=mathfuntion6)
def mathfuntion6():
    canvas.create_rectangle(560, 160, 0, 200, fill='#ffffff',width=0)
    canvas.create_text(200, 180, text='工程師之恥',fill='#000000', font=('Arial', 18))
    bt_next['text'] = '下一步'
    bt_next.config(command=mathfuntion7)
def mathfuntion7():
    bt_X.place(x=966, y=362)
    bt_X.config(command = mathfuntion8)
    bt_next.config(command = null)
def mathfuntion8():
    bt_X.place(x=1100, y=200)
    bt_X.config(command = mathfuntion9)
def mathfuntion9():
    bt_X.place(x=300, y=200)
    bt_X.config(command = mathfuntion10)
def mathfuntion10():
    bt_X.place(x=300, y=700)
    bt_X.config(command = mathfuntion11)
def mathfuntion11():
    canvas.create_rectangle(560, 160, 0, 200, fill='#ffffff',width=0)
    canvas.create_rectangle(560, 75, 0, 155, fill='#ffffff',width=0)
    canvas.create_text(150, 110, text='你以為下個會在右下嗎',fill='#000000', font=('Arial', 18))
    bt_next['text'] = '確認'
    bt_next.config(command = mathfuntion12)
    bt_X.config(command = null)
def mathfuntion12():
    canvas.create_rectangle(560, 75, 0, 155, fill='#ffffff',width=0)
    canvas.create_text(150, 110, text='是不是覺得很煩阿',fill='#000000', font=('Arial', 18))
    bt_next.config(command = mathfuntion13)
def mathfuntion13():
    canvas.create_rectangle(560, 75, 0, 155, fill='#ffffff',width=0)
    canvas.create_text(150, 110, text='請等待十秒後按關閉',fill='#000000', font=('Arial', 18))
    bt_next['text'] = '關閉'
    bt_next.config(command = mathfuntion14)
def mathfuntion14():
    canvas.create_rectangle(560, 75, 0, 155, fill='#ffffff',width=0)
    canvas.create_text(60, 110, text='TLE',fill='#000000', font=('Arial', 18))
    canvas.create_rectangle(560, 160, 0, 200, fill='#ffffff',width=0)
    canvas.create_text(130, 180, text='超過時間限制:3秒',fill='#000000', font=('Arial', 18))
    bt_next['text'] = '關閉'
    bt_next.config(command = mathfuntion15)
def mathfuntion15():
    canvas.create_rectangle(560, 0, 0, 235, fill='#ffffff',width=0)  # 白框
    canvas.create_text(250, 40, text='PS D:\school software\workspace\jam>', fill='#000000', font=('Arial', 18))
    canvas.create_text(250, 80, text='PS D:\school software\workspace\jam>', fill='#000000', font=('Arial', 18))
    canvas.create_text(250, 120, text='PS D:\school software\workspace\jam>', fill='#000000', font=('Arial', 18))
    canvas.create_text(230, 200, text= '[erro]    unexcept" :( " on your face ', fill='#FF0000', font=('Arial', 18))
    bt_next.config(command = mathfuntion16)
def mathfuntion16():
    x = random.randint(0,1200)
    y = random.randint(0,800)
    global i
    i = i + 1
    text1 = Label(text = 'error',fg= "#FF0000",font=('Arial', 50))
    if ((x <= 700 or x >= 1000) or (y <= 300 or y >= 650)):
        text1.place(x = x,y = y)
    if (i >= 10):
        bt_y.place(x = 1480,y = 750)
    if (i == 20):
        import hint
        hint
def mathfuntion17():
    tk.destroy()
    import end
    end
photo5 = PhotoImage(file='pange(5).gif')
photoL5 = Label(tk,image = photo5,bg = '#468bcc')
photoL5.place(x = 0 , y = 0)
canvas = Canvas(tk,width=560,height=235)
canvas.place(x = 440 , y = 360)
canvas.create_rectangle(560, 75, 0, 235, fill='#ffffff',width=0)  # 白框
canvas.create_rectangle(560, 0, 0, 75, fill='#468bcc',width = 2,outline = '#468bcc')  # 藍框
canvas.create_text(60, 40, text='錯誤', fill='#ffffff',font=('Arial', 25))  # 錯誤
# canvas.create_rectangle(1200, 450, 720, 530, fill='#ffffff')  # wa框
canvas.create_line(20, 155, 540, 155, fill='#a9a9a9')
canvas.create_text(100, 110, text='WA : Line 1',fill='#000000', font=('Arial', 18))  # WA
bt_next = Button(tk, text='下一步', bg='#4169e1',fg='#ffffff', font=('Arial', 17),command = mathfuntion1)  # 下一步按鈕
bt_next.place(x=890, y=540)
bt_X = Button(tk, text='X',bg = '#468bcc',fg='#ffffff', font=('Arial', 17),command=mathfuntion7)  # 下一步按鈕
i = 0
img = PhotoImage(file = 'pange(6).gif')
bt_y = Button(tk,text = 'pot',command = mathfuntion17)
bt_y.config(image = img)
tk.mainloop()