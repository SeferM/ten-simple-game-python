from tkinter import *
import os
class FaceLock(Toplevel):
    def __init__(self):
        super(FaceLock,self).__init__()
        self.THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        self.my_file = os.path.join(self.THIS_FOLDER, r'img/Lock.png')
        self.photo = PhotoImage(file=self.my_file)
        self.photoimage = self.photo.subsample(2, 2)

        self.my_file2 = os.path.join(self.THIS_FOLDER, r'img/unLock.png')
        self.photo2 = PhotoImage(file=self.my_file2)
        self.photoimage2 = self.photo2.subsample(2, 2)

        self.my_file3 = os.path.join(self.THIS_FOLDER, r'img/emtyfoto.png')
        self.photo3 = PhotoImage(file=self.my_file3)
        self.photoimage3 = self.photo3.subsample(2, 2)

        self.my_file4 = os.path.join(self.THIS_FOLDER, r'img/webcamfoto1zenci.png')
        self.photo4 = PhotoImage(file=self.my_file4)
        self.photoimage4 = self.photo4.subsample(2, 2)

        self.yerlestir()
    def lock(self):
        self.bottomCanvas.delete("all")
        self.bottomCanvas.config(bg="red")
        self.bottomCanvas.create_image(150,100,image=self.photoimage)
        self.topCanvas.delete("all")
        self.topCanvas.create_image(150,100,image=self.photoimage3)

    def unlock(self):
        self.bottomCanvas.delete("all")
        self.bottomCanvas.config(bg="green")
        self.bottomCanvas.create_image(150,100,image=self.photoimage2)
        self.topCanvas.delete("all")
        self.topCanvas.create_image(150,100, image=self.photoimage4)

    def yerlestir(self):
        self.topCanvas=Canvas(self,width=300,height=200,bg="red")
        self.topCanvas.pack()
        self.topCanvas.create_image(150,100,image=self.photoimage3)

        self.enterButton=Button(self,text="Kilidi aç",command=self.unlock )
        self.enterButton.pack()

        self.exitButton=Button(self,text="Kilitle",command=self.lock)
        self.exitButton.pack()

        self.bottomCanvas=Canvas(self,width=300,height=200,bg="red")
        self.bottomCanvas.create_image(150,100,image=self.photoimage)
        self.bottomCanvas.pack()

        self.minsize(300,400)

if __name__ == '__main__':
    app=FaceLock()
    app.mainloop()