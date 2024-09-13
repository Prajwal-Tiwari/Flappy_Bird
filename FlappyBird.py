import pygame as p
from pygame import mixer
import random as r
import time
import sys
import os

p.init()
p.font.init()

w = p.display.set_mode((500,500))

imp = p.image.load(os.path.join("bg.jpg")).convert()
sp = p.transform.scale(imp, w.get_size())
w.blit(sp,(0,0))

gaon = p.font.Font(None,100)
gmovrs = gaon.render("Flappy Bird",True,"black")
w.blit(gmovrs,(50,100))

cc = True

clock = p.time.Clock()

birds = p.image.load(os.path.join("bird.png")).convert_alpha()
bird = p.transform.scale(birds,(55,33))
bdown = p.transform.rotate(bird,-15)
bup = p.transform.rotate(bird,15)
pipe = p.image.load(os.path.join("pipe.png")).convert_alpha()
pipe2 = p.transform.rotate(pipe,180)
pipeb = p.transform.scale(pipe,(60,440))
pipeb2 = p.transform.scale(pipe2,(60,440))

w.blit(bird,(60,170))

p.display.update()

pipeHeight = r.randrange(160,350,5)

def gameOver():
    global cc
    
    gon = p.font.Font(None,80)
    gmovr = gon.render("Game Over",True,"black")
    w.blit(gmovr,(100,100))

    eon = p.font.Font(None,40)
    emovr = eon.render("Enter to Restart",True,"black")
    w.blit(emovr,(130,200))

    p.display.update()
    while True:
        for event in p.event.get():
                if event.type == p.QUIT or (event.type == p.KEYDOWN and event.key == p.K_ESCAPE): 
                    p.quit() 
                    sys.exit()
                if event.type == p.KEYDOWN and (event.key == p.K_RETURN):
                    cc = True
                    theGame()

def pipefun(horpipe, pipeHeight):
    w.blit(pipeb2,(horpipe,-pipeHeight))
    w.blit(pipeb,(horpipe,pipeb2.get_height()-pipeHeight+60))

def theGame():
    points = 0
    ver = 170
    pipes = [[500, r.randrange(160,350,5), False]]  

    global cc
    while cc:
        for event in p.event.get():
            if event.type == p.QUIT or (event.type == p.KEYDOWN and event.key == p.K_ESCAPE): 
                p.quit() 
                sys.exit()
            if event.type == p.KEYDOWN and (event.key == p.K_SPACE or event.key == p.K_UP):
                if ver - bird.get_height() > 0:
                    ver -= 40
                    w.blit(bup, (60, ver))
                    p.display.update()

        ver += 6

        w.blit(sp, (0, 0))
        
        # Reduced delay for smoother gameplay
        p.time.delay(50)  # Faster update rate for smoother gameplay
        
        w.blit(bdown, (60, ver))
        
        for pipe in pipes:
            pipe[0] -= 10
            pipefun(pipe[0], pipe[1])            

        pot = p.font.Font(None, 32)
        pt = pot.render(f"{points}", True, "black")
        w.blit(pt, (450, 50))

        
        if pipes[-1][0] < 200:
            pipes.append([499, r.randrange(160,350,5), False])

        
        if pipes[0][0] < -60:
            pipes.pop(0)

       
        if ver >= 365:
            cc = False
            gameOver()
        
        for pipe in pipes:
            if (105 in range(pipe[0], pipe[0] + 60) and 
                ver in range(pipeb2.get_height() - pipe[1] - 20)) or (
                105 in range(pipe[0], pipe[0] + 60) and 
                ver in range(pipeb2.get_height() - pipe[1] + 40, 500)):
                cc = False
                gameOver()

            
            if pipe[0] + 60 < 60 and not pipe[2]:  
                points += 1
                pipe[2] = True 

        p.display.update()
        
        clock.tick(32)  # Increase the frame rate for smoother animation

def mainGameScreen():
    tt = p.font.Font(None, 32)
    ttt = tt.render("Start", True, "black")
    w.blit(ttt, (220, 230))

    r1 = p.draw.rect(w, "black", p.Rect(200, 225, 100, 30), 3, 8)

    tt = p.font.Font(None, 32)
    ttt = tt.render("Exit", True, "black")
    w.blit(ttt, (225, 275))

    r2 = p.draw.rect(w, "black", p.Rect(210, 270, 80, 30), 3, 8)

    p.display.update()

    while True:
        mouse = p.mouse.get_pos()
        for event in p.event.get():
            if event.type == p.MOUSEBUTTONDOWN:
                if 200 <= mouse[0] <= 300 and 230 <= mouse[1] <= 260:
                    theGame()
                elif 210 <= mouse[0] <= 290 and 270 <= mouse[1] <= 300:
                    p.quit()
                    sys.exit()
                    
            elif event.type == p.KEYDOWN:
                if event.key == p.K_SPACE:
                    theGame()
                elif event.key == p.K_ESCAPE:
                    p.quit()
                    sys.exit()
            elif event.type == p.QUIT:
                p.quit()
                sys.exit()

mainGameScreen()
