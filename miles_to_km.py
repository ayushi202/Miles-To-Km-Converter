from tkinter import *

window=Tk()
window.title("miles to KM Converter")
window.minsize(height=200,width=400)
window.config(padx=20,pady=20)

def milestokm():
    miles=input.get()
    miles=int(miles)
    km =miles// 0.62137
    label3["text"]=int(km)
    
    
input=Entry(width=7)
print(input.get())
input.grid(row=0,column=2)

label=Label(text="Miles",font=("Arial",18))
label.config(padx=10)
label.grid(row=0,column=3)

label2=Label(text="is equal to",font=("Arial",18))
label2.config(padx=10)
label2.grid(row=1,column=1)

label3=Label(text="0",font=("Arial",18))
label3.config(padx=20,pady=20)
label3.grid(row=1,column=2)

label4=Label(text="Km",font=("Arial",18))
label4.config(padx=10)
label4.grid(row=1,column=3)

button=Button(text="Convert",command=milestokm)
button.grid(row=3,column=2)


window.mainloop()
