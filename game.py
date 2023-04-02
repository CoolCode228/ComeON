import pygame
pygame.init()
width=900
height=600
screen=pygame.display.set_mode((width,height))
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    screen.fill("purple")
    pygame.draw.rect(screen,"green",(300,300,80,80))
    pygame.draw.rect(screen,"green",(400,300,80,80))
    pygame.draw.rect(screen,"green",(500,300,80,80))
    pygame.draw.rect(screen,"green",(350,220,80,80))
    pygame.draw.rect(screen,"green",(450,220,80,80))
    pygame.draw.rect(screen,"green",(400,140,80,80))
    pygame.display.flip()
