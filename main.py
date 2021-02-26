from tkinter import *
from PIL import Image, ImageTk
from PIL import Image
from PIL import ImageTk
import pandas as pd
import random
import tkinter
import tkinter.font as font



import time
def bg_colour():
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    r=177
    g=221
    b=198
    return f'#{r:02x}{g:02x}{b:02x}'

class myGUI(object):
    def __init__(self):
        self.filename="data/french_words.csv"
        self.df = pd.read_csv(self.filename,header=0)
        self.df_dict = self.df.to_dict('split')
        self.df_dict=self.df_dict['data']
        
        self.master=tkinter.Tk()
        self.master.title("Flashy")
        self.master.geometry("900x676")
        self.master.resizable(width=0, height=0)
        self.master.configure(bg=bg_colour())
        self.canvas = tkinter.Canvas(self.master,width = 750, height = 400,bg=bg_colour(),highlightthickness=0)
        self.canvas.pack(expand = tkinter.YES, fill = tkinter.BOTH)
        
    
        right = tkinter.PhotoImage(file="images/right.png")
        wrong = tkinter.PhotoImage(file="images/wrong.png")
        self.img = ImageTk.PhotoImage(file = "images/card_front.png")
        
        button_qwer1 = tkinter.Button(self.master,image=wrong,highlightthickness=0,command=self.onWrong).pack(side=tkinter.LEFT,padx=187)
        button_qwer2 = tkinter.Button(self.master,image=right,highlightthickness=0,command=self.onRight).pack(padx=10)
        self.display()
    def display(self):
        self.data = self.get_word()

        #Front card
        self.canvas_img=self.canvas.create_image(50, 50, image = self.img,anchor='nw') 
        img1 = ImageTk.PhotoImage(file = "images/card_front.png") 
        self.canvas.itemconfig(self.canvas_img,image=img1)
        self.canvas.photo = img1
        self.canvas.delete("test1")
        self.canvas.create_text(400, 200, text = "French",tag="test1",font=("Arial", 40,'italic'))
        self.canvas.create_text(400, 313, text = self.data[0][0],tag="test1",font=("Arial", 60,'bold'))
#     time.sleep(10)
#         id_=master.after(3000,after_3s(data))
#         create_image(250, 250, image=self.photo)
        self.master.after(3000, self.after_3s)
        self.master.mainloop()
    def get_word(self):
        select = int(random.randint(0,len(self.df_dict)-1))
        result = self.df_dict[select]
        return result,select
    def after_3s(self):
        filename = "images/card_back.png"
        image = Image.open(filename)
        self.photo = ImageTk.PhotoImage(image)
        self.canvas.itemconfig(self.canvas_img, image=self.photo)
        self.canvas.delete("test1")
        self.canvas.create_text(400, 200, text = "English",tag="test1",font=("Arial", 40,'italic'))
        self.canvas.create_text(400, 313, text = self.data[0][1],tag="test1",font=("Arial", 60,'bold'))
#         myFont = font.Font(family='Helvetica', size=50, weight='bold')
#         self.canvas['font'] = myFont
    def onWrong(self):
        self.display()
        print("Try again")


    def onRight(self):
        print(self.df_dict.pop(self.data[1]))
#         print(self.df_dict)
        self.display()



if __name__ == "__main__":
    gui = myGUI()


