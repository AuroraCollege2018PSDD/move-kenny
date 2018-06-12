#-------------------------------------------------------------------------------
# Name:        move_kenny
# Purpose:     Q&D module to demonstrate moving pictures in pygame
#
# Author:      ggoldric
#
# Created:     26/07/2012
# Copyright:   (c) ggoldric 2012
# Licence:     <your licence>
# Edited:      26/07/2012
#               added ability for kenny to move with mouse
#               added check to see if mouse is in kenny
#-------------------------------------------------------------------------------
#!/usr/bin/env python

#dependencies
#from pygame import *
import pygame

#set global variables
displaySize = [800,600]
x = y = 0
quitGame = False

# Define some colors
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)
blue     = (   0,   0, 225)

#create a window to display game
mainWindow = pygame.display.set_mode(displaySize)
mainWindow.fill(blue)
kenny = pygame.image.load("kenny.png")
kennyPosition = [0,0]
mainWindow.blit(kenny, kennyPosition)
pygame.display.flip()
mouseDown = False

while not quitGame:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        quitGame = True
    #when the user presses the mouse button down,
    #a call to mouse.get.rel() resets this function
    elif event.type == pygame.MOUSEBUTTONDOWN:
        imageRectangle = pygame.Rect(kennyPosition,kenny.get_size())
        if imageRectangle.collidepoint(pygame.mouse.get_pos()):
            pygame.mouse.get_rel() #reset the relative mouse movement
            mouseDown = True


        #now wait until the mouse button has been released and call
        #mouse.gel.rel() again
        while  mouseDown:
            event = pygame.event.poll()
            if event.type == pygame.MOUSEBUTTONUP:
                mouseDown = False
            elif event.type == pygame.MOUSEMOTION: #move kenny with the mouse
                motion = pygame.mouse.get_rel() #get and reset the relative mouse movement
                #adjust kenny's position by the amount the mouse has moved
                kennyPosition[0] = kennyPosition[0] + motion[0]
                kennyPosition[1] = kennyPosition[1] + motion[1]
                #redraw the screen
                mainWindow.fill(blue)
                mainWindow.blit(kenny, kennyPosition)
                pygame.display.flip()



pygame.quit()

# this module needs to be improved by:
# 1/ making sure that the mouse is over kenny when initially pressed
# 2/ allowing kenny to move with the mouse. this could be done by including
# a MOUSEMOTION event handler in the loop at line 50.




##def main():
##    pass
##
##if __name__ == '__main__':
##    main()
