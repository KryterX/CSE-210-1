import random
import  tkinter as Tk
from tkinter import *
import Player
from turtle import  window_width
import Game
d = {}
d["score"] = 300
window_width=450
win_width=int(window_width)
win_height=window_width

def prog():
    root = Tk()
    root.geometry(f"{win_width}x{win_height}")  
    root.config(background="black") 
    d["pic{0}".format(5)] = Label(root,text="High Low",bd=20,highlightthickness=2)
    d["pic{0}".format(5)].config(highlightbackground="red",highlightcolor="red")
    d["pic{0}".format(5)].grid(row=0, column=2)   
    rand = random.randint(1,13)
    d["pic{0}".format(0)] = Label(root,text=f"{rand}",bd=20,highlightthickness=2,width=5)
    d["pic{0}".format(0)].config(highlightbackground="blue",highlightcolor="blue")
    d["pic{0}".format(0)].grid(row=1, column=1,rowspan=2,sticky="NS")
    
    d["but{0}".format(0)]= Button(root,text="🢁",padx=20,command=lambda highlow="high": Player.draw(highlow,root,d))
    d["but{0}".format(0)].grid(row=1,column=2,sticky="NS")
    d["but{0}".format(1)] = Button(root,text="🢃",padx=20,command=lambda highlow="low": Player.draw(highlow,root,d))
    d["but{0}".format(1)].grid(row=2,column=2,sticky="NS")
    
    d["pic{0}".format(2)] = Label(root,text="",bd=20,highlightthickness=2,width=5)
    d["pic{0}".format(2)].config(highlightbackground="blue",highlightcolor="blue")
    d["pic{0}".format(2)].grid(row=1, column=3,rowspan=2,sticky="NS")
    score=int(d["score"])
    d["pic{0}".format(3)] = Label(root,text=f"score = {score}",bd=20,highlightthickness=2,pady=5)
    d["pic{0}".format(3)].config(highlightbackground="orange",highlightcolor="orange")
    d["pic{0}".format(3)].grid(row=3, column=2)
    d["pic{0}".format(4)] = Label(root,text="Welcome to High Low",bd=20,highlightthickness=2)
    d["pic{0}".format(4)].config(highlightbackground="black",highlightcolor="black",width=15,height=1)
    d["pic{0}".format(4)].grid(row=4, column=2)
    for i in range(5): 
        Grid.rowconfigure(root,i,weight=1)
        Grid.columnconfigure(root,i,weight=1)
        
    root.update()
    Game.pause(1)
    d["pic4"].config(text="Will the next card be\n higher or lower?")    
    
    root.mainloop()


    
    
    


                 
if __name__ == "__main__":
    prog()