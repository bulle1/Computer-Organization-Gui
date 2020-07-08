
from tkinter import *
import turtle
from copy import copy
import re
#------------------------------------------------------------------------------
def FIFO(Request, Start):
    Sum = 0                     #initialize to 0
    position = Start            #set current position = start
    Order = []                  # creates empty list of name Order
    Order.append(Start)         #adds Start to end of list Order
    for i in Request:
        if i != Start:              # i is the current element in the list(first loop i = 95)
            Sum += abs(i-position)  # sum = sum + (distance of current position from next position)
            position = i            # set position new position (i)
            Order.append(i)         # Add i to the end of the list Order
    return Order, Sum
#------------------------------------------------------------------------------
def SSTF(Request,Start):
    if Start in Request:
        Request.remove(Start)
    templist = copy(Request)
    position = Start
    highest = max(templist)
    mindiff=abs(Start-highest)
    j=highest
    templist.sort()
    Order = []
    Order.append(Start)
    Sum = 0
    while len(templist) > 0:
        for i in templist:
                diff= abs(position-i)
                if diff<mindiff:
                    mindiff=diff
                    j=i
        Sum+= abs(position-j)
        position = j
        templist.remove(j)
        Order.append(j)
        mindiff=abs(position-highest)
        j=highest
    return Order, Sum
#------------------------------------------------------------------------------
def SCAN(Request, Start):
    if Start in Request:
        Request.remove(Start)
    n = len(Request)
    Order = []
    Request_tmp=copy(Request)
    Request_tmp.sort()
    if Start != 0 and Start < Request_tmp[n-1]:
        Request_tmp.append (0)
    p = len(Request_tmp)

    i = Start - 1
    Order.append(Start)
    while i >= 0:
        for j in range(0,p):
            if(Request_tmp[j] == i):
                Order.append(i)
        i -= 1




    k = Start + 1
    while k < 200:
        for l in range(0,n):
            if(Request[l] == k):
                Order.append(k)
        k += 1

    Sum = 0
    for p in range(0,len(Order) - 1):
        Sum += abs(Order[p] - Order[p+1])
    return Order, Sum
#------------------------------------------------------------------------------
def CSCAN(Request, Start):
    if Start in Request:
        Request.remove(Start)
    n = len(Request)
    Order = []
    Request_tmp=copy(Request)
    Request_tmp.sort()
    if Start != 0 and Start < Request_tmp[n-1]:
        Request_tmp.append (0)
    p = len(Request_tmp)

    i = Start - 1
    Order.append(Start)
    while i >= 0:
        for j in range(0,p):
            if(Request_tmp[j] == i):
                Order.append(i)
        i -= 1

    k = 199
    while k > Start:
        if(k == 199):
            Order.append(k)
        for l in range(0,n):
            if(Request[l] == k):
                Order.append(k)
        k -= 1

    Sum = 0
    SortedReq = copy(Order)
    SortedReq.sort()
    for p in range(0,len(Order) - 1):
        if (Order[p] != SortedReq[0]):
            Sum += abs(Order[p] - Order[p+1])
    return Order, Sum
#------------------------------------------------------------------------------
def LOOK(Request, Start):
    if Start in Request:
        Request.remove(Start)
    n = len(Request)                        # Number of Requests
    Order = []
    i = Start - 1
    Order.append(Start)
    while i > 0:                            # Diskhead moving outward from start
        for j in range(0,n):                    #position
            if(Request[j] == i):            # Request found
                Order.append(i)             # Request executed
        i -= 1

    k = Start + 1
    while k < 200:                          # Diskhead moving inward from
        for l in range(0,n):                    #previous position
            if(Request[l] == k):            # Request found
                Order.append(k)             # Request executed
        k += 1

    Sum = 0
    for p in range(0,len(Order) - 1):
        Sum += abs(Order[p] - Order[p+1])   # Calculates total movement
    return Order, Sum
#------------------------------------------------------------------------------
def CLOOK(Request, Start):
    if Start in Request:
        Request.remove(Start)
    n = len(Request)                            # Number of requests
    Order = []
    i = Start - 1
    Order.append(Start)
    while i > 0:                                # Diskhead moving outward from
        for j in range(0,n):                        #start position
            if(Request[j] == i):                # Request found
                Order.append(i)                 # Request executed
        i -= 1

    k = 199
    while k > Start:                            # Diskhead moving inward from
        for l in range(0,n):                        #highest request position
            if(Request[l] == k):                # Request found
                Order.append(k)                 # Request executed
        k -= 1

    Sum = 0
    SortedReq = copy(Order)                     # Creates copy of job order
    SortedReq.sort()                            # Sorts job order from lowest to
    for p in range(0,len(Order) - 1):               #highest
        if (Order[p] != SortedReq[0]):          # Excludes the circular movement
            Sum += abs(Order[p] - Order[p+1])   # Calculates total movement
    return Order, Sum
