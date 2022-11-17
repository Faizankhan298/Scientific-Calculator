from tkinter import * 
import tkinter.messagebox as tmsg
import math as m

root = Tk()
root.title("Scientific Calculator")

sc = StringVar()
sc = Entry(root, width=48,textvariable=sc,relief=SUNKEN,font="cosmicsansms 20")
sc.grid(row=0,column=0,columnspan=8,padx=10,pady=10) 

def sciCal(event):
    key = event.widget
    text = key['text']
    val = sc.get()
    sc.delete(0,END)
    if text=="Sin":
        sc.insert(0,m.sin(float(val)))
    elif text=="Cos":
        sc.insert(0,m.cos(float(val)))  
    elif text=="Tan":
        sc.insert(0,m.tan(float(val)))
    
    elif text=="Log":
        if(float(val)<=0.00):
            sc.insert(0,"Not Possible")
        else:
            sc.insert(0,m.log10(float(val)))
    elif text=="Inv":
        if(float(val)<=0.00):
            sc.insert(0,"Not Possible")
        else:
            sc.insert(0,m.log(float(val)))
    elif text=="√":
        sc.insert(0,m.sqrt(float(val)))
    elif text=="!":
        sc.insert(0,m.factorial(int(val)))
    elif text=="rad":
        sc.insert(0,m.radians(float(val)))
    elif text=="deg":
        sc.insert(0,m.degrees(float(val)))
    elif text=="1/x":
        if(val=="0"):
            sc.insert(0,"ꝏ")
        else:
            sc.insert(0,1/float(val))
    elif text=="π":
        if val=="":
             ans = str(m.pi)
             sc.insert(0,ans)
        else:
            ans = str(float(val) * (m.pi))
            sc.insert(0,ans)

    elif text=="e":
        if val=="":
            sc.insert(0,str(m.e))
        else:
            sc.insert(0, str(float(val) * (m.e)))
    
def click(event):
    key = event.widget
    text = key['text']
    oldValue = sc.get()
    sc.delete(0,END)
    newValue = oldValue + text
    sc.insert(0,newValue)
              
def clr(event):
    sc.delete(0,END)
    
def backspace(event):
    entered = sc.get()
    length = len(entered)-1
    sc.delete(length,END)
    
def calculate(event):
    answer = sc.get()
    if "^" in answer:
        answer = answer.replace("^","**")
    answer = eval(answer)
    sc.delete(0,END)
    sc.insert(0,answer)
    
class Calculator:
    def __init__(self,txt,r,c,funcName,color="white"):
        self.var = Button(root,text=txt,padx=3,pady=5,fg="black",bg=color,width=10,font="cosmicsansms 12")
        self.var.bind("<Button-1>",funcName)
        self.var.grid(row=r,column=c)

btn0 =Calculator("Inv",1,0,sciCal)

btn1 = Calculator("Log",1,1,sciCal)

btn2 = Calculator("(",1,2,click)

btn3 = Calculator(")",1,3,click)

btn4 = Calculator("Clear",1,4,clr)

btn5 = Calculator("√",1,5,sciCal)

btn6 = Calculator("+",1,6,click) 



btn7 = Calculator("Sin",2,0,sciCal)   

btn8 =  Calculator("Cos",2,1,sciCal) 

btn9 =  Calculator("Tan",2,2,sciCal)  

btn10 = Calculator("7",2,3,click)     

btn11 = Calculator("8",2,4,click)       

btn12 = Calculator("9",2,5,click)        

btn13 = Calculator("-",2,6,click)                               



btn14 = Calculator("%",3,0,click)                                    

btn15 = Calculator("!",3,1,sciCal)                         

btn16 = Calculator("^",3,2,click)                              

btn17 = Calculator("4",3,3,click)    

btn18 =  Calculator("5",3,4,click) 

btn19 =  Calculator("6",3,5,click)

btn20 = Calculator("/",3,6,click)



btn21 = Calculator("Deg",4,0,sciCal)

btn22 = Calculator("e",4,1,sciCal)

btn23 =  Calculator("π",4,2,sciCal)

btn24 = Calculator("1",4,3,click)

btn25 = Calculator("2",4,4,click)

btn26 = Calculator("3",4,5,click)

btn27 = Calculator("*",4,6,click)



btn28 = Calculator("rad",5,0,sciCal)

btn29 = Calculator("1/x",5,1,sciCal)

btn30 = Calculator("⌦",5,2,backspace)   

btn31 =  Calculator(".",5,3,click) 

btn32 =  Calculator("0",5,4,click)

btn33 = Calculator("00",5,5,click)

btn34= Calculator("=",5,6,calculate)

root.mainloop()
