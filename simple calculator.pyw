from tkinter import*
from tkinter import messagebox
import sys
import math

top = Tk()
top.geometry("400x350")

#Define
def plus():
    intt1= int(int1.get())
    intt2= int(int2.get())
    plus1= intt1+intt2
    out1= Label(top, text=plus1, font=("Helvetica", 16), borderwidth=2, relief='groove').place(x=120, y=150)

def substraction():
    intt1= int(int1.get())
    intt2= int(int2.get())
    subs1= intt1 - intt2
    out2= Label(top, text= subs1, font=("Helvetica", 16), borderwidth=2, relief="groove").place(x=120, y= 150)

def multiple():
    intt1= int(int1.get())
    intt2= int(int2.get())
    mult1= intt1*intt2
    out3= Label(top, text= mult1, font= ('Helvetica', 16), borderwidth= 2, relief='groove').place(x=120, y=150)

def division():
    intt1= int(int1.get())
    intt2= int(int2.get())
    div1= intt1/intt2
    out4= Label(top, text= div1, font=('Helvetica', 16), borderwidth= 2, relief= 'groove').place(x=120, y=150)

def exit():
    sys.exit()

#Tampilan
int1= IntVar()
int2= IntVar()

lbl1= Label(top, text= "Input 1 = ", font=("Helvetica", 16)).place(x=20, y=50)
inp1= Entry(top, textvariable=int1,font=("Hetvetica", 16)).place(x=120, y=50, height= 30)
lbl2= Label(top, text= "Input 2 = ", font=("Helvetica", 16)).place(x=20, y=100)
inp2= Entry(top, textvariable=int2, font=("Helvetica", 16) ).place(x=120, y=100, height= 30)

lbl3= Label(top, text="Hasil = ", font=('Helvetica', 16)).place(x=20, y=150)



#Button
btn1= Button(top, text='Add',command= plus).place(x=23, y=300)
btn2= Button(top, text='Substract', command= substraction).place(x= 60, y=300)
btn3= Button(top, text='Multiply', command= multiple).place(x=125, y=300)
btn4= Button(top, text='Divide', command= division).place(x= 185, y= 300)

btn5= Button(top, text='Exit', command= exit).place(x= 235, y=300)



top.mainloop()