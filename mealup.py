from tkinter import *

def about():
    status_label.configure(text = """
A Simple Resturant Billing Application

Made By
Aman Patel
amanpatel599@gmail.com
""")

def reset():
    burvar1.set(0)
    cburvar1.set(0)
    ffrvar1.set(0)
    cffrvar1.set(0)
    rollvar1.set(0)
    crollvar1.set(0)
    ccdvar1.set(0)
    cofvar1.set(0)
    srvtax = 0
    gst = 0
    cgst = 0
    gtot = 0
    status_label3.configure(text = srvtax)
    status_label4.config(text = gst)
    status_label5.configure(text = cgst)
    status_label2.configure(text = gtot)

def tot():
    a = float(burvar1.get())
    b = float(cburvar1.get())
    c = float(ffrvar1.get())
    d = float(cffrvar1.get())
    e = float(rollvar1.get())
    f = float(crollvar1.get())
    g = float(ccdvar1.get())
    h = float(cofvar1.get())
    tot = a*30+b*70+c*40+d*60+e*50+f*70+g*30+h*50
    status_label0.configure(text = tot)
    status_label.configure(text = """
Your Bill is Generated
Service Tax: 3%
GST: 7%
CGST: 5%
Hope to see you again!
""")
    
    srvtax = float(tot*3/100)
    gst = float(tot*7/100)
    cgst = float(tot*5/100)

    status_label3.configure(text = srvtax)
    status_label4.config(text = gst)
    status_label5.configure(text = cgst)

    gtot =float(tot+srvtax+gst+cgst)
    status_label2.configure(text = gtot)

win = Tk()
win.geometry("1280x720")
win.title("Meal Up Resturant")

burvar1 = StringVar()
cburvar1 = StringVar()
ffrvar1 = StringVar()
cffrvar1 = StringVar()
rollvar1 = StringVar()
crollvar1 = StringVar()
ccdvar1 = StringVar()
cofvar1 = StringVar()
burvar1.set(0)
cburvar1.set(0)
ffrvar1.set(0)
cffrvar1.set(0)
rollvar1.set(0)
crollvar1.set(0)
ccdvar1.set(0)
cofvar1.set(0)


##########################FRAMES####################################
#Frame 0
top = Frame(win, width = 800, height = 50)
top.pack(side = TOP)

#Frame 1
top1 = Frame(win, width = 250, height = 600)
top1.pack(side = LEFT)

#Frame 2
top2 = Frame(win, width =550, height = 600)
top2.pack(side = LEFT)

#####################################################################

##############################FRAME 0################################

lbl0 = Label(top, text = 'Cash Counter', font = ('arial',30), fg = 'black')
lbl0.pack(side = TOP)

button0 = Button(top, text = 'About!', command = about)
button0.pack(side = LEFT)
######################################################################

##############################FRAME 1#################################

lbl_1 = Label(top1, text = 'Burger', font = ('arial',16), fg = 'black')
lbl_1.grid(row = 0, column = 0,stick = W)
entry_1 = Entry(top1, text = burvar1, bd = 10, insertwidth = 4)
entry_1.grid(row = 0, column = 1,)


lbl = Label(top1, text = '                                           ')
lbl.grid(row = 1)


lbl_2 = Label(top1, text = 'French Fries', font = ('arial',16), fg = 'black')
lbl_2.grid(row = 2, column = 0,stick = W)
entry_2 = Entry(top1, text = ffrvar1, bd = 10, insertwidth = 4)
entry_2.grid(row = 2, column = 1)


lbl = Label(top1, text = '                                           ')
lbl.grid(row = 3)


lbl_3 = Label(top1, text = 'Chicken Burger', font = ('arial',16), fg = 'black')
lbl_3.grid(row = 4, column = 0,stick = W)
entry_3 = Entry(top1, text = cburvar1, bd = 10, insertwidth = 4)
entry_3.grid(row = 4, column = 1)


lbl = Label(top1, text = '                                           ')
lbl.grid(row = 5)


lbl_4 = Label(top1, text = 'Chicken Fries', font = ('arial',16), fg = 'black')
lbl_4.grid(row = 6, column = 0,stick = W)
entry_4 = Entry(top1, text = cffrvar1, bd = 10, insertwidth = 4)
entry_4.grid(row = 6, column = 1)


lbl = Label(top1, text = '                                           ')
lbl.grid(row = 7)


