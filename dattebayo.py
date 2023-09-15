from tkinter import *
root=Tk()
def framing():
    f=Frame(root,width=500,height=1000,bg="blue")
    f.propagate(0)
    f.place(x=0,y=900)
    Label(f,text="labeling").pack(padx=20,pady=30)
def framing2():
    f1=Frame(root,width=500,height=1000,bg="yellow")
    f1.propagate(0)
    f1.place(x=600,y=900)
    Label(f1,text="labeling").pack(padx=20,pady=20)

Button(root,text="lets go",command=framing).pack()
Button(root,text="frame 2",command=framing2).pack()
root.geometry("800x800")
root.mainloop()