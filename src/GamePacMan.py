from tkinter import *
import os,time,random

class PacMan(Toplevel):

    def __init__(self):

        super(PacMan,self).__init__()
        self.title("MakeMeHappy")
        self.table()
        self.character(70,85,190,185)
        self.kirmizix=190
        self.kirmiziy=185
        self.btn=Button(self,text="başla",command = lambda:self.move(1,70,85,0))
        self.btn.pack()
        self.btnnew=Button(self, text="yeni oyun", command= lambda :self.kirmizikonum(random.uniform(10,15)*20))
        self.btnnew.pack()

    def kirmizikonum(self,yk):
        self.pacmanKirmiziImg.place(x=190,y=yk)
        self.kirmiziy=yk
    def table(self):
        self.canvas = Canvas(self,width=300,height=300)
        self.canvas.pack()
        for i in range(16):
            self.canvas.create_line(i*20,0,i*20,300,fill="black")
            self.canvas.create_line(0,i*20,300,i*20,fill="black")

        self.minsize(400, 400)

    def character(self, xp, yp, xk, yk):
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

        my_file1 = os.path.join(THIS_FOLDER, 'img\pacmanirmiziimg.png')
        self.photo1 = PhotoImage(file=my_file1)
        self.photoimage1 = self.photo1.subsample(3, 3)
        self.pacmanKirmiziImg = Label(self, image=self.photoimage1)
        self.pacmanKirmiziImg.place(x=xk, y=yk)

        my_file = os.path.join(THIS_FOLDER, 'img\pacmanimg.png')
        self.photo = PhotoImage(file=my_file)
        self.photoimage = self.photo.subsample(3, 3)
        self.pacmanImg=Label(self, image=self.photoimage)
        self.pacmanImg.place(x=xp, y=yp)



    def move(self, mode, xp, yp, time):
        if(mode==1 and self.kirmizix>xp):
            self.pacmanImg.place(x=xp, y=yp)
            self.after(400, lambda: self.move(1, xp+20, yp, time+1))
        elif(mode==1 and self.kirmiziy>=yp):
            self.pacmanImg.place(x=xp, y=yp)
            self.after(400, lambda : self.move(1, xp, yp+20, time+1))
        else:
            pass

if __name__ == '__main__':
    app=PacMan()
    app.mainloop()