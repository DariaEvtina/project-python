from tkinter import*
from tkinter import ttk
from tkinter import scrolledtext
from tkinter.messagebox import*
from random import*

mas1=[]
mas2=[]
fail=open("wordas.txt",'r',encoding="utf-8-sig")
for line in fail:
 n=line.find(",")# , - разделитель
 mas1.append(line[0:n].strip())
 mas2.append(line[n+1:len(line)].strip())
fail.close()

print(mas1)
def tr2():
 l1_=str(l1.get())
 if l1_ in mas1:
  ide=mas1.index(l1_)
  l2.configure(text=f"{mas2[ide]}")
 elif l1_ in mas2:
  ide=mas2.index(l1_)
  l2.configure(text=f"{mas1[ide]}")
 else:
   l2.configure(text="в словаре нет этого слова")

win=Tk()
win.geometry("750x800")
win.title("Translator-Dictionary")
tabs=ttk.Notebook(win)
tabs_list=[]
tab1=Frame(tabs)
tab2=Frame(tabs)
tab3=Frame(tabs)
tabs.add(tab1,text="translator")
tabs.add(tab2,text="dictionary")
tabs.add(tab3,text="Add new word")
tabs.grid(row=0,column=0,columnspan=5)

l=Label(tab1,text="Translator - Dictionary",font="Calibri 18",fg="lightslategrey",bg="ghostwhite",width=20)
l1=Entry(tab1,font="Calibri 22",fg="ghostwhite",bg="lightslategrey",width=20)
ll=Label(tab1,text="----",font="Calibri 11",fg="ghostwhite",bg="lightslategrey",width=10)
l2=Label(tab1,text="---------",font="Calibri 22",fg="ghostwhite",bg="lightslategrey",width=23)
btn=Button(tab1,text="translate",font="Calibri 18",fg="ghostwhite",bg="dark gray",width=20,command=tr2)
l.grid(row=1,column=0,columnspan=5)
l1.grid(row=2,column=0,columnspan=2)
ll.grid(row=2,column=3)
l2.grid(row=2,column=5,columnspan=2)
btn.grid(row=3,column=0,columnspan=5)
i=0
for y in mas1:
 lab=Label(tab2,text=f"{y}",font="Calibri 22",fg="ghostwhite",bg="lightslategrey",width=15)
 lab.grid(row=i,column=0,columnspan=3)
 i+=1
e=0
for y in mas2:
 lab=Label(tab2,text=f"{y}",font="Calibri 22",fg="ghostwhite",bg="lightslategrey",width=15)
 lab.grid(row=e,column=4,columnspan=3)
 e+=1
txt_box=scrolledtext.ScrolledText(tab3,width=90,height=10)
txt_box.grid(row=0,column=0,columnspan=4)
btn1=Button(tab3,text="Add new word in dictionary",font="Calibri 10",fg="ghostwhite",bg="lightslategrey",width=15)
lb=Label(tab3,text="write the word and translation through ´,´")
btn1.grid(row=1,column=0)
M=Menu(win)
win.config(menu=M)
m1=Menu(M,tearoff=-1)
M.add_cascade(label="Menu",menu=m1)
win.mainloop()
