import tkinter
from tkinter import filedialog
global t
Tk=tkinter.Tk(className="GhTr DIY制作器 ")
l=tkinter.Label(Tk,font=(None,20),text="关卡名")
l.grid(row=0,column=0)
e1=tkinter.Entry(Tk)
e1.grid(row=0,column=1)
l=tkinter.Label(Tk,font=(None,20),text="作者")
l.grid(row=0,column=2)
e2=tkinter.Entry(Tk)
e2.grid(row=0,column=3)
l=tkinter.Label(Tk,font=(None,20),text="简介(使用<br/>换行)")
l.grid(row=1,column=0)
e3=tkinter.Entry(Tk)
e3.grid(row=1,column=1)
l=tkinter.Label(Tk,font=(None,20),text="关卡背景")
l.grid(row=1,column=2)
e4=tkinter.Entry(Tk)
e4.grid(row=1,column=3)
l5=tkinter.Label(Tk,font=(None,20),text="关卡难度")
l5.grid(row=2,column=0)
e5=tkinter.Entry(Tk)
e5.grid(row=2,column=1)
l=tkinter.Label(Tk,font=(None,20),text="所选路线")
l.grid(row=2,column=2)
e6=tkinter.Entry(Tk)
e6.grid(row=2,column=3)
l=tkinter.Label(Tk,font=(None,20),text="四虚无(卡槽虚无、推车虚无、阳光虚无、加点虚无)")
l.grid(row=3,column=0)
e7=tkinter.Entry(Tk)
e7.grid(row=3,column=1)
l=tkinter.Label(Tk,font=(None,20),text="卡槽加点、阳光加点、推车加点(用空格隔开)")
l.grid(row=3,column=2)
e8=tkinter.Entry(Tk)
e8.grid(row=3,column=3)
l=tkinter.Label(Tk,font=(None,20),text="被动加点、主动加点(用空格隔开)")
l.grid(row=4,column=0)
e9=tkinter.Entry(Tk)
e9.grid(row=4,column=1)
l=tkinter.Label(Tk,font=(None,20),text="开始阳光")
l.grid(row=4,column=2)
e10=tkinter.Entry(Tk)
e10.grid(row=4,column=3)

def c():
    global x
    def test():
        global x
        x=t.get(1.0,"end")
        root.destroy()
    root=tkinter.Tk()
    t=tkinter.Text(root)
    t.pack()
    b1=tkinter.Button(root,text="完成",command=test).pack()
b=tkinter.Button(Tk,text="点击编辑僵尸",command=c).grid(row=8,column=3)

l=tkinter.Label(Tk,font=(None,20),text="卡槽数量")
l.grid(row=5,column=0)
e11=tkinter.Entry(Tk)
e11.grid(row=5,column=1)
l=tkinter.Label(Tk,font=(None,20),text="不启用选卡（是或否）")
l.grid(row=5,column=2)
e12=tkinter.Entry(Tk)
e12.grid(row=5,column=3)
l=tkinter.Label(Tk,font=(None,20),text="不预览僵尸（是或否）")
l.grid(row=6,column=0)
e13=tkinter.Entry(Tk)
e13.grid(row=6,column=1)
l=tkinter.Label(Tk,font=(None,20),text="卡槽卡片")
l.grid(row=6,column=2)
e14=tkinter.Entry(Tk)
e14.grid(row=6,column=3)
l=tkinter.Label(Tk,font=(None,20),text="禁用卡片")
l.grid(row=7,column=0)
e15=tkinter.Entry(Tk)
e15.grid(row=7,column=1)
l=tkinter.Label(Tk,font=(None,20),text="强制携带卡片")
l.grid(row=7,column=2)
e16=tkinter.Entry(Tk)
e16.grid(row=7,column=3)
l=tkinter.Label(Tk,font=(None,20),text="未拥有卡片")
l.grid(row=8,column=0)
e17=tkinter.Entry(Tk)
e17.grid(row=8,column=1)
def test_1():
    file=filedialog.asksaveasfilename()
    with open(file,"w",encoding="ANSI") as f:
        f.write("""[文件信息]
关卡名={}
作者名={}
关卡简介={}
[基础信息]
关卡背景={}
关卡难度={}
所选路线={}
卡槽虚无={}
推车虚无={}
阳光虚无={}
加点虚无={}
卡槽加点={}
阳光加点={}
推车加点={}
被动加点={}
主动加点={}
开始阳光={}
[波数信息]
{}
[卡片信息]
卡槽数量={}
不启用选卡={}
不预览僵尸={}
卡槽卡片={}
禁用卡片={}
强制携带卡片={}
未拥有卡片={}""".format(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get().split()[0],e7.get().split()[1],e7.get().split()[2],e7.get().split()[3],e8.get().split()[0],e8.get().split()[1],e8.get().split()[2],e9.get().split()[0],e9.get().split()[1],e10.get(),x,e11.get(),e12.get(),e13.get(),e14.get(),e15.get(),e16.get(),e17.get()))
b=tkinter.Button(Tk,text="完成",command=test_1).grid(row=9,column=2)


Tk.mainloop()















