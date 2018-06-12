""" Kill Kenny II.

A really simple pygame game that demonstrates:
    opening a pygame window
    setting the background colour
    displaying a sprite from an image
    using random coordinates
    checking for mouse clicks
    checking is mouse click is in the rectangle of the sprite
    updating the sprite image
    playing a sound
    using a clock to control loop rate and activities
    the use of functions

"""

__copyright__ = "(c) Pinkogreenie Collective 2014"
__license__ = "Creative Commons Attribution-ShareAlike 2.0 Generic License."
__author__ = "Dr G"
__version__ = "0.2"
__revision__ = "20150721"

""" revision notes:
    0.2
    add functionality of moving kenny every 0.75 secs
    limits rate at which game cycles through the while loop
    adds a function for setting kenny's position
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
kenny_lives = True #flag to see if kenny still alive

#set the sound file to play when kenny killed
killed_kenny = P.mixer.Sound('media/killed_kenny.ogg')

#set an initial background colour
bg_colour = blue

clock = P.time.Clock() # Create a timer used to control how often the screen updates
loop_rate = 20 #number of times per second the while loop executes
time_step = 750 #time in millisecs between moving kenny
last_moved = 0 #last time kenny was moved


def set_kenny_position():
    """ creates a random position for kenny on the screen.

    put kenny randomly on the screen.
    need to make sure he stays on the screen by subtracting the image size
    from the screen size
    pygame places things according to x and y coordinates
    [0,0] is the top left hand corner
    the units are pixels
    """

    #first get a random x coordinate
    kenny_x_position = R.randrange(0,display_size[0]-kenny_size[0])
    #then a random y coordinate
    kenny_y_position = R.randrange(0,display_size[1]-kenny_size[1])
    #now combine these into a position
    return [kenny_x_position,kenny_y_position]


#set the intial position for kenny
kenny_position = set_kenny_position()

#-------------------------------------------------------------------------------
#now the fun begins
#-------------------------------------------------------------------------------

while not quit_game: #this is the loop where we wait for the user to do something

    clock.tick(loop_rate) #cycle through loop 'rate' times per second
    now = P.time.get_ticks() #get the time since program started in millisecs

    if (now - last_moved > time_step) and kenny_lives: #time to move kenny
        kenny_position = set_kenny_position()
        last_moved = now


    #at the beginning of each loop check to see if the user wants to quit
    event = P.event.poll()
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
            kenny_lives = False
            bg_colour = dark_red

    main_window.fill(bg_colour) #this sets the background colour
    main_window.blit(kenny, kenny_position) #this is the command to put kenny on the screen
    P.display.flip() #this updates the screen


P.quit()
