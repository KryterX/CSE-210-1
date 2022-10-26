import pygame
import random

pygame.init()
Window=pygame.display.set_mode((500,500),pygame.RESIZABLE)  
Vars={}
Vars["WinSize"]=pygame.display.get_window_size() 
Vars["time"]=0
Vars["running"]=True
Vars["pos"]=[Vars["WinSize"][0]/2-(Vars["WinSize"][0]/20)+1,1]
Vars["grid"]=[Vars["WinSize"][0]/20,Vars["WinSize"][1]/20]
Vars["shape"]=""
Vars["color"]=""
Vars["structure"]=[]
Vars["structure_color"]=[]
Vars["square"]=[(Vars["WinSize"][0]/20),(Vars["WinSize"][1]/20)]
for i in range(20):
    Vars["structure"].append([0,0,0,0,0,0,0,0,0,0])
    Vars["structure_color"].append(["","","","","","","","","",""])
Vars["size"]=[0,0]
Vars["orientation"]=[]
Vars["xy"]=[4,0]
Vars["shapes"]=["square","L","RL","Triangle","Stick","zig","zag"]
Vars["colors"]=["grey","purple","orange","yellow","blue","green","red"]
Vars["score"]=0
Vars["down"]=False
Vars["time_max"]=50
Vars["gameover"]=False
Vars["next_shape"]=random.choice(Vars["shapes"])
Vars["next_shape_orientation"]=[]
Vars["next_shape_color"]=""
clock=pygame.time.Clock()



class shape:
    def __init__(self,shape,color,pos):
        
        drawing(shape,color,pos)

def screen():
    Vars["WinSize"]=pygame.display.get_window_size() 
    pygame.draw.rect(Window,"white",[Vars["WinSize"][0]/4,0,Vars["WinSize"][0]/2,Vars["WinSize"][1]],1)
    Vars["grid"]=[Vars["WinSize"][0]/20,Vars["WinSize"][1]/20]
    
def keyboard(key):
    if key==pygame.K_ESCAPE:
        Vars["running"]=False
    if key==pygame.K_a:
        test=True
        for i in range(len(Vars["orientation"])):
            if Vars["structure"][Vars["xy"][1]+i][Vars["xy"][0]-1]==0:
                test=True
            else:
                test=False
        if Vars["pos"][0]>(Vars["WinSize"][0]/4)+1 and test==True:
            Window.fill("black",((Vars["WinSize"][0]/4)+1,1,(Vars["WinSize"][0]/2)-2,Vars["WinSize"][1]-2))
            Vars["pos"][0]-=Vars["square"][0]
            drawing()
            Vars["xy"][0]-=1
    if key==pygame.K_d:
        test=True
        for i in range(len(Vars["orientation"])):
            if Vars["xy"][0]+(len(Vars["orientation"][0]))<10:
                if Vars["orientation"][i][len(Vars["orientation"][0])-1]==1 and Vars["structure"][Vars["xy"][1]+(i)][Vars["xy"][0]+(len(Vars["orientation"][0]))]==0:
                    #if Vars["structure"][Vars["xy"][1]+i][Vars["xy"][0]+ len(Vars["orientation"][0])-1]==0:
                    test=True
                elif Vars["orientation"][i][len(Vars["orientation"][0])-1]==0:
                    test=True
                else:
                    test=False
                    print("here 1")
        if Vars["pos"][0]+(Vars["square"][0]*Vars["size"][1])<(Vars["WinSize"][0]*0.75)+1 and test==True:
            Window.fill("black",((Vars["WinSize"][0]/4)+1,1,(Vars["WinSize"][0]/2)-2,Vars["WinSize"][1]-2))
            Vars["pos"][0]+=Vars["square"][0]
            drawing()
            Vars["xy"][0]+=1
    if key==pygame.K_e:
        test=0
        for f in range(3):
            arr=[]
            for i in range(len(Vars["orientation"][0])):
                arr.append([])
            for j in range(len(Vars["orientation"])):
                for k in range(len(Vars["orientation"][0])):
            
                    if Vars["orientation"][j][k]==1:
                        arr[len(Vars["orientation"][0])-k-1].append(1)
                    else:
                        arr[len(Vars["orientation"][0])-k-1].append(0)
            if Vars["pos"][1] +(Vars["square"][1]*len(arr)) < Vars["WinSize"][1]:
                Vars["size"]=[len(arr),len(arr[0])]
                Vars["orientation"]=arr
                test=1
            while Vars["xy"][0] +(len(arr[0])) > 10:
                Vars["pos"][0]-=Vars["square"][0]
                Vars["xy"][0]-=1
        if test==1:
            Window.fill("black",((Vars["WinSize"][0]/4)+1,1,(Vars["WinSize"][0]/2)-2,Vars["WinSize"][1]-2))
            drawing()
    if key==pygame.K_s:
        Vars["down"]=True
        
    if key==pygame.K_SPACE:
        x=1
        
