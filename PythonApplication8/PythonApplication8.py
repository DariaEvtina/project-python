from tkinter import*
from tkinter import ttk
from tkinter import scrolledtext
from tkinter.messagebox import*
from random import*



mas1=[]
mas2=[]
fail=open("wordas.txt",'r',encoding="utf-8-sig")
for l in fail:
 mas1.append(l)
fail.close()
f=open("words.txt",'r',encoding="utf-8-sig")
for l in f:
 mas2.append(l)
fail.close()
def list_():
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

def show_list():
    labs=list_
    btt=Button(tab2,text="close dictionary",font="Calibri 10",fg="ghostwhite",bg="lightslategrey",width=25)
    btt.grid(row=(len(mas1))+1,column=2)
def add_words():
        t=txt_box.get(0.0,END)
        for line in t:
            n=line.find(",")# , - разделитель
            mas1.append(line[0:n].strip())
            mas2.append(line[n+1:len(line)].strip())
        f=open("wordas.txt",'w',encoding="utf-8-sig")
        for i in mas2:
            f.write("\n"+i)
        f.close()
        f=open("words.txt",'w',encoding="utf-8-sig")
        for i in mas1:
            f.write("\n"+i)
        f.close()
        #lb.configure(text="If you need to simultaneously add several words to the dictionary,\n enter the word and its translation separated by commas ','.\n(example:небо,sky)",bg="lightslategrey")

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

def delete_(e):
    if e in mas1:
        lk=Label(tab3,text="correct the word:",font="Calibri 10",fg="ghostwhite",bg="lightslategrey",width=24)
        p=Entry(tab3,font="Calibri 10",fg="ghostwhite",bg="lightslategrey",width=25)
        lk.grid(row=3,column=0)
        p.grid(row=3,column=1)
        ind=mas1.index(ee)
        mas1.pop(ind)
        mas1.insert(ind,str(p))
        fail=open("words.txt",'w',encoding="utf-8-sig")
        for i in r :
            fail.write(i+"\n")
        fail.close()
    elif e in mas2:
        lk=Label(tab3,text="correct the word:",fg="ghostwhite",bg="lightslategrey",width=25)
        p=Entry(tab3,font="Calibri 10",fg="ghostwhite",bg="lightslategrey",width=25)
        lk.grid(row=3,column=0)
        p.grid(row=3,column=1)
        a=str(p)
        ind=mas2.index(ee)
        mas2.pop(ind)
        mas2.insert(ind,a)
        fail=open("wordas.txt",'w',encoding="utf-8-sig")
        for i in mas2:
            fail.write(i+"\n")
        fail.close()
    else:
       l=Label(tab3,text=f"{v} этого слова нет в программе",font="Calibri 10",fg="ghostwhite",bg="lightslategrey",width=25)
       l.grid(row=2,column=2)

#############################################################################################################################################

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
btns=Button(tab2,text="show dictionary",font="Calibri 10",fg="ghostwhite",bg="lightslategrey",width=25,command=show_list)
btns.grid(row=0,column=2)
txt_box=scrolledtext.ScrolledText(tab3,width=90,height=10)
txt_box.grid(row=0,column=0,columnspan=4)
btn1=Button(tab3,text="Add new words in dictionary",font="Calibri 10",fg="ghostwhite",bg="lightslategrey",width=25,command=add_words)
lb=Label(tab3,text="If you need to simultaneously add several words to the dictionary,\n enter the word and its translation separated by commas ','.\n(example:sky,небо)",font="Calibri 9",fg="ghostwhite",bg="lightslategrey",width=90)
btn1.grid(row=1,column=0)
lb.grid(row=1,column=1,columnspan=3)
ind=0
v=Label(tab3,text="enter the word you want to correct: ",font="Calibri 10",fg="ghostwhite",bg="lightslategrey",width=24)
e=Entry(tab3,font="Calibri 10",fg="ghostwhite",bg="lightslategrey",width=24,command=delete_(str(e))
v.grid(row=2,column=0)
e.grid(row=2,column=1)


win.mainloop()
