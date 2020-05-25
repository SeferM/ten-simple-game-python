from tkinter import *
import os
import time
class GameEmojiMask(Toplevel):

    def __init__(self):
        super(GameEmojiMask,self).__init__()

        self.THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        self.my_file = os.path.join(self.THIS_FOLDER, 'img\emtyfoto.png')
        self.photo = PhotoImage(file=self.my_file)
        self.photoimage = self.photo.subsample(2, 2)
        self.drawscreen()
    def smileyerlestir(self,text):
        self.phototext=text.subsample(3,3)
        self.lbl=Label(self,width=40,height=42,image=self.phototext)
        self.lbl['bg']=self.img['bg']
        self.lbl.place(x=223,y=40)
    def fotocek(self):
        self.my_file=os.path.join(self.THIS_FOLDER,'img\webcamfoto1zenci.png')
        self.photo=PhotoImage(file=self.my_file)
        self.photoimage = self.photo.subsample(2, 2)
        self.img.config(image=self.photoimage)
    def drawscreen(self):
        self.title("Emoji mask")
        self.my_file0 = os.path.join(self.THIS_FOLDER, 'img\emtyfoto.png')
        self.photo0 = PhotoImage(file=self.my_file0)
        self.photoimage0 = self.photo0.subsample(2, 2)
        self.img = Label(self, image=self.photoimage0)
        self.img.pack()
        self.btn=Button(self, text="Fotoğraf çekin", command=self.fotocek)
        self.btn.pack()
        self.txt=Label(self,text="Maske seçiniz")
        self.txt.place(x=410,y=20)



        self.my_file1 = os.path.join(self.THIS_FOLDER,'img\smile1.png')
        self.photo1 = PhotoImage(file=self.my_file1)
        self.photoimage1 = self.photo1.subsample(2, 2)
        self.mask1 = Button(self,width=100, height=100, image=self.photoimage1,command= lambda :self.smileyerlestir(self.photo1))
        self.mask1.place(x=400,y=50)

        self.my_file2 = os.path.join(self.THIS_FOLDER,'img\smile2.png')
        self.photo2 = PhotoImage(file=self.my_file2)
        self.photoimage2 = self.photo2.subsample(2, 2)
        self.mask2 = Button(self,width=100, height=100, image=self.photoimage2,command= lambda :self.smileyerlestir(self.photo2))
        self.mask2.place(x=400,y=160)

        self.my_file3 = os.path.join(self.THIS_FOLDER,'img\cry.png')
        self.photo3 = PhotoImage(file=self.my_file3)
        self.photoimage3 = self.photo3.subsample(2, 2)
        self.mask3 = Button(self,width=100, height=100, image=self.photoimage3,command= lambda :self.smileyerlestir(self.photo3))
        self.mask3.place(x=400,y=270)
        self.minsize(500,400)
if __name__ == '__main__':
    app=GameEmojiMask()
    app.mainloop()