def keyup(key):
    if key==pygame.K_s:
        Vars["down"]=False

def move():
    test=True
    num=0
    for i in range(len(Vars["orientation"])-1):
        for j in range(len(Vars["orientation"][0])):
            if Vars["xy"][1]+len(Vars["orientation"])<20:
                if Vars["orientation"][i][j]==1 and Vars["orientation"][i+1][j]==0:
                    if Vars["structure"][Vars["xy"][1]+1+i][Vars["xy"][0]+j]==0 and test==True:
                        test=True
                    else:
                        test=False
        num=i
    if len(Vars["orientation"])>=2:
        num+=1
    for k in range(len(Vars["orientation"][0])):
        if Vars["xy"][1]+len(Vars["orientation"])<20 and Vars["orientation"][num][k]==1:
            if Vars["structure"][Vars["xy"][1]+1+num][Vars["xy"][0]+k]==0 and test==True:
                test=True
            else:
                test=False
              
    if Vars["pos"][1] +(Vars["square"][1]*len(Vars["orientation"])) < Vars["WinSize"][1] and test==True:
        Window.fill("black",((Vars["WinSize"][0]/4)+1,1,(Vars["WinSize"][0]/2)-2,Vars["WinSize"][1]-2))
        Vars["pos"][1]+=Vars["WinSize"][1]/20
        drawing()
        Vars["time"]=0
        Vars["xy"][1]+=1
    else:
        update_structure()
        setup_shape()
        

def drawing():
    for i in range(len(Vars["orientation"])):
        for j in range(len(Vars["orientation"][0])):
            if Vars["orientation"][i][j]==1:
                pygame.draw.rect(Window,Vars["color"],[Vars["pos"][0]+(Vars["square"][0]*j),Vars["pos"][1]+(Vars["square"][1]*i),(Vars["square"][0])-2,(Vars["square"][1])-2],3)
    
    structure()
    
