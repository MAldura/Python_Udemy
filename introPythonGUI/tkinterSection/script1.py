from tkinter import *

window = Tk()
window.title("Lbs to Kg Converter")

def lbs_to_kg():
    kg = str(float(e1_value.get()) * 0.453592) + " Kg"
    t1.config(state="normal")
    if t1.compare("end-1c", "==", "1.0"):
        t1.insert(END,kg)
        t1.config(state="disabled")
    else:
        t1.delete("1.0", END)
        t1.insert(END,kg)
        t1.config(state="disabled")

lbl1 = Label(text="Lbs:")
lbl1.grid(row=0,column=0)

e1_value = StringVar()
e1 = Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

lbl2 = Label(text="Kg:")
lbl2.grid(row=0,column=2)

t1 = Text(window,height=1,width=20)
t1.grid(row=0,column=3)

b1 = Button(window, text = "Convert",command=lbs_to_kg)
b1.grid(row=0,column=4,rowspan=2)

window.mainloop()