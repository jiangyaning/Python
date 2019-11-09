import pygame as pg
import sys
import random
import time
from pygame.locals import *


pg.init()
game_window=pg.display.set_mode((1000,600))
ball_color=(0,255,0)
bar_color=(255,0,0)
score=0
font=pg.font.Font(None,70)
font2=pg.font.Font(None,30)
ball_x=random.randint(20,1000)


ball_y=30
mv_x=1
mv_y=1
pg.display.set_caption('接球小游戏')
while True:
    game_window.fill((0,0,255))
    rect_x,rect_y=pg.mouse.get_pos()
    for event in pg.event.get():
        if event.type==pg.QUIT:
            sys.exit()
    pg.draw.circle(game_window,ball_color,(ball_x,ball_y),20)
    pg.draw.rect(game_window,bar_color,(rect_x,500,100,10))
    my_score=font.render(str(score),False,(255,255,255))
    game_window.blit(my_score,(800,30))
    ball_x+=mv_x
    ball_y+=mv_y
    if ball_x<=20 or ball_x>=1000:
        mv_x=-mv_x
    if ball_y<=20:
        mv_y=-mv_y
    elif rect_x-20<ball_x<rect_x+120 and ball_y>=470:
        mv_y=-mv_y
        score+=1
    elif ball_y>480 and (ball_x<=rect_x-20 or ball_x>=rect_x+120):
        a="The game is over. Your score is:"+str(score)
        game_window.blit(font2.render(a,True, (255, 255, 255)),(300,300))
        game_window.blit(font.render(('enter exit'),False,(255,255,255)),(300,400))
        for i in pg.event.get():
            if i.type==pg.KEYDOWN:
                if i.key==K_RETURN:
                    sys.exit()
    pg.display.update()
    time.sleep(0.0005)