def struct():
    Vars["orientation"].clear()
    Vars["next_shape_orientation"].clear()
    if Vars["shape"]=="square":
        Vars["color"]="grey"
        Vars["size"]=[2,2]
        Vars["orientation"].append([1,1])
        Vars["orientation"].append([1,1])
    elif Vars["shape"]=="L":
        Vars["color"]="purple"
        Vars["size"]=[3,2]
        Vars["orientation"].append([1,0])
        Vars["orientation"].append([1,0])
        Vars["orientation"].append([1,1])
    elif Vars["shape"]=="RL":
        Vars["color"]="orange"
        Vars["size"]=[3,2]
        Vars["orientation"].append([0,1])
        Vars["orientation"].append([0,1])
        Vars["orientation"].append([1,1])
    elif Vars["shape"]=="Triangle":
        Vars["color"]="yellow"
        Vars["size"]=[2,3]
        Vars["orientation"].append([0,1,0])
        Vars["orientation"].append([1,1,1])
    elif Vars["shape"]=="Stick":
        Vars["color"]="blue"
        Vars["size"]=[4,1]
        Vars["orientation"].append([1])
        Vars["orientation"].append([1])
        Vars["orientation"].append([1])
        Vars["orientation"].append([1])
    elif Vars["shape"]=="zig":
        Vars["color"]="green"
        Vars["size"]=[3,2]
        Vars["orientation"].append([1,0])
        Vars["orientation"].append([1,1])
        Vars["orientation"].append([0,1])
    elif Vars["shape"]=="zag":
        Vars["color"]="red"
        Vars["size"]=[3,2]
        Vars["orientation"].append([0,1])
        Vars["orientation"].append([1,1])
        Vars["orientation"].append([1,0])
    elif Vars["shape"]=="O":
        Vars["color"]="violet"
        Vars["size"]=[3,3]
        Vars["orientation"].append([1,1,1])
        Vars["orientation"].append([1,0,1])
        Vars["orientation"].append([1,1,1])
        
    if Vars["next_shape"]=="square":
        Vars["next_shape_color"]="grey"
        Vars["next_shape_orientation"].append([1,1])
        Vars["next_shape_orientation"].append([1,1])
    elif Vars["next_shape"]=="L":
        Vars["next_shape_color"]="purple"
        Vars["next_shape_orientation"].append([1,0])
        Vars["next_shape_orientation"].append([1,0])
        Vars["next_shape_orientation"].append([1,1])
    elif Vars["next_shape"]=="RL":
        Vars["next_shape_color"]="orange"
        Vars["next_shape_orientation"].append([0,1])
        Vars["next_shape_orientation"].append([0,1])
        Vars["next_shape_orientation"].append([1,1])
    elif Vars["next_shape"]=="Triangle":
        Vars["next_shape_color"]="yellow"
        Vars["next_shape_orientation"].append([0,1,0])
        Vars["next_shape_orientation"].append([1,1,1])
    elif Vars["next_shape"]=="Stick":
        Vars["next_shape_color"]="blue"
        Vars["next_shape_orientation"].append([1])
        Vars["next_shape_orientation"].append([1])
        Vars["next_shape_orientation"].append([1])
        Vars["next_shape_orientation"].append([1])
    elif Vars["next_shape"]=="zig":
        Vars["next_shape_color"]="green"
        Vars["next_shape_orientation"].append([1,0])
        Vars["next_shape_orientation"].append([1,1])
        Vars["next_shape_orientation"].append([0,1])
    elif Vars["next_shape"]=="zag":
        Vars["next_shape_color"]="red"
        Vars["next_shape_orientation"].append([0,1])
        Vars["next_shape_orientation"].append([1,1])
        Vars["next_shape_orientation"].append([1,0])
    elif Vars["next_shape"]=="O":
        Vars["next_shape_color"]="violet"
        Vars["next_shape_orientation"].append([1,1,1])
        Vars["next_shape_orientation"].append([1,0,1])
        Vars["next_shape_orientation"].append([1,1,1])
def update_structure():
    x=1
    for i in range(len(Vars["orientation"])):
        for j in range(len(Vars["orientation"][0])):
            if Vars["orientation"][i][j]==1:
                Vars["score"]+=1
                Vars["structure"][Vars["xy"][1]+(i)][Vars["xy"][0]+(j)]=1
                Vars["structure_color"][Vars["xy"][1]+(i)][Vars["xy"][0]+(j)]=Vars["color"]
    
    k=19
    while k>-1:
        if 0 not in Vars["structure"][k]:
            remove_line(k)
            Patch_structure(k)
        else:
            k-=1
    update_score()
    if Vars["xy"][1]==0:
        Vars["gameover"]=True
        font = pygame.font.SysFont(None,100)
        text = font.render("gameover", True, "white")
        #pygame.Surface.blit(text,((Vars["WinSize"][0]/4)*3,Vars["WinSize"][1]/10))
        Window.blit(text,((Vars["WinSize"][0]/6.2),Vars["WinSize"][1]/3))
    
def update_score():
    Window.fill("black",(((Vars["WinSize"][0]/4)*3)+1,1,(Vars["WinSize"][0]/4)-2,Vars["WinSize"][1]/8))
    font = pygame.font.SysFont(None,60)
    text = font.render(f'{Vars["score"]}', True, "white")
    Window.blit(text,((Vars["WinSize"][0]/4)*3.3,Vars["WinSize"][1]/20))
        
def Patch_structure(line):
    
    for i in reversed(range(line+1)):
        if i >0:
            Vars["structure"][i]=list(Vars["structure"][i-1])
            Vars["structure_color"][i]=list(Vars["structure_color"][i-1])
        else:
            Vars["structure"][i]=[0,0,0,0,0,0,0,0,0,0]
            Vars["structure_color"][i]=["","","","","","","","","",""]
        if i>=20:
            break
            
def remove_line(line):
    Vars["structure"][line]=[0,0,0,0,0,0,0,0,0,0]
    Vars["score"]+=10
    if Vars["time_max"]>10:
        Vars["time_max"]-=3
    #Vars["structure_color"][i]=["","","","","","","","","",""]
    
def structure():
    for i in range(20):
        for j in range(10):
            if Vars["structure"][i][j]==1:
                print(Vars["structure_color"][i][j])
                pygame.draw.rect(Window,Vars["structure_color"][i][j],((Vars["WinSize"][0]/4)+(Vars["WinSize"][0]/20*j)+1,i*(Vars["WinSize"][1]/20)+1,(Vars["WinSize"][0]/20)-2,(Vars["WinSize"][1]/20)-2))
    
        
def setup_shape():
    Vars["xy"]=[4,0]
    Vars["shape"]=Vars["next_shape"]
    Vars["next_shape"]=random.choice(Vars["shapes"])
    
    struct()
    Vars["pos"]=[Vars["WinSize"][0]/2-(Vars["WinSize"][0]/20)+1,1]
    drawing()
    Vars["down"]=False
    show_next_shape()
    
def show_next_shape():
    x=1
    Window.fill("black",(((Vars["WinSize"][0]/4)*3)+1,Vars["WinSize"][1]/8,(Vars["WinSize"][0]/2)-2,Vars["WinSize"][1]/2))
    for i in range(len(Vars["next_shape_orientation"])):
        for j in range(len(Vars["next_shape_orientation"][0])):
            if Vars["next_shape_orientation"][i][j]==1:
                pygame.draw.rect(Window,Vars["next_shape_color"],(Vars["WinSize"][0]*0.75+((j+1)*Vars["square"][0]),Vars["WinSize"][1]/8+((1+i)*Vars["square"][1]),Vars["square"][0],Vars["square"][1]),3)
screen()


setup_shape()
while Vars["running"] == True:
    if Vars["gameover"]==False:
        WinSize=pygame.display.get_window_size()
        
        Vars["time"]+=1
        if Vars["time"]>Vars["time_max"]:
            move()
            
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                Vars["running"]=False
            if event.type == pygame.KEYDOWN:
                keyboard(event.key)
            if event.type==pygame.VIDEORESIZE:
                screen()
            if event.type == pygame.KEYUP:
                keyup(event.key)
                
        if Vars["down"]==True:
            move()
        pygame.display.update()
    else:
        font = pygame.font.SysFont(None,100)
        text = font.render("gameover", True, "white")
        #pygame.Surface.blit(text,((Vars["WinSize"][0]/4)*3,Vars["WinSize"][1]/10))
        Window.blit(text,((Vars["WinSize"][0]/6.2),Vars["WinSize"][1]/3))
        pygame.display.update()
    for event in pygame.event.get():
            
        if event.type == pygame.QUIT:
            Vars["running"]=False            

            
        
    
    clock.tick(60)