import pygame
import random

pygame.init()
Window=pygame.display.set_mode((500,500),pygame.RESIZABLE)  
Vars={}
Vars["WinSize"]=pygame.display.get_window_size() 
Vars["time"]=0
Vars["running"]=True
Vars["pos"]=[Vars["WinSize"][0]/2-(Vars["WinSize"][0]/20)+1,1]
Vars["shape"]=""
Vars["structure"]=[]
Vars["square"]=[(Vars["WinSize"][0]/20),(Vars["WinSize"][1]/20)]
for i in range(20):
    Vars["structure"].append([0,0,0,0,0,0,0,0,0,0])
Vars["size"]=[0,0]
Vars["IDK"]=[]
Vars["xy"]=[5,19]
clock=pygame.time.Clock()


class shape:
    def __init__(self,shape,color,pos):
        
        drawing(shape,color,pos)

def screen():
    Vars["WinSize"]=pygame.display.get_window_size() 
    pygame.draw.rect(Window,"red",[Vars["WinSize"][0]/4,0,Vars["WinSize"][0]/2,Vars["WinSize"][1]],1)
    
def keyboard(key):
    if key==pygame.K_ESCAPE:
        Vars["running"]=False
    if key==pygame.K_a:
        if Vars["pos"][0]>(Vars["WinSize"][0]/4)+1:
            Window.fill("black",((Vars["WinSize"][0]/4)+1,1,(Vars["WinSize"][0]/2)-2,Vars["WinSize"][1]-2))
            Vars["pos"][0]-=Vars["square"][0]
            drawing(Vars["shape"],"blue",Vars["pos"])
            Vars["xy"][0]-=1
    if key==pygame.K_d:
        if Vars["pos"][0]+(Vars["square"][0]*Vars["size"][1])<(Vars["WinSize"][0]*0.75)+1:
            Window.fill("black",((Vars["WinSize"][0]/4)+1,1,(Vars["WinSize"][0]/2)-2,Vars["WinSize"][1]-2))
            Vars["pos"][0]+=Vars["square"][0]
            drawing(Vars["shape"],"blue",Vars["pos"])
            Vars["xy"][0]+=1

def move():
    if Vars["pos"][1] +(Vars["square"][1]*len(Vars["IDK"])) < Vars["WinSize"][1]:
        Window.fill("black",((Vars["WinSize"][0]/4)+1,1,(Vars["WinSize"][0]/2)-2,Vars["WinSize"][1]-2))
        Vars["pos"][1]+=Vars["WinSize"][1]/20
        drawing(Vars["shape"],"blue",Vars["pos"])
        Vars["time"]=0
        Vars["xy"][1]+=1
    else:
        update_structure()
        setup_shape()
        

def drawing(shape,color,pos):
    Vars["shape"]=shape
    if Vars["shape"]=="square":
        for i in range(len(Vars["IDK"])):
            for j in range(len(Vars["IDK"][0])):
                if Vars["IDK"][i][j]==1:
                    pygame.draw.rect(Window,color,[pos[0]+(Vars["square"][0]*j),pos[1]+(Vars["square"][1]*i),(Vars["square"][0])-2,(Vars["square"][1])-2],1)
    
    elif Vars["shape"]=="L":    
        for i in range(len(Vars["IDK"])):
            for j in range(len(Vars["IDK"][0])):
                if Vars["IDK"][i][j]==1:
                    pygame.draw.rect(Window,color,[pos[0]+(Vars["square"][0]*j),pos[1]+(Vars["square"][1]*i),(Vars["square"][0])-2,(Vars["square"][1])-2],1)
    
    elif Vars["shape"]=="RL":
        for i in range(len(Vars["IDK"])):
            for j in range(len(Vars["IDK"][0])):
                if Vars["IDK"][i][j]==1:
                    pygame.draw.rect(Window,color,[pos[0]+(Vars["square"][0]*j),pos[1]+(Vars["square"][1]*i),(Vars["square"][0])-2,(Vars["square"][1])-2],1)
    
    elif Vars["shape"]=="Triangle":    
        for i in range(len(Vars["IDK"])):
            for j in range(len(Vars["IDK"][0])):
                if Vars["IDK"][i][j]==1:
                    pygame.draw.rect(Window,color,[pos[0]+(Vars["square"][0]*j),pos[1]+(Vars["square"][1]*i),(Vars["square"][0])-2,(Vars["square"][1])-2],1)
    
    elif Vars["shape"]=="Stick":
        for i in range(len(Vars["IDK"])):
            pygame.draw.rect(Window,color,[pos[0],pos[1]+(Vars["square"][1]*i),(Vars["square"][0])-2,(Vars["square"][1])-2],1)
    
    structure()
    
def struct():
    Vars["IDK"].clear()
    if Vars["shape"]=="square":
        Vars["size"]=[2,2]
        Vars["IDK"].append([1,1])
        Vars["IDK"].append([1,1])
    elif Vars["shape"]=="L":
        Vars["size"]=[3,2]
        Vars["IDK"].append([1,0])
        Vars["IDK"].append([1,0])
        Vars["IDK"].append([1,1])
    elif Vars["shape"]=="RL":
        Vars["size"]=[3,2]
        Vars["IDK"].append([0,1])
        Vars["IDK"].append([0,1])
        Vars["IDK"].append([1,1])
    elif Vars["shape"]=="Triangle":
        Vars["size"]=[2,3]
        Vars["IDK"].append([0,1,0])
        Vars["IDK"].append([1,1,1])
    elif Vars["shape"]=="Stick":
        Vars["size"]=[4,1]
        Vars["IDK"].append([1])
        Vars["IDK"].append([1])
        Vars["IDK"].append([1])
        Vars["IDK"].append([1])
def update_structure():
    x=1
    for i in range(len(Vars["IDK"])):
        for j in range(len(Vars["IDK"][0])):
            if Vars["IDK"][i][j]==1:
                Vars["structure"][Vars["xy"][0]]
    
def structure():
    for i in range(20):
        for j in range(10):
            if Vars["structure"][i][j]==1:
                pygame.draw.rect(Window,"Blue",((Vars["WinSize"][0]/4)+(Vars["WinSize"][0]/20*j)+1,i*(Vars["WinSize"][1]/20)+1,(Vars["WinSize"][0]/20)-2,(Vars["WinSize"][1]/20)-2),1)
    
        
def setup_shape():
    shapes=["square","L","RL","Triangle","Stick"]
    Vars["shape"]=random.choice(shapes)
    struct()
    Vars["pos"]=[Vars["WinSize"][0]/2-(Vars["WinSize"][0]/20)+1,1]
    drawing(Vars["shape"],"blue",Vars["pos"])
    
screen()


setup_shape()
while Vars["running"] == True:
    WinSize=pygame.display.get_window_size()
    
    Vars["time"]+=1
    if Vars["time"]>50:
        move()
    for event in pygame.event.get():
        #print(event)
        print(event)
        if event.type == pygame.QUIT:
            Vars["running"]=False
        if event.type == pygame.KEYDOWN:
            keyboard(event.key)
        if event.type==pygame.VIDEORESIZE:
            screen()
            

        
    
    pygame.display.update()
    clock.tick(60)