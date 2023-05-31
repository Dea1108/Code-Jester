

from tkinter import *

root= Tk()
root.title(" კალკულატორი")

text_Input= StringVar()
operator = ""

def btnClick(numbers):
    global operator
    operator += str(numbers)
    text_Input.set(operator)
def btnClearDisplay():
    global operator
    operator= ""
    text_Input.set(operator)

def btnEquals():
    global operator
    total = str(eval(operator))
    text_Input.set(total)


txtDisplay = Entry(root,
                   bd = 30,
                   font = ('arial', 20),
                   insertwidth = 4,
                   bg = 'light yellow',
                   justify = 'right',
                   textvariable= text_Input).grid(columnspan=4)


btnClear= Button(root,
                 padx = 59,
                 pady = 15,
                 bd = 8,
                 font = ('arial',20),
                 text= "C",
                 bg = 'light pink',
                 command = btnClearDisplay).grid(row = 1, columnspan =2)
btnbracket1= Button(root,
                    padx = 19,
                    pady =15,
                    bd = 8,
                    font = ('arial',20),
                    text = "(",
                    bg = 'light pink',
                    command = lambda: btnClick("(")).grid(row = 1, column= 2)
btnbracket2= Button(root,
                    padx = 19,
                    pady =15,
                    bd = 8,
                    font = ('arial',20),
                    text = ")",
                    bg = 'light pink',
                    command = lambda: btnClick(")")).grid(row = 1, column= 3)
btn7= Button(root,
                    padx = 16,
                    pady =16,
                    bd = 8,
                    font = ('arial',20),
                    text = "7",
                    bg = 'light pink',
                    command = lambda: btnClick("7")).grid(row = 2, column= 0)
btn8= Button(root,
                    padx = 16,
                    pady =16,
                    bd = 8,
                    font = ('arial',20),
                    text = "8",
                    bg = 'light pink',
                    command = lambda: btnClick("8")).grid(row = 2, column= 1)
btn9= Button(root,
                    padx = 16,
                    pady =16,
                    bd = 8,
                    font = ('arial',20),
                    text = "9",
                    bg = 'light pink',
                    command = lambda: btnClick(9)).grid(row = 2, column= 2)
division= Button(root,
                    padx = 19,
                    pady =19,
                    bd = 8,
                    font = ('arial',20),
                    text = "/",
                    bg = 'light pink',
                    command = lambda: btnClick("/")).grid(row = 2, column= 3)
btn4= Button(root,
                    padx = 16,
                    pady =16,
                    bd = 8,
                    font = ('arial',20),
                    text = "4",
                    bg = 'light pink',
                    command = lambda: btnClick("4")).grid(row = 3, column= 0)
btn5= Button(root,
                    padx = 16,
                    pady =16,
                    bd = 8,
                    font = ('arial',20),
                    text = "5",
                    bg = 'light pink',
                    command = lambda: btnClick("5")).grid(row = 3, column= 1)
btn6= Button(root,
                    padx = 16,
                    pady =16,
                    bd = 8,
                    font = ('arial',20),
                    text = "6",
                    bg = 'light pink',
                    command = lambda: btnClick("6")).grid(row = 3, column= 2)
minus= Button(root,
                    padx = 19,
                    pady =19,
                    bd = 8,
                    font = ('arial',20),
                    text = "-",
                    bg = 'light pink',
                    command = lambda: btnClick("-")).grid(row = 3, column= 3)

btn1= Button(root,
                    padx = 16,
                    pady =16,
                    bd = 8,
                    font = ('arial',20),
                    text = "1",
                    bg = 'light pink',
                    command = lambda: btnClick("1")).grid(row = 4, column= 0)
btn2= Button(root,
                    padx = 16,
                    pady =16,
                    bd = 8,
                    font = ('arial',20),
                    text = "2",
                    bg = 'light pink',
                    command = lambda: btnClick("2")).grid(row = 4, column= 1)
btn3= Button(root,
                    padx = 16,
                    pady =16,
                    bd = 8,
                    font = ('arial',20),
                    text = "3",
                    bg = 'light pink',
                    command = lambda: btnClick("3")).grid(row = 4, column= 2)
multi= Button(root,
                    padx = 19,
                    pady =19,
                    bd = 8,
                    font = ('arial',20),
                    text = "*",
                    bg = 'light pink',
                    command = lambda: btnClick("*")).grid(row = 4, column= 3)
btn0= Button(root,
                    padx = 16,
                    pady =16,
                    bd = 8,
                    font = ('arial',20),
                    text = "0",
                    bg = 'light pink',
                    command = lambda: btnClick("0")).grid(row = 5, column= 0)
point= Button(root,
                    padx = 16,
                    pady =16,
                    bd = 8,
                    font = ('arial',20),
                    text = ".",
                    bg = 'light pink',
                    command = lambda: btnClick(".")).grid(row = 5, column= 1)
equal= Button(root,
                    padx = 16,
                    pady =16,
                    bd = 8,
                    font = ('arial',20),
                    text = "=",
                    bg = 'light pink',
                    command= btnEquals).grid(row = 5, column= 2)
plus= Button(root,
                    padx = 19,
                    pady =19,
                    bd = 8,
                    font = ('arial',20),
                    text = "+",
                    bg = 'light pink',
                    command = lambda: btnClick("+")).grid(row = 5, column= 3)
print(root.mainloop())