#------------------------------------------------------------------------------
def Sim(option, request, start):
    if option == "FIFO":                        # Select and run algorithm
        Order, Sum = FIFO(request, start)
    elif option =="SSTF":
        Order, Sum = SSTF(request, start)
    elif option =="SCAN":
        Order, Sum = SCAN(request, start)
    elif option =="CSCAN":
        Order, Sum = CSCAN(request, start)
    elif option =="LOOK":
        Order, Sum = LOOK(request, start)
    elif option =="CLOOK":
        Order, Sum = CLOOK(request, start)
    Disk = turtle.Screen()
    Disk.title("Disk Scheduling")
    Disk.bgcolor("#00BBFF")
    Disk.setworldcoordinates(-5, -20, 210, 10)  # Set turtle window boundaries
    head = turtle.Turtle()
    head.shape("circle")
    head.turtlesize(.3, .3, 1)
    head.speed(1)
    head.pensize(2)
    n = len(Order)
    y = 0
    for i in range(0, n):
        if i == 0:      # No drawing while the diskhead goes to start position
            head.penup()
            head.goto(Order[i], y)
            head.pendown()
            head.stamp()
            head.write(Order[i], False, align="right")
        else:           # Diskhead draws its path to each request
            head.goto(Order[i], y-1)
            head.stamp()
            head.write(Order[i], False, align="right")
            y -= 1
    head.hideturtle()
    head.speed(0)
    head.penup()
    head.goto(100, 5)
    message1 = "Disk Scheduling Algorithm: " + option
    message2 = "Total Head Movement: " + str(Sum)
    head.write(message1, False, align="center")     # Display algorithm used
    head.goto(100,4)
    head.write(message2, False, align="center")     # Display total movement
    head.pendown
    Disk.exitonclick()
#-----------------------------------------------------------------------------
def next(a,b,c): 
    global Request
    Request = a
    Request= re.split(r',|\n| ',Request)
    Request= [int(i) for i in Request if i != '']
    global init
    init = c
    global en
    en = b
#------------------------------------------------------------------------------
    
    #95 180 34 119 11 123 62 64'''
    # GUI - 3x2 Grid
Menu = Tk()
Menu.title("DS")
Menu.geometry('500x500')
newl = Label(Menu , text = "Enter the sequence :")
newl.grid(row = 0 , column = 0)
txtbx = Text(Menu, width = 20 , height = 5)
txtbx.grid(row = 0 , column = 1)
initl1 = Label(Menu , text = "Starting disk value")
initl1.grid(row = 1 , column  = 0)
endl1 = Label(Menu , text = "Ending disk value")
endl1.grid(row = 2 , column  = 0)
initl2 = Entry(Menu ,width = 15)
initl2.grid(row = 1 , column  = 1)
endl2 = Entry(Menu , width = 15)
endl2.grid(row = 2 , column  = 1)
store  = Button(Menu, text = "Store Seq." , command  = lambda:next(txtbx.get('1.0',END),endl2.get(),initl2.get()))
store.grid(row = 3 , column  = 3)
    # List of options in dropdown menu
optionlist = ('FIFO', 'SSTF', 'SCAN', 'CSCAN', 'LOOK', 'CLOOK')
Option = StringVar()
Start = IntVar()
Option.set("FIFO")
L1 = Label(Menu, text = "Choose Algorithm:")                # Label 1
L1.grid(row=7,column=0)
OM = OptionMenu(Menu, Option, *optionlist)                  # Dropdown menu
OM.grid(row=7, column=1)
L2 = Label(Menu, text = "Enter start position:")            # Label 2
L2.grid(row=8, column=0)
E1 = Entry(Menu, textvariable = Start, bd = 3, width = 9)   # Textbox
E1.grid(row=8, column=1,)
B1 = Button(Menu, text = "Run",\
 command = lambda:Sim(Option.get(), Request, Start.get()))  # Button
B1.grid(row=9, column=1)


Menu.mainloop()
