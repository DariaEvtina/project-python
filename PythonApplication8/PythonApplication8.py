from tkinter import*
from tkinter import ttk
from tkinter import scrolledtext
from tkinter.messagebox import*
from random import*

mas2=[]
f=open("wordsa.txt",'r',encoding="utf-8-sig")
for l in f:
 mas2.append(l)
f.close()
mas1=[]
fail=open("wordas.txt",'r',encoding="utf-8-sig")
for l in fail:
 mas1.append(l)
fail.close()
print(mas2)
def show_list():
 i=0
 e=0
 for l in mas1:
  lab1=Label(tab2,text=f"{l}",font="Calibri 11",fg="ghostwhite",bg="lightslategrey",width=15)
  lab1.grid(row=e,column=2)
  e+=1
 for y in mas2:
  lab=Label(tab2,text=f"{y}",font="Calibri 11",fg="ghostwhite",bg="lightslategrey",width=15)
  lab.grid(row=i,column=3)
  i+=1
    
def add_words():
 global o
 o_=o.get()
 n=o_.find(",")# , - разделитель
 mas1.append(o_[0:n].strip())
 mas2.append(o_[n+1:len(o_)].strip())
 f=open("wordsa.txt",'a',encoding="utf-8-sig")
 f.write(mas2[len(mas2)-1]+"\n")
 f.close()
 f_=open("wordas.txt",'a',encoding="utf-8-sig")
 f_.write(mas1[len(mas1)-1]+"\n")
 f_.close()
        #lb.configure(text="If you need to simultaneously add several words to the dictionary,\n enter the word and its translation separated by commas ','.\n(example:небо,sky)",bg="lightslategrey")
a=0
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
def testing():
 global a
 a+=1
def result():
    global name,a
    if name.get()!=" ":
     fail_=open("Result.txt","a",encoding="utf-8-sig")
     fail_.write(name+","+f"5:{a}")
     fail_.close()
def test():
 win1=Tk()
 win1.geometry("300x400")
 win1.title("TEST")
 e=0
 e1=1
 for i in range(5):
  r=randint(0,(len(mas1)-1))
  r_=randint(0,(len(mas1)-1))
  r_1=randint(0,(len(mas1)-1))
  if r_1==r_ or r_1==r:
       r_1=randint(0,(len(mas1)-1))
  else:
      pass
  random_=randint(0,2)
  if random_==2:
      r3=Radiobutton(win1,text=f"{mas1[r]}",font="Calibri 10",fg="ghostwhite",width=5,command=testing)
      r2=Radiobutton(win1,text=f"{mas1[r_]}",font="Calibri 10",fg="ghostwhite",width=5)
      r1=Radiobutton(win1,text=f"{mas1[r_1]}",font="Calibri 10",fg="ghostwhite",width=5)
  elif random_==1:
      r3=Radiobutton(win1,text=f"{mas1[r_1]}",font="Calibri 10",fg="ghostwhite",width=5)
      r2=Radiobutton(win1,text=f"{mas1[r]}",font="Calibri 10",fg="ghostwhite",width=5,command=testing)
      r1=Radiobutton(win1,text=f"{mas1[r_]}",font="Calibri 10",fg="ghostwhite",width=5)
  else:
      r3=Radiobutton(win1,text=f"{mas1[r_]}",font="Calibri 10",fg="ghostwhite",width=5)
      r2=Radiobutton(win1,text=f"{mas1[r_1]}",font="Calibri 10",fg="ghostwhite",width=5)
      r1=Radiobutton(win1,text=f"{mas1[r]}",font="Calibri 10",fg="ghostwhite",width=5,command=testing)
  labele=Label(win1,text=f"{mas2[r]}-???",font="Calibri 10",fg="ghostwhite",bg="lightslategrey",width=15)
  labele.grid(row=e,column=0)
  r1.grid(row=e1,column=0)
  r2.grid(row=e1,column=1)
  r3.grid(row=e1,column=2)
  e+=2
  e1+=2
 name=Entry(win1,font="Calibri 14",fg="ghostwhite",bg="lightslategrey",width=15)
 name.grid(row=10,column=0)
 win1.mainloop()
#############################################################################################################################################

win=Tk()
win.geometry("990x400")
win.title("Translator-Dictionary")
M=Menu(win)
win.config(menu=M)
m1=Menu(M,tearoff=1)
M.add_cascade(label="Menu",menu=m1)
m1.add_command(label="test",command=test)

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
l7=Label(tab3,text="eng/rus",font="Calibri 22",fg="ghostwhite",bg="lightslategrey",width=10)
o=Entry(tab3,font="Calibri 22",fg="ghostwhite",bg="lightslategrey",width=25)
btn1=Button(tab3,text="Add new words in dictionary",font="Calibri 10",fg="ghostwhite",bg="lightslategrey",width=25,command=add_words)


l7.grid(row=0,column=0)
o.grid(row=0,column=1)
btn1.grid(row=1,column=0)
#b.grid(row=3,column=0)
#b.grid(row=3,column=1)
#.grid(row=3,column=2)



win.mainloop()
