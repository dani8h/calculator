from tkinter import *
root=Tk()
root.title("Danish's Calculator")

##########################################################################################################
#FUNCTIONS


def btn(n):
    current=scrn.get()
    scrn.delete(0, END)
    scrn.insert(0,str(current)+str(n))


def cls():
    scrn.delete(0,END)


def add():
    f_num=scrn.get()
    global x, a
    x=int(f_num)
    scrn.delete(0,END)
    a="add"

def sub():
    f_num=scrn.get()
    global x, a
    x=int(f_num)
    scrn.delete(0,END)
    a="sub"



def mul():
        f_num=scrn.get()
        global x, a
        x=int(f_num)
        scrn.delete(0,END)
        a="mul"



def div():
        f_num=scrn.get()
        global x, a
        x=int(f_num)
        scrn.delete(0,END)
        a="div"

def equal():
    y=scrn.get()
    y=int(y)
    scrn.delete(0,END)
    
    if a=="add":
        scrn.insert(0, x+y)
    
    if a=="sub":
        scrn.insert(0, x-y)

    if a=="mul":
        scrn.insert(0, x*y)

    if a=="div":
        try:
            m=x/y
        except:
            scrn.insert(0, "error")
        else:
            scrn.insert(0, m)



#############################################################################################################
scrn=Entry(root, width=50, borderwidth=5)
scrn.grid(row=0, column=0, columnspan=4,padx=5, pady=10)

#############################################################################################################
button1=Button(root, text="1",padx=30, pady=30, command=lambda: btn(1))
button2=Button(root, text="2",padx=30, pady=30, command=lambda: btn(2))
button3=Button(root, text="3",padx=30, pady=30, command=lambda: btn(3))
button4=Button(root, text="4",padx=30, pady=30, command=lambda: btn(4))
button5=Button(root, text="5",padx=30, pady=30, command=lambda: btn(5))
button6=Button(root, text="6",padx=30, pady=30, command=lambda: btn(6))
button7=Button(root, text="7",padx=30, pady=30, command=lambda: btn(7))
button8=Button(root, text="8",padx=30, pady=30, command=lambda: btn(8))
button9=Button(root, text="9",padx=30, pady=30, command=lambda: btn(9))
button0=Button(root, text="0", padx=30, pady=30, command=lambda: btn(0))


button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0)
###########################################################################

btn_add=Button(root, text="+", padx=30, pady=30, command=add)
btn_sub=Button(root, text="-", padx=30, pady=30, command=sub)
btn_mul=Button(root, text="x", padx=30, pady=30, command=mul)
btn_div=Button(root, text="%", padx=30, pady=30, command=div)
btn_cls=Button(root, text="cls", padx=30, pady=30, command=cls)
btn_equal=Button(root,text="=", padx=30, pady=30, command=equal)

btn_add.grid(row=1, column=3)
btn_sub.grid(row=2, column=3)
btn_mul.grid(row=3, column=3)
btn_div.grid(row=4, column=3)
btn_cls.grid(row=4, column=1)
btn_equal.grid(row=4, column=2)










root.mainloop()



