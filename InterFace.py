from tkinter import *
from src.GameMakeMeHappy import MakeMeHappy
from src.EmojiMask import GameEmojiMask
from src.GameFaceLock import FaceLock
from src.GamePacMan import PacMan
from src.GameChatBot import chatty
from src.GameTicTacToe import TicTacToe
from src.GameBukalemun import Bukalemun
from src.GameRockPaperScissors import RockPaperScissors
from src.GameSmartClassroom import SmartClassroom
from src.GameSnap import Snap
import os

class App(Tk):
    def __init__(self):
        super(App,self).__init__()

        self.title("Ten Game")
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(THIS_FOLDER, 'src\img\smileGame1icon.png')
        # +game1
        # -game1 icon
        self.photo = PhotoImage(file=my_file)
        self.photoimage = self.photo.subsample(2, 2)
        # -game1 button
        self.game1=Button(self, text="game1", width=150, height=150, image =self.photoimage, command=MakeMeHappy)
        self.game1.place(x=100, y=100)
        # -game1 text
        self.text1=Label(self, text="Make smile")
        self.text1.place(x=140, y=270)

        #game2
        # -game2 icon
        # -game2 button
        self.game2 = Button(self, text="game2", width=150, height=150, image =self.photoimage, command=GameEmojiMask)
        self.game2.place(x=300, y=100)
        # -game2 text
        self.text2 = Label(self, text="Emoji Mask")
        self.text2.place(x=340, y=270)

        #game3
        # -game3 icon
        my_filefl = os.path.join(THIS_FOLDER, 'src\img\Lock.png')
        self.photofl = PhotoImage(file=my_filefl)
        self.photoimagefl = self.photofl.subsample(2, 2)
        # -game3 button
        self.game3 = Button(self, text="game3", width=150, height=150, image =self.photoimagefl, command=FaceLock)
        self.game3.place(x=500, y=100)
        # -game3 text
        self.text3 = Label(self, text="FaceLock")
        self.text3.place(x=540, y=270)

        # game4
        # -game4 icon
        my_filep = os.path.join(THIS_FOLDER, 'src\img\pacmanimg.png')
        self.photop = PhotoImage(file=my_filep)
        self.photoimagep = self.photop.subsample(2, 2)
        # -game4 button
        self.game4 = Button(self, text="game4", width=150, height=150, image =self.photoimagep, command=PacMan)
        self.game4.place(x=700, y=100)
        # -game4 text
        self.text4 = Label(self, text="PacMan")
        self.text4.place(x=740, y=270)

        # game5
        # -game5 icon
        my_filecb = os.path.join(THIS_FOLDER, 'src\img\chatboticon.png')
        self.photocb = PhotoImage(file=my_filecb)
        self.photoimagecb = self.photocb.subsample(3, 3)
        # -game5 button
        self.game5 = Button(self, text="game5", width=150, height=150, image =self.photoimagecb, command=chatty)
        self.game5.place(x=900, y=100)
        # -game5 text
        self.text5 = Label(self, text="ChatBot")
        self.text5.place(x=940, y=270)

        # +game6
        # -game6 icon
        my_filetc = os.path.join(THIS_FOLDER, 'src\img\-tictactoeicon.png')
        self.phototc = PhotoImage(file=my_filetc)
        self.photoimagetc = self.phototc.subsample(2, 2)
        # -game6 button
        self.game6 = Button(self, text="game1", width=150, height=150, image=self.photoimagetc, command=TicTacToe)
        self.game6.place(x=100, y=300)
        # -game6 text
        self.text6 = Label(self, text="Tic Tac Toe")
        self.text6.place(x=140, y=470)

        # game7
        # -game7 icon
        my_filebk = os.path.join(THIS_FOLDER, 'src\img\-bukalemunBlack.png')
        self.photobk = PhotoImage(file=my_filebk)
        self.photoimagebk = self.photobk.subsample(2, 2)
        # -game7 button
        self.game7 = Button(self, text="game2", width=150, height=150, image=self.photoimagebk, command=Bukalemun)
        self.game7.place(x=300, y=300)
        # -game7 text
        self.text7 = Label(self, text="Bukalemun")
        self.text7.place(x=340, y=470)

        # game8
        # -game8 icon
        my_filetk = os.path.join(THIS_FOLDER, 'src\img\icontaskagit.png')
        self.phototk = PhotoImage(file=my_filetk)
        self.photoimagetk = self.phototk.subsample(2, 2)
        # -game8 button
        self.game8 = Button(self, text="game3", width=150, height=150, image=self.photoimagetk, command=RockPaperScissors)
        self.game8.place(x=500, y=300)
        # -game8 text
        self.text8 = Label(self, text="Taş Kagıt Makas")
        self.text8.place(x=540, y=470)

        # game9
        # -game9 icon
        my_file9 = os.path.join(THIS_FOLDER, 'src\img\light.png')
        self.photo9 = PhotoImage(file=my_file9)
        self.photoimage9 = self.photo9.subsample(2, 2)
        # -game9 button
        self.game9 = Button(self, text="game4", width=150, height=150, image=self.photoimage9, command=SmartClassroom)
        self.game9.place(x=700, y=300)
        # -game9 text
        self.text9 = Label(self, text="Smart Classroom")
        self.text9.place(x=740, y=470)

        # game10
        # -game10 icon
        my_file10 = os.path.join(THIS_FOLDER, 'src\img\cardGameicon.png')
        self.photo10 = PhotoImage(file=my_file10)
        self.photoimage10 = self.photo10.subsample(4, 4)
        # -game10 button
        self.game10 = Button(self, text="game5", width=150, height=150, image=self.photoimage10, command=Snap)
        self.game10.place(x=900, y=300)
        # -game10 text
        self.text10 = Label(self, text="Snap")
        self.text10.place(x=940, y=470)

        self.minsize(1250,800)


if __name__ == '__main__':
    app=App()
    app.mainloop()