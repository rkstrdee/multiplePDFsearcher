from tkinter import *
import PyPDF2
import re
import os
import webbrowser

def callback(url):
    webbrowser.open_new(url)

def goforit(a,String):
    # open the pdf file
    object = PyPDF2.PdfFileReader(a)

    # get number of pages
    NumPages = object.getNumPages()

    # define keyterms

    # extract text and do the search
    cnt=0
    foc=-1
    for i in range(0, NumPages):
        PageObj = object.getPage(i)
        Text = PageObj.extractText()
        if re.search(String, Text, re.IGNORECASE):
            if cnt==0:
                foc=i
            cnt+=1
    ret=[]
    if cnt!=0:
        ret.append(" found "+String+" in the pdf - "+str(a)+" goto page number "+str(foc)+"\n( "+str(cnt)+" occurances )\n")
    else:
        ret.append("Oh no! no occurance of your word found\n")
    return ret


    

root = Tk()
root.geometry("900x600")

root.title("Made with Python for math peeps")

up = Frame(root, borderwidth=2, relief="solid")

up.pack(side="top", expand=True, fill="both")

uplft=Frame(up,width=50)

uplft.pack(side="left")

upcent=Frame(up,width=50)

upcent.pack(side="left")

uprgt=Frame(up,width=50)

uprgt.pack(side="left")

lbl = Label(uplft, text="the word you want to search : ",font=("Courier", 18))

lbl.pack()

txt = Entry(upcent,width=25)

txt.pack()

lbl2=Label(up,text="")
lbl2.pack(side="right")

files = [f for f in os.listdir('.') if os.path.isfile(f)]
files = filter(lambda f: f.endswith(('.pdf','.PDF')), files)
for a in files:
    link1 = Label(root, text=str(a), fg="blue", cursor="hand2")
    link1.pack()
    link1.bind("<Button-1>", lambda e: webbrowser.open_new(r"file://"+os.path.realpath(str(a))))

scrollbar = Scrollbar(root)
scrollbar.pack(side = RIGHT, fill = Y)
 
area = Text(root, yscrollcommand = scrollbar.set,font="Calibri 16")

area.pack(expand=True, fill='both')

scrollbar.config(command = area.yview)



def fun(tString):
    area.delete('1.0', END)
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    files = filter(lambda f: f.endswith(('.pdf','.PDF')), files)
    tString
    for a in files:
        lst=goforit(a,tString)
        for b in lst:
            area.insert(END,b+'\n')
        

def solveqry(a):
    fun(a)
    lbl2.configure(text="search sucessful")

def clicked():
    solveqry(txt.get())

btn = Button(uprgt, text=" Go ", command=clicked)

btn.pack()


root.mainloop()
