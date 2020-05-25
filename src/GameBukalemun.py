from tkinter import *
import os
class Bukalemun(Toplevel):
    def __init__(self):
        super(Bukalemun,self).__init__()
        self.title("Bukalemun")
        self.create()

    def create(self):
        self.canvas=Canvas(self,width=300,height=300)
        self.canvas.pack()
        self.THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        self.my_file = os.path.join(self.THIS_FOLDER, 'img\emtyfoto.png')
        self.photo = PhotoImage(file=self.my_file)
        self.photoimage = self.photo.subsample(2, 2)

        self.canvas.create_image(150,150,image=self.photoimage)

        self.buka_file = os.path.join(self.THIS_FOLDER, 'img\-bukalemunDiscephe.png')
        self.bukaimg = PhotoImage(file=self.buka_file)
        self.bukaimage = self.bukaimg.subsample(2, 2)

        self.canvas.create_image(150,150,image=self.bukaimage)

        self.button= Button(self, text="Fotoğraf değitir",command=self.change)
        self.button.pack()
        self.i=0
    def change(self):
        self.canvas.delete("all")
        if self.i%2==0:
            self.my_file = os.path.join(self.THIS_FOLDER, 'img\-blackimg.png')
            self.photo = PhotoImage(file=self.my_file)
            self.photoimage = self.photo.subsample(2, 2)
            self.canvas.create_image(150,150,image=self.photoimage)

            self.buka_file = os.path.join(self.THIS_FOLDER, 'img\-bukalemunBlack.png')
            self.bukaimg = PhotoImage(file=self.buka_file)
            self.bukaimage = self.bukaimg.subsample(2, 2)

            self.after(1000,lambda :self.canvas.create_image(150, 150, image=self.bukaimage))
        else:
            self.my_file = os.path.join(self.THIS_FOLDER, 'img\-redimage.png')
            self.photo = PhotoImage(file=self.my_file)
            self.photoimage = self.photo.subsample(2, 2)
            self.canvas.create_image(150, 150, image=self.photoimage)

            self.buka_file = os.path.join(self.THIS_FOLDER, 'img\-bukalemunRed.png')
            self.bukaimg = PhotoImage(file=self.buka_file)
            self.bukaimage = self.bukaimg.subsample(2, 2)

            self.after(1000, lambda: self.canvas.create_image(150, 150, image=self.bukaimage))




        self.i += 1
if __name__ == '__main__':
    app=Bukalemun()
    app.mainloop()