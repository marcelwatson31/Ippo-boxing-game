import pygame
pygame.init()

clock = pygame.time.Clock()
screenwidth = 840
screenheight = 600

win = pygame.display.set_mode((screenwidth, screenheight))

pygame.display.set_caption("Marcel Game")

walkright = [pygame.image.load('C:/Users\marce\Desktop\python code\game python\sprite_00.png'), pygame.image.load('C:/Users\marce\Desktop\python code\game python\sprite_01.png'), pygame.image.load('C:/Users\marce\Desktop\python code\game python\sprite_02.png'), pygame.image.load('C:/Users\marce\Desktop\python code\game python\sprite_03.png')]
walkleft = [pygame.image.load('C:/Users\marce\Desktop\python code\game python\sprite_04.png'),  pygame.image.load('C:/Users\marce\Desktop\python code\game python\sprite_00.png'), pygame.image.load('C:/Users\marce\Desktop\python code\game python\sprite_01.png'), pygame.image.load('C:/Users\marce\Desktop\python code\game python\sprite_02.png')]
char = pygame.image.load('C:/Users\marce\Desktop\python code\game python\sprite_00.png')
bg = pygame.image.load('C:/Users\marce\Desktop\python code\game python/arena.png')
walkCount = 0

def redrawgamewindow():
    global walkCount

    win.blit(bg,(0,0))
    

    if walkCount + 1 >= 27:
       walkCount = 0

    if left:
        win.blit(walkleft[walkCount//7], (x,y))
        walkCount += 1
    elif right:
        win.blit(walkright[walkCount//7], (x, y))
        walkCount += 1
    else:
        win.blit(char, (x,y))

    pygame.display.update()

x = 50
y = 450
wid = 64
hei = 64
vel = 5
left = False
right = False


isjump = False
jumpcount = 10

run = True
while run:
    clock.tick(27)
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x-= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < screenwidth - wid - vel:
        x += vel
        right = True
        left = False
    else:
        right = False
        left = False
        walkCount = 0

    if not(isjump):
        if keys[pygame.K_DOWN] and y < screenheight  - hei - vel:
            y += vel
        if keys[pygame.K_UP] and y > vel:
            y -= vel
        if keys[pygame.K_SPACE]:
            isjump = True
            right = False
            left = False
            walkCount = 0

    else:
        if jumpcount >= -10:
            neg = 1
            if jumpcount < 0:
                neg = -1
            y -= (jumpcount ** 2) * .7 * neg
            jumpcount -= 1
        else:
            isjump = False
            jumpcount = 10

    redrawgamewindow()
    

pygame.quit()
