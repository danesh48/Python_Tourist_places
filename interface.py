from tkinter import *
class interface:
    def __init__(self,root):
        self.f=Frame(width=800,height=840,bg="sky blue")
        self.f.propagate(0)
        self.f.place(x=0,y=0)
        self.l=Label(self.f,text="WELCOME TO BAGALKOT",font=("new Time",40,"bold"),bg="sky blue")
        self.l.place(x=10,y=100)
        self.L=Listbox(self.f,font=("new times",20),bg="#ccffff",width=13,height=8,activestyle="underline",selectmode="SINGLE")
        self.L.place(x=20,y=200)
        pla=["Badami","Kudalasangam","Pattadakallu","Alamatti"]
        for c in pla:
            self.L.insert(END,c)
        self.b=Button(self.f,text="click me",width=10,height=2,command=self.display)
        self.b.place(x=80,y=200)

    def display(self):
        self.f1=Frame(width=900,height=840,bg="yellow")
        self.f1.propagate(0)
        
        self.f1.place(x=800,y=0)
        self.img = PhotoImage(file="bec.webp")

        # Create a Label Widget to display the text or Image
        self.label = Label(self.f1, image = self.img)
        self.label.pack()
        #self.l=Label(self.f1,font=("new Time",6,"bold"),bg="yellow")
        # self.l.place(x=70,y=100)
root=Tk()
M=interface(root)
root.mainloop()