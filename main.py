from tkinter import*

def btnClick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)

def btnClear():
    global operator
    operator=""
    text_Input.set("")

def btnEqualsInput():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""

cal = Tk()
cal.title("Calculator")

operator=""

text_Input =StringVar()

txtDisplay = Entry(cal,font=('arial', 20 ,'bold'), textvariable=text_Input, bd=15, insertwidth=3,
                bg="powder blue", justify='right').grid(columnspan=4)


#========================================1nd Line=====================================================#

btn7=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20 , 'bold'), text="7", bg="powder blue",command=lambda:btnClick(7)).grid(row=2,column=0)

btn8=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20 , 'bold'), text="8", bg="powder blue",command=lambda:btnClick(8)).grid(row=2,column=1)

btn9=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20 , 'bold'), text="9", bg="powder blue",command=lambda:btnClick(9)).grid(row=2,column=2)

Add=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20 , 'bold'), text="+", bg="powder blue",command=lambda:btnClick('+')).grid(row=2,column=3)

#========================================2nd Line=====================================================#

btn4=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20 , 'bold'), text="4", bg="powder blue",command=lambda:btnClick(4)).grid(row=3,column=0)

btn5=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20 , 'bold'), text="5", bg="powder blue",command=lambda:btnClick(5)).grid(row=3,column=1)

btn6=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20 , 'bold'), text="6", bg="powder blue",command=lambda:btnClick(6)).grid(row=3,column=2)

Sub=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20 , 'bold'), text="-", bg="powder blue",command=lambda:btnClick('-')).grid(row=3,column=3) 

#=========================================3rd Line========================================================#

btn1=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20 , 'bold'), text="1", bg="powder blue",command=lambda:btnClick(1)).grid(row=4,column=0)

btn2=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20 , 'bold'), text="2", bg="powder blue",command=lambda:btnClick(2)).grid(row=4,column=1)

btn3=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20 , 'bold'), text="3", bg="powder blue",command=lambda:btnClick(3)).grid(row=4,column=2)

Mult=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20 , 'bold'), text="x", bg="powder blue",command=lambda:btnClick('*')).grid(row=4,column=3)

#=========================================4th Line========================================================#

Div=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20 , 'bold'), text="÷", bg="powder blue",command=lambda:btnClick('/')).grid(row=5,column=3) 

btnC=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20 , 'bold'), text="C", bg="powder blue",command= btnClear).grid(row=5,column=1)

Equal=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20 , 'bold'), text="=", bg="powder blue",command= btnEqualsInput).grid(row=5,column=2)

btn0=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20 , 'bold'), text="0", bg="powder blue",command=lambda:btnClick(0)).grid(row=5,column=0)

cal.mainloop()