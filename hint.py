from tkinter import*
tk = Tk()
tk.title('hint')
tk.geometry('600x150')
canvas = Canvas(tk,width=600,height=150)
canvas.pack(side=TOP)
canvas.create_text(300, 75, text='找到繽紛的壺，即可結束這場災難',fill = '#000000', font=('Arial', 20))
tk.mainloop()