from tkinter import *
import os
import random
class RockPaperScissors(Toplevel):
    def __init__(self):
        super(RockPaperScissors,self).__init__()

        self.THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

        self.canvasl=Canvas(self,width=200,height=200, bg="red")
        self.canvasl.grid(row=0,column=0)

        self.label=Label(self,text="")
        self.label.grid(row=0, column=1,columnspan=2)

        self.canvasr=Canvas(self,width=200,height=200, bg="blue")
        self.canvasr.grid(row=0,column=3)


        self.my_filer = os.path.join(self.THIS_FOLDER, 'img\-tas.png')
        self.photor = PhotoImage(file=self.my_filer)
        self.photoimager = self.photor.subsample(3, 3)
        self.rockButton=Button(self,text="Rock",image=self.photoimager,command=lambda :self.oyna('img\-tas.png',1))
        self.rockButton.grid(row=1,column=0)

        self.my_filep = os.path.join(self.THIS_FOLDER, 'img\-kagit.png')
        self.photop = PhotoImage(file=self.my_filep)
        self.photoimagep = self.photop.subsample(3, 3)
        self.paperButton = Button(self, text="Paper",image=self.photoimagep,command=lambda :self.oyna('img\-kagit.png',2))
        self.paperButton.grid(row=1,column=1,columnspan=2)

        self.my_files = os.path.join(self.THIS_FOLDER, 'img\-makas.png')
        self.photos = PhotoImage(file=self.my_files)
        self.photoimages = self.photos.subsample(3, 3)
        self.scissorsButton = Button(self, text="Scissors",image=self.photoimages, command=lambda :self.oyna('img\-makas.png',3))
        self.scissorsButton.grid(row=1,column=3)

    def oyna(self,index,t):
        self.canvasr.delete("all")
        self.canvasl.delete("all")
        self.my_filelc = os.path.join(self.THIS_FOLDER, index)
        self.photolc = PhotoImage(file=self.my_filelc)
        self.photoimagelc = self.photolc.subsample(3, 3)
        self.canvasl.create_image(100,100,image=self.photoimagelc)

        self.random=round(random.uniform(1,3))
        if self.random==1:
            self.my_file1 = os.path.join(self.THIS_FOLDER, 'img\-tas.png')
            self.photo1 = PhotoImage(file=self.my_file1)
            self.photoimage1 = self.photo1.subsample(3, 3)
            self.canvasr.create_image(100, 100, image=self.photoimage1)
            if t==1:
                self.label.config(text="Berabere")
            elif t==2:
                self.label.config(text="Kazandın")
            elif t==3:
                self.label.config(text="Kaybettin")
        elif self.random==2:
            self.my_file2 = os.path.join(self.THIS_FOLDER, 'img\-makas.png')
            self.photo2 = PhotoImage(file=self.my_file2)
            self.photoimage2 = self.photo2.subsample(3, 3)
            self.canvasr.create_image(100, 100, image=self.photoimage2)
            if t==1:
                self.label.config(text="Kazandın")
            elif t==2:
                self.label.config(text="Kaybettin")
            elif t==3:
                self.label.config(text="Berabere")
        elif self.random==3:
            self.my_file3 = os.path.join(self.THIS_FOLDER, 'img\-kagit.png')
            self.photo3 = PhotoImage(file=self.my_file3)
            self.photoimage3 = self.photo3.subsample(3, 3)
            self.canvasr.create_image(100, 100, image=self.photoimage3)
            if t==1:
                self.label.config(text="Kaybettin")
            elif t==2:
                self.label.config(text="Berabere")
            elif t==3:
                self.label.config(text="Kazandın")

if __name__ == '__main__':
    app=RockPaperScissors()
    app.mainloop()