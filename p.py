from tkinter import *
from PIL import ImageTk,Image
root=Tk()
f=Frame(root,width=1000,height=300,bg="red")
f.pack()
img3 = Image.open("bgk.jpg")
rm3 = img3.resize((250, 200))
img13 = ImageTk.PhotoImage(rm3)
l3 = Label(f,image=img13)
l3.image = img3
l.pack(padx=50,pady=20)
l=Label(root,text="Banashankari Temple",font=("italic",50,"bold","underline"))
l.place(x=490,y=230)
root.mainloop()