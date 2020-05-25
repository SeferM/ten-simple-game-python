from tkinter import *
import os
import random
class Snap(Toplevel):
    def __init__(self):
        super(Snap,self).__init__()

        self.THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

        self.canvasl=Canvas(self,width=200,height=200, bg="red")
        self.canvasl.grid(row=0,column=0)

        self.label=Label(self,text="")
        self.label.grid(row=0, column=1,columnspan=2)

        self.canvasr=Canvas(self,width=200,height=200, bg="blue")
        self.canvasr.grid(row=0,column=3)


        self.my_fileKaro = os.path.join(self.THIS_FOLDER, 'img\-karoP.png')
        self.photoKaro = PhotoImage(file=self.my_fileKaro)
        self.photoimageKaro = self.photoKaro.subsample(3, 3)
        self.karoButton=Button(self,text="Karo",image=self.photoimageKaro,command=lambda :self.oyna('img\-karoP.png',1))
        self.karoButton.grid(row=1,column=0)

        self.my_fileKupa = os.path.join(self.THIS_FOLDER, 'img\-kupaP.png')
        self.photoKupa = PhotoImage(file=self.my_fileKupa)
        self.photoimageKupa = self.photoKupa.subsample(3, 3)
        self.kupaButton = Button(self, text="Kupa",image=self.photoimageKupa,command=lambda :self.oyna('img\-kupaP.png',2))
        self.kupaButton.grid(row=1,column=1)

        self.my_fileMaca = os.path.join(self.THIS_FOLDER, 'img\-macoP.png')
        self.photoMaca = PhotoImage(file=self.my_fileMaca)
        self.photoimageMaca = self.photoMaca.subsample(3, 3)
        self.macaButton = Button(self, text="Maça",image=self.photoimageMaca,command=lambda :self.oyna('img\-macoP.png',3))
        self.macaButton.grid(row=1,column=2)

        self.my_fileSinek = os.path.join(self.THIS_FOLDER, 'img\-sinekP.png')
        self.photoSinek = PhotoImage(file=self.my_fileSinek)
        self.photoimageSinek = self.photoSinek.subsample(3, 3)
        self.sinekButton = Button(self, text="Sinek",image=self.photoimageSinek, command=lambda :self.oyna('img\-sinekP.png',4))
        self.sinekButton.grid(row=1,column=3)

    def oyna(self,text,i):
        self.canvasl.delete("all")
        self.canvasr.delete("all")
        self.my_file = os.path.join(self.THIS_FOLDER, text)
        self.photo = PhotoImage(file=self.my_file)
        self.photoimage = self.photo.subsample(2, 2)
        self.canvasl.create_image(100,100,image=self.photoimage)
        self.random=round(random.uniform(1,4))
        if self.random==1:
            self.my_filer = os.path.join(self.THIS_FOLDER, 'img\-karoB.png')
            self.photor = PhotoImage(file=self.my_filer)
            self.photoimage = self.photor.subsample(2, 2)
            self.canvasr.create_image(100, 100, image=self.photoimager)
            if i==1:
                self.label.config(text="SNAP!!!")
            else:
                self.label.config(text="NEXT!")
        elif self.random==2:
            self.my_filer = os.path.join(self.THIS_FOLDER, 'img\-kupaB.png')
            self.photor = PhotoImage(file=self.my_filer)
            self.photoimager = self.photor.subsample(2, 2)
            self.canvasr.create_image(100, 100, image=self.photoimager)
            if i==2:
                self.label.config(text="SNAP!!!")
            else:
                self.label.config(text="NEXT!")
        elif self.random==3:
            self.my_filer = os.path.join(self.THIS_FOLDER, 'img\-macoB.png')
            self.photor = PhotoImage(file=self.my_filer)
            self.photoimager = self.photor.subsample(2, 2)
            self.canvasr.create_image(100, 100, image=self.photoimager)
            if i==3:
                self.label.config(text="SNAP!!!")
            else:
                self.label.config(text="NEXT!")
        elif self.random==4:
            self.my_filer = os.path.join(self.THIS_FOLDER, 'img\-sinepB.png')
            self.photor = PhotoImage(file=self.my_filer)
            self.photoimager = self.photor.subsample(2, 2)
            self.canvasr.create_image(100, 100, image=self.photoimager)
            if i==4:
                self.label.config(text="SNAP!!!")
            else:
                self.label.config(text="NEXT!")

if __name__ == '__main__':
    app=Snap()
    app.mainloop()