lbl_5 = Label(top1, text = 'Roll', font = ('arial',16), fg = 'black')
lbl_5.grid(row = 8, column = 0,stick = W)
entry_5 = Entry(top1, text = rollvar1, bd = 10, insertwidth = 4)
entry_5.grid(row = 8, column = 1)


lbl = Label(top1, text = '                                           ')
lbl.grid(row = 9)


lbl_6 = Label(top1, text = 'Chicken Roll', font = ('arial',16), fg = 'black')
lbl_6.grid(row = 10, column = 0,stick = W)
entry_6 = Entry(top1, text = crollvar1, bd = 10, insertwidth = 4)
entry_6.grid(row = 10, column = 1)


lbl = Label(top1, text = '                                           ')
lbl.grid(row = 11)


lbl_7 = Label(top1, text = 'Cold-Drink', font = ('arial',16), fg = 'black')
lbl_7.grid(row = 12, column = 0,stick = W)
entry_7 = Entry(top1, text = ccdvar1, bd = 10, insertwidth = 4)
entry_7.grid(row = 12, column = 1)


lbl = Label(top1, text = '                                           ')
lbl.grid(row = 13)


lbl_8 = Label(top1, text = 'Coffee', font = ('arial',16), fg = 'black')
lbl_8.grid(row = 14, column = 0,stick = W)
entry_8 = Entry(top1, text = cofvar1, bd = 10, insertwidth = 4)
entry_8.grid(row = 14, column = 1)

lbl = Label(top1, text = '                                           ')
lbl.grid(row = 15)

lbl = Label(top1, text = '                                           ')
lbl.grid(row = 16)


button1 = Button(top1, text = 'Calculate', command = tot)
button1.grid(row = 17, column = 1)

#######################################################################

###########################FRAME 2#####################################

label = Label(top2, text = 'Total Bill')
label.grid(row = 0,column = 0,stick = E)

status_label0 =Label(top2, height =2, width =20, bg ="white", wraplength =150)
status_label0.grid(row =0, column =1)

lbl = Label(top2, text = '                                           ')
lbl.grid(row = 1)

status_label =Label(top2, height =10, width =30, bg ="white", wraplength =150)
status_label.grid(row =2, column =1)

status_label.configure(text = """
Welcome to the Meal Up Resturant
Fast Food Hub
mealup@mealup.co.in
""")


lbl = Label(top2, text = '                                           ')
lbl.grid(row = 3)

lbl = Label(top2, text = '                                           ')
lbl.grid(row = 4)

lbl01 = Label(top2, text = 'Service Tax', font = ('arial',16), fg = 'black')
lbl01.grid(row = 5, column = 0)
status_label3 =Label(top2, height =2, width =20, bg ="white", wraplength =150)
status_label3.grid(row =5, column =1)

lbl = Label(top2, text = '                                           ')
lbl.grid(row = 6)

lbl01 = Label(top2, text = 'GST', font = ('arial',16), fg = 'black')
lbl01.grid(row = 7, column = 0)
status_label4 =Label(top2, height =2, width =20, bg ="white", wraplength =150)
status_label4.grid(row = 7, column =1)

lbl = Label(top2, text = '                                           ')
lbl.grid(row = 8)

lbl01 = Label(top2, text = 'CGST', font = ('arial',16), fg = 'black')
lbl01.grid(row =9, column = 0)
status_label5 =Label(top2, height =2, width =20, bg ="white", wraplength =150)
status_label5.grid(row = 9, column =1)

lbl = Label(top2, text = '                                           ')
lbl.grid(row = 10)

lbl = Label(top2, text = '                                           ')
lbl.grid(row = 11)

lbl = Label(top2, text = '                                           ')
lbl.grid(row = 12)

lbl01 = Label(top2, text = 'GRAND TOTAL', font = ('arial',16,'bold'), fg = 'black')
lbl01.grid(row = 13, column = 0)

status_label2 =Label(top2, height =2, width =20, bg ="white", wraplength =150)
status_label2.grid(row =14, column =1)

lbl = Label(top2, text = '                                           ')
lbl.grid(row = 15)

button0 = Button(top2, text = 'RESET', command = reset)
button0.grid(row = 16, column = 0)

button1 = Button(top2, text = 'QUIT!', command = quit)
button1.grid(row = 17, column = 1)

#######################################################################


win.mainloop()
