""" Kill Kenny.

A really simple pygame game that demonstrates:
    opening a pygame window
    setting the background colour
    displaying a sprite from an image
    using random coordinates
    checking for mouse clicks
    checking is mouse click is in the rectangle of the sprite
    updating the sprite image
    playing a sound

"""

__copyright__ = "(c) Pinkogreenie Collective 2014"
__license__ = "Creative Commons Attribution-ShareAlike 2.0 Generic License."
__author__ = "Dr G"
__version__ = "0.1"
__revision__ = "20150721"

""" revision notes:
"""

#-------------------------------------------------------------------------------
# first some housekeeping
#-------------------------------------------------------------------------------
#import dependencies
import pygame as P
import random as R

#initialise pygame
P.init()

#set some global variables
display_size = [800,600]
quit_game = False

# Define some colors
dark_red = (128,0,0)
blue = (0,0,225)

#create a window to display game
main_window = P.display.set_mode(display_size)

#now we need a kenny sprite.
kenny = P.image.load("media/kenny.png")
kenny_size = kenny.get_size() #returns the size in pixels of the image

#set the sound file to play when kenny killed
killed_kenny = P.mixer.Sound('media/killed_kenny.ogg')

#set an initial background colour
bg_colour = blue

#put kenny randomly on the screen.
#need to make sure he stays on the screen by subtracting the image size
#from the screen size
#pygame places things according to x and y coordinates
#[0,0] is the top left hand corner
#the units are pixels
#first get a random x coordinate
kenny_x_position = R.randrange(0,display_size[0]-kenny_size[0])
#then a random y coordinate
kenny_y_position = R.randrange(0,display_size[1]-kenny_size[1])
#now combine these into a position
kenny_position = [kenny_x_position,kenny_y_position]

#-------------------------------------------------------------------------------
#now the fun begins
#-------------------------------------------------------------------------------

while not quit_game: #this is the loop where we wait for the user to do something

    #see if the user has done something
    event = P.event.poll()

    #if they want to quit, let them
    if event.type == P.QUIT:
        quit_game = True

    #check to see if the user presses the mouse button down,
    elif event.type == P.MOUSEBUTTONDOWN:
        #find the rectangle covered by the image
        image_rectangle = P.Rect(kenny_position,kenny.get_size())
        # the function collide point is used to check if a point is inside a rectangle
        #in this case the point is the position of the mouse
        #and the rectangle is the image of kenny
        if image_rectangle.collidepoint(P.mouse.get_pos()):
            #now kenny must die!
            kenny = P.image.load("media/kenny_dead.png")
            killed_kenny.play()
            bg_colour = dark_red

    main_window.fill(bg_colour) #this sets the background colour
    main_window.blit(kenny, kenny_position) #this is the command to put kenny on the screen
    P.display.flip() #this updates the screen

P.quit()
