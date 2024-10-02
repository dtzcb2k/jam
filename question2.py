from tkinter import*
tk = Tk()
tk.title('window')
tk.geometry('1920x1080')
def answer2py():
    tk.destroy()
    import answer2
    answer2
canvas = Canvas(tk,width=1920,height=1080)
canvas.pack(side=TOP)
canvas.create_rectangle(1920,0,0,90,fill='#468bcc') #(右上角,左下角)
canvas.config(highlightthickness=0)
canvas.create_rectangle(120,36,20,120,fill='#808080')
canvas.create_text(70, 62, text='One',fill = '#ffffff', font=('Arial', 25))
canvas.create_text(70, 92, text='Judge',fill = '#ffffff', font=('Arial', 25))
canvas.create_text(210, 45, text='Problems',fill = '#ffffff', font=('Arial', 20))
canvas.create_text(370, 45, text='Submissions',fill = '#ffffff', font=('Arial', 20))
canvas.create_text(505, 45, text='Rank',fill = '#ffffff', font=('Arial', 20))
canvas.create_text(600, 45, text='Forum',fill = '#ffffff', font=('Arial', 20))
canvas.create_text(710, 45, text='Contest',fill = '#ffffff', font=('Arial', 20))
canvas.create_text(1300, 45, text='Login',fill = '#ffffff', font=('Arial', 20))
canvas.create_text(1410, 45, text='Register',fill = '#ffffff', font=('Arial', 20))
photo1 = PhotoImage(file='pange(1).gif')
photoL1 = Label(tk,image = photo1)
photoL1.place(x = 800 , y = 25)
photo2 = PhotoImage(file='pange(2).gif')
photoL2 = Label(tk,image = photo2,bg = '#468bcc')
photoL2.place(x = 1480 , y = 18)

canvas.create_text(770, 170, text='問題二:明天下雨機率多少?',fill = '#000000', font=('Arial', 25))

canvas.create_rectangle(610,250,290,300,fill='#D3D3D3')
canvas.create_text(350, 275, text='輸入說明',fill = '#000000', font=('Arial', 15))
canvas.create_rectangle(610,300,290,375,fill='#ffffff')
canvas.create_text(440, 332, text='輸入你認為明天下雨機率為何',fill = '#000000', font=('Arial', 15))

canvas.create_rectangle(970,250,640,300,fill='#D3D3D3')
canvas.create_text(700, 275, text='輸出說明',fill = '#000000', font=('Arial', 15))
canvas.create_rectangle(970,300,640,375,fill='#ffffff')
canvas.create_text(720, 332, text='明天下雨機率',fill = '#000000', font=('Arial', 15))

canvas.create_rectangle(610,405,290,455,fill='#D3D3D3')
canvas.create_text(350, 425, text='範例輸入',fill = '#000000', font=('Arial', 15))
canvas.create_rectangle(610,455,290,530,fill='#ffffff')
canvas.create_text(332, 487, text='70%',fill = '#000000', font=('Arial', 15))

canvas.create_rectangle(970,405,640,455,fill='#D3D3D3')
canvas.create_text(700, 425, text='範例輸出',fill = '#000000', font=('Arial', 15))
canvas.create_rectangle(970,455,640,530,fill='#ffffff')
canvas.create_text(682, 487, text='30%',fill = '#000000', font=('Arial', 15))

canvas.create_rectangle(1200,250,1000,300,fill='#D3D3D3')
canvas.create_text(1060, 275, text='測資資訊:',fill = '#000000', font=('Arial', 15))
canvas.create_rectangle(1200,300,1000,439,fill='#ffffff')
canvas.create_text(1090, 332, text='~ ~ ~ ~ ~ ~ ~ ~',fill = '#000000', font=('Arial', 15))
canvas.create_text(1090, 362, text='~ ~ ~ ~ ~ ~ ~ ~',fill = '#000000', font=('Arial', 15))
canvas.create_text(1090, 392, text='~ ~ ~ ~ ~ ~ ~ ~',fill = '#000000', font=('Arial', 15))

bt_1 = Button(tk, text='送出解答', bg='#2cba1d', fg='white', font=('Arial', 15),command = answer2py)
bt_1.place(x = 290 , y = 630)

tk.mainloop()
