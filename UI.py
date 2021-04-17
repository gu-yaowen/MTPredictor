from tkinter import *
import tkinter
import tkinter.messagebox
import easygui
import pandas as pd
import os
from predict import Predict


def run2():
    list_item = []
    if (CheckVar1.get() == 0 and CheckVar2.get == 0 and CheckVar3.get() == 0 and CheckVar4.get == 0 \
            and CheckVar5.get() == 0 and CheckVar6.get == 0 and CheckVar7.get() == 0 \
            and CheckVar8.get() == 0 and CheckVar9.get == 0):
        s = '请选择待预测的药物属性'
    else:
        s1 = 'P450 1A2' if CheckVar1.get() == 1 else ''
        s2 = 'P450 2C9' if CheckVar2.get() == 1 else ''
        s3 = 'P450 2C19' if CheckVar3.get() == 1 else ''
        s4 = 'P450 2D6' if CheckVar4.get() == 1 else ''
        s5 = 'P450 3A4' if CheckVar5.get() == 1 else ''
        s6 = 'Ames' if CheckVar6.get() == 1 else ''
        s7 = 'hERG' if CheckVar7.get() == 1 else ''
        s8 = 'LO2' if CheckVar8.get() == 1 else ''
        s9 = 'HEK293' if CheckVar9.get() == 1 else ''

        s = s1 + '|' + s2 + '|' + s3 + '|' + s4 + '|' + s5 + '|' + s6 + '|' + s7 + '|' + s8 + '|' + s9
        s = s.split('|')

        list_item = [a for a in s if a != '']
    lb3.config(text=s)
    txt_input.delete(1.0, END)
    file_dir = inpl2.get(1.0, END).strip('\n')
    if os.path.exists(file_dir.strip('\n')):
        file = pd.read_csv(file_dir)
    else:
        easygui.msgbox('请输入正确的待分析物质文件路径!')
        return
    n = file.head(5)['SMILES'].values.tolist()
    txt_input.insert(END, n)
    txt_output.delete(1.0, END)
    save_dir = inpl4.get(1.0, END).strip('\n')
    if os.path.exists(save_dir):
        tkinter.messagebox.showerror(title='错误', message='该文件已存在')
    else:
        try:
            output = Predict(file_dir, save_dir, list_item)
            txt_output.insert(END, output.head(5).values.tolist())
            inpl4.delete(1.0, END)
        except:
            tkinter.messagebox.showerror(title='错误', message=str(list_item) + file_dir + save_dir)


####################################################################################
win = Tk()
win.title('MTPredictor:药物代谢及毒性预测工具')
win.geometry('1000x800')

bg_color = "#2f6477"

frame = Frame(win, relief=RAISED, borderwidth=2, width=800, height=400, bg=bg_color)
frame.pack(side=TOP, fill=BOTH, ipadx=5, ipady=5, expand=1)

lb1 = Label(win, text='请选择待预测的药物属性', bg=bg_color)
lb1.place(x=70, y=100, anchor=W, width=150, height=30)

CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()
CheckVar4 = IntVar()
CheckVar5 = IntVar()
CheckVar6 = IntVar()
CheckVar7 = IntVar()
CheckVar8 = IntVar()
CheckVar9 = IntVar()

ch1 = Checkbutton(win, text='P450 1A2', variable=CheckVar1, onvalue=1, offvalue=0)
ch2 = Checkbutton(win, text='P450 2C9', variable=CheckVar2, onvalue=1, offvalue=0)
ch3 = Checkbutton(win, text='P450 2C19', variable=CheckVar3, onvalue=1, offvalue=0)
ch4 = Checkbutton(win, text='P450 2D6', variable=CheckVar4, onvalue=1, offvalue=0)
ch5 = Checkbutton(win, text='P450 3A4', variable=CheckVar5, onvalue=1, offvalue=0)
ch6 = Checkbutton(win, text='Ames', variable=CheckVar6, onvalue=1, offvalue=0)
ch7 = Checkbutton(win, text='hERG', variable=CheckVar7, onvalue=1, offvalue=0)
ch8 = Checkbutton(win, text='LO2', variable=CheckVar8, onvalue=1, offvalue=0)
ch9 = Checkbutton(win, text='HEK293', variable=CheckVar9, onvalue=1, offvalue=0)

ch1.place(x=50, y=150, anchor=W, width=50, height=10)
ch2.place(x=50, y=200, anchor=W, width=50, height=10)
ch3.place(x=50, y=250, anchor=W, width=50, height=10)
ch4.place(x=50, y=300, anchor=W, width=50, height=10)
ch5.place(x=50, y=350, anchor=W, width=50, height=10)
ch6.place(x=200, y=150, anchor=W, width=50, height=10)
ch7.place(x=200, y=200, anchor=W, width=50, height=10)
ch8.place(x=200, y=250, anchor=W, width=50, height=10)
ch9.place(x=200, y=300, anchor=W, width=50, height=10)

lb3 = Label(win, text='')

lb3.place(x=100, y=450, anchor=W, width=100, height=40)

###############################################################################
lb2 = Label(win, text='输入路径')
lb2.place(x=500, y=100, anchor=W, width=100, height=20)
inpl2 = Text(win)
inpl2.place(x=600, y=100, anchor=W, width=200, height=20)

#############控件##############################################################
button2 = Button(win, text="执行", font=('宋体', 20), fg='red', command=run2)
button2.place(x=300, y=200, anchor=W, width=100, height=40)

button_input = Button(win, text="分子", font=('宋体', 20), fg='red')
button_input.place(x=500, y=250, width=100, height=40)

button_output = Button(win, text="结局", font=('宋体', 20), fg='red')
button_output.place(x=750, y=250, width=100, height=40)

lb4 = Label(win, text='保存路径', font=('宋体', 10))
lb4.place(x=500, y=150, anchor=W, width=100, height=20)
inpl4 = Text(win)
inpl4.place(x=600, y=150, anchor=W, width=200, height=20)

txt_input = Text(win)
txt_input.place(x=500, y=300, width=200, height=300)

txt_output = Text(win)
txt_output.place(x=750, y=300, width=200, height=300)

ico_path = '.\\fig\\favicon.ico'

if os.path.exists(ico_path):
    win.iconbitmap(ico_path)

bg_path = '.\\fig\\bg.png'
if os.path.exists(bg_path):
    bg_image = PhotoImage(file=bg_path)
    Label(frame, image=bg_image).place(x=0, y=0)

win.mainloop()
