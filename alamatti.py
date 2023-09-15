
from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.configure(bg="#bbffbb")
img1= Image.open("al1.jpeg")
img2= Image.open("al3.jpeg")
img3= Image.open("al4.jpeg")
img4= Image.open("al5.jpeg")
rm1 = img1.resize((350, 250))
img11 = ImageTk.PhotoImage(rm1)
l1 =Label(image=img11)
l1.image = img1
l1.pack(padx=50,pady=20)

rm2 = img2.resize((350, 250))
img12 = ImageTk.PhotoImage(rm2)
l1 =Label(image=img12)
l1.image = img2

rm3 = img3.resize((350, 250))
img13 = ImageTk.PhotoImage(rm3)
l1 =Label(image=img13)
l1.image = img3

rm4 = img4.resize((350, 250))
img14 = ImageTk.PhotoImage(rm4)
l1 =Label(image=img14)
l1.image = img4



ls=[img11,img12,img13,img14]



def forward(no):
    global l
    global bf 
    global bb
    l.place_forget()
    l=Label(image=ls[no-1])
    b2=Button(root,text=">>",command=lambda: forward(no+1))
    b1=Button(root,text="<<",command=lambda: back(no-1))
    l.place(x=590,y=20)
    b1.place(x=550,y=150)
    b2.place(x=955,y=150)
    l=Label(root,text="Alamatti",font=("Gabriola",50,"bold","underline"),bg="#bbffbb",fg="dark green")
    l.place(x=660,y=280)
    if no==4:
        b2=Button(root,text=">>",state=DISABLED)
        b2.place(x=955,y=150)

def back(no):
    global l
    global bf 
    global bb
    l.place_forget()
    l=Label(image=ls[no-1])
    b2=Button(root,text=">>",command=lambda: forward(no+1))
    b1=Button(root,text="<<",command=lambda: back(no-1))
    l.place(x=590,y=20)
    b1.place(x=550,y=150)
    b2.place(x=955,y=150)
    l=Label(root,text="Alamatti",font=("Gabriola",50,"bold","underline"),bg="#bbffbb",fg="dark green")
    l.place(x=660,y=280)
    if no==1:
        b1=Button(root,text="<<",state=DISABLED)
        b1.place(x=550,y=150)
b1=Button(root,text="<<",command=back, state=DISABLED)
b2=Button(root,text=">>",command=lambda: forward(2))
b1.place(x=550,y=150)
b2.place(x=955,y=150)
l=Label(root,text="Alamatti",font=("Gabriola",50,"bold","underline"),bg="#bbffbb",fg="dark green")
l.place(x=660,y=280)
t=Text(root,width=130,height=8,font=("normal",20,),bg="#bbffbb")
des="""              The Almatti Dam is a hydropower project constructed in July 2005 on the Krishna River in North Karnataka, India. 
The dam’s yearly electric output goal is 560 MU (or GWh).

            The Almatti Dam serves as the major reservoir for the Upper Krishna Irrigation Project; the 290 MW power station is
located on the dam’s right side. Vertical  kaplan turbines are used in the  plant, with  five  55MWgenerators  and one 15MW 
generator. After being used for power generating, water is discharged into the  Narayanpur reservoir to service downstream
irrigation  demands.  Power  generation  capabilities  are  provided  by  two different  facilities,  Almatti  1  Powerhouse  and
Almatti II Powerhouse, which are separated by distance.   """
t.insert(END, des)
t.place(x=5,y=420)
root.geometry("1532x840")
root.mainloop()