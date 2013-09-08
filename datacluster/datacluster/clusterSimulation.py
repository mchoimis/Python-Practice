'''
http://www.codeproject.com/Articles/369387/Data-Clustering-Simulation-in-Python-and-PyGame
Created on Apr 19, 2012

@author: CyberHornet
'''

import pygame, sys, time
from pygame.locals import *
from pyDataCluster import *

data=[]
groups=10  #random integer 500 * 10 groups = 5000?
for i in range(5000):
    data.append([random.randint(1, 500), random.randint(1, 500)])
    
cluster = pyDataCluster(groups,data)
Color=[]
for i in range(groups):
    
    while True:
        cl=((random.randint(0,255)),(random.randint(0,255)),(random.randint(0,255)))
        if cl not in Color:   
            Color.append(cl)
            break
pygame.init()
WINDOWWIDTH = 500
WINDOWHEIGHT = 500
BASICFONT = pygame.font.Font('freesansbold.ttf',50)
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32) # bits per pixel (range is {8...32})
pygame.display.set_caption('Cluster Simulation')

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE=(255,255,255)


while cluster.terminat:
        points=[]
        
        clus=cluster.createCluster()
        a=0
        for i in clus:
            
            for j in i:
                points.append({'rect':pygame.Rect(j[0],j[1],4,4),'color':Color[a]})
            a=a+1
        for p in points:        
                pygame.draw.rect(windowSurface, p['color'], p['rect'])
        pygame.display.update()
    #time.sleep(0.05)
  

while True:
    # check for the QUIT event
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()  
