from getOsu.Osu_clean import *
from getOsu.Osu_paqu import *
import tkinter as tk
from tkinter import messagebox
showindow=tk.Tk()
showindow.title('OSU rank search！')
showindow.geometry('390x600')
#提示输入框
l=tk.Label(showindow,text='输入您的ID:',bg='white',
           font=('Arial',14),width=16,height=1).place(x=10,y=25,anchor='nw')
e=tk.Entry(showindow,width=25,show=None)#
e.place(x=10,y=70,anchor='nw')
canvas=tk.Canvas(showindow,bg='pink',height=155,width=155)
image_file=tk.PhotoImage(file='AA.png')
image=canvas.create_image(15,15,anchor='nw',image=image_file)
canvas.place(x=380,y=10,anchor='ne')

var=tk.StringVar()
def getval():
    var=e.get()#ID
    SSS=Get_OsuHtml(var)#HTML
    s_final=Get_OSUlist(SSS)#最终信息
    #用于显示
    l = tk.Label(showindow, text=s_final, bg='white', font=('Arial', 14), width=32, height=15).place(x=14, y=175)
b=tk.Button(showindow,text='点击开始查询',width=24,height=1,command=getval).place(x=11,y=115)


showindow.mainloop()