from tkinter import*
from turtle import down
#python third.py
tk = Tk()
tk.title('sent')
tk.geometry('1920x1080')
def wa3py():
    tk.destroy()
    import wa3
    wa3
# a2 = Label(tk,text="使用語言: Python",font=('Arial', 12))
# a2.place(x=60,y=60)
# a=Label(tk,text="送出程式",font=('Arial', 12))
# a.place(x=60,y=20)
photo5 = PhotoImage(file='pange(5).gif')
photoL5 = Label(tk,image = photo5,bg = '#468bcc')
photoL5.place(x = 0 , y = 0)
sent = Canvas(tk,width=580,height=420,background="#ffffff")#設置畫布
sent.place(x = 480 ,y = 100) #設置畫布
sent.create_rectangle(580,0,0,420,fill='#ffffff',width = 0)
sent.create_text(60,30,text="程式碼",font=('Arial', 20))
sent.create_line(10,50,570,50, fill='#808080') #前面是左邊的(x,y)，後面是右邊(x,y)
# sent.create_text(45,20,text="送出程式",font=('Arial', 12))
# myentry1 = Entry(tk)
# myentry1.place(x = 100 ,y = 200,width=450,height=200)
sent.create_text(205,80,text="#Created your code",font=('Arial', 12))
sent.create_text(245,100,text="from question1 import answer1",font=('Arial', 12))
sent.create_text(245,120,text="from question2 import answer2",font=('Arial', 12))
sent.create_text(245,140,text="from question3 import answer3",font=('Arial', 12))
sent.create_text(270,230,text="print( \"                                                 \" )",font=('Arial', 12))
en = Entry()
en.place(x=685,y=322)
sent1 = Button(tk,text = '送出',width=7,height=2,command= wa3py)
sent1.place(x= 970,y=462,anchor='nw')
tk.mainloop()