##需要先安裝pygame (pip install pygame)
import pygame,sys
from pygame.locals import *

pygame.init();

windows_surface = pygame.display.set_mode((10,10), pygame.NOFRAME);

x,y =0,0;

while True: 
  for event in pygame.event.get(): 
    if event.type==KEYDOWN: 
      if event.key==K_LEFT: 
        x-=1
        print(x,y)
      if event.key==K_RIGHT: 
        x+=1
        print(x,y)
      if event.key==K_UP: 
        y+=1
        print(x,y)
      if event.key==K_DOWN: 
        y-=1
        print(x,y)
      if event.key==K_SPACE:
        pygame.quit() 
        sys.exit() 
