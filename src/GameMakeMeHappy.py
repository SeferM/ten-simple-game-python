from tkinter import *
import os

class MakeMeHappy(Toplevel):

    def __init__(self):

        super(MakeMeHappy,self).__init__()

        self.title("MakeMeHappy")

        #emoji
        self.THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        self.my_file = os.path.join(self.THIS_FOLDER, 'img\smile1.png')
        self.photo = PhotoImage(file=self.my_file)  # r"c:\projects\tenGame\src\img\smileGame1icon.png")
        self.photoimage = self.photo.subsample(2, 2)
        self.img = Label(self, width=300, height=200, image=self.photoimage)
        self.img.pack(side="top", fill=BOTH, expand=True)

        #textbox
        self.textbox = Entry(self)
        self.textbox.pack(side="left",fill=X, expand=True)

        #button
        self.btnSend = Button(self, width=10 , text="Say", command=self.say)
        self.btnSend.pack(side="right")

        self.minsize(500, 500)

    #
    def say(self):
        self.txt = self.textbox.get().lower()
        self.textbox.delete(0, 'end')
        self.spltTxt=self.txt.split(" ")
        #log
        print(self.spltTxt)

        for i in self.spltTxt:
            if(i=='güzel'  or i=='güzeller' or i=='yakışıklı' or i=='yakışıklısın' or i=='harikasın' or i=='harikasınız' or i=='zekisin' or i=='güzeldin'):
                self.my_file = os.path.join(self.THIS_FOLDER, 'img\smile2.png')
                self.photo = PhotoImage(file=self.my_file)
                self.photoimage = self.photo.subsample(2, 2)
                self.img.config(image=self.photoimage)
            elif(i=='salak'):
                self.my_file = os.path.join(self.THIS_FOLDER, r'img/anlamveremiyor.png')
                self.photo = PhotoImage(file=self.my_file)
                self.photoimage = self.photo.subsample(2, 2)
                self.img.config(image=self.photoimage)
            elif(i=='çirkinsin' or i=='çirkinlik'):
                self.my_file = os.path.join(self.THIS_FOLDER, 'img\cry.png')
                self.photo = PhotoImage(file=self.my_file)
                self.photoimage = self.photo.subsample(2, 2)
                self.img.config(image=self.photoimage)
            elif(i=='harikasın' or i=='muhteşemsin' or i=='temel' or i=='dursun'):
                self.my_file = os.path.join(self.THIS_FOLDER, 'img\happy.png')
                self.photo = PhotoImage(file=self.my_file)
                self.photoimage = self.photo.subsample(2, 2)
                self.img.config(image=self.photoimage)
            else:
                self.my_file = os.path.join(self.THIS_FOLDER, 'img\smile1.png')
                self.photo = PhotoImage(file=self.my_file)
                self.photoimage = self.photo.subsample(2, 2)
                self.img.config(image=self.photoimage)


        





if __name__ == '__main__':
    app=MakeMeHappy()
    app.mainloop()