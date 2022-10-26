# import pygame module in this program
import pygame
pygame.init()

screen=pygame.display.set_mode((100,100))


font = pygame.font.SysFont(None, 24)
img = font.render('hello', True, "BLUE")
screen.blit(img, (20, 20))

"""img = font.render(sysfont, True, RED)
rect = img.get_rect()
pygame.draw.rect(img, BLUE, rect, 1)"""
running=True    
    
    
while running == True:
    WinSize=pygame.display.get_window_size()
    
    
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
            

        
    
    pygame.display.update()