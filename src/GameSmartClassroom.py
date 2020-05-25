from tkinter import *
import os
import tkinter.messagebox
class SmartClassroom(Toplevel):
    def __init__(self):
        super(SmartClassroom,self).__init__()
        self.canvas=Canvas(self,width=300,height=200,bg="black")
        self.canvas.pack()

        self.canvas.create_text(150,100,fill="white",text="light_on")

        self.entry=Entry(self)
        self.entry.pack(side="left",fill="both",expand="true")

        self.button=Button(self,text="Enter",command=lambda :self.control(self.entry.get()))
        self.button.pack(side="right")
    def control(self,text):
        if text=="light_on":
            self.canvas.delete("all")
            self.THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
            self.my_file9 = os.path.join(self.THIS_FOLDER, 'img\light.png')
            self.photo9 = PhotoImage(file=self.my_file9)
            self.photoimage9 = self.photo9.subsample(2, 2)
            self.canvas.create_image(150,100,image=self.photoimage9)
            self.canvas.create_text(150,150,fill="white",text="light_off")
        elif text=="light_off":
            self.canvas.delete("all")
            self.canvas.create_text(150, 100, fill="white", text="light_on")
        else:
            tkinter.messagebox.showinfo("Uyarı","Lütfen geçerli bir komut giriniz.Örn:'light_on veya light_off'")


if __name__ == '__main__':
    app=SmartClassroom()
    app.mainloop()