""" Kill Kenny III - The array version.

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
    the use of classes

"""

__copyright__ = "(c) Pinkogreenie Collective 2014"
__license__ = "Creative Commons Attribution-ShareAlike 2.0 Generic License."
__author__ = "Dr G"
__version__ = "0.3.1"
__revision__ = "20150721"

""" revision notes:
    0.2
    add functionality of moving kenny every 0.75 secs
    limits rate at which game cycles through the while loop
    0.2.1
    more pythonesque. Uses classes for sprite.
    0.3
    adds two sprites and creates a subclass of Sprites called Kenny to
    demonstrate inheritance
    0.3.1
    uses arrays and looping to manipulate multiple sprites
    adds slap sound and fart sound for cartman

    fart and slap sounds public domain from soundbible
"""

#-------------------------------------------------------------------------------
#dependencies
#-------------------------------------------------------------------------------
import pygame as P
import random as R

#initialise pygame
P.init()

#set global variables
display_size = [800,600]
quit_game = False

# Define some colors
dark_red = (128,0,0)
blue = (0,0,225)

#create a window to display game
main_window = P.display.set_mode(display_size)

#set an initial background colour
bg_colour = blue

clock = P.time.Clock() # Create a timer used to control how often the screen updates
loop_rate = 20 #number of times per second while loop executes
time_step = 500 #time in millisecs between moving kenny
last_moved = 0 #last time kenny was moved


class Sprite(object):
    """southpark sprites.

    Create a sprite with necessary parameters to draw it

    Attributes:
        screen_size: the size of the display screen in pixels

    """

    def __init__(self, image_fn):
        """Initiates the properties of the sprite."""
        self.image = P.image.load(image_fn)
        self.rectangle = self.image.get_rect()
        self.set_position()
        self.live = True


    def set_position(self):
        """ creates a random position for sprite on the screen.

        put sprite randomly on the screen.
        need to make sure it stays on the screen by subtracting the image size
        from the screen size
        pygame places things according to x and y coordinates
        [0,0] is the top left hand corner
        the units are pixels
        """

        #set a random x coordinate
        self.rectangle.left = R.randrange(0,display_size[0]- self.image.get_size()[0])
        #set a random y coordinate
        self.rectangle.top = R.randrange(0,display_size[1]- self.image.get_size()[1])

class Kenny(Sprite):

    def __init__(self):
        """Initiates the properties of the sprite."""
        Sprite.__init__(self,'media/kenny.png')


    def die(self):
        self.image = P.image.load("media/kenny_dead.png")
        self.live = False
        P.mixer.Sound('media/killed_kenny.ogg').play()


#now lets create kenny
kenny = Kenny()
stan = Sprite('media/stan.png')
kyle = Sprite('media/kyle.png')
cartman = Sprite('media/cartman.png')

sprite_array = [kenny, stan, kyle, cartman]

while not quit_game: #this is the loop where we wait for the user to do something

    clock.tick(loop_rate) #cycle through loop 'rate' times per second
    now = P.time.get_ticks() #get the time since program started in millisecs

    if (now - last_moved > time_step) and kenny.live: #time to move kenny
        for s in sprite_array:
            s.set_position()
            last_moved = now
            time_step += 10 #slow it down every loop to make it easier


    #at the beginning of each loop check to see if the user wants to quit
    event = P.event.poll()
    if event.type == P.QUIT:
        quit_game = True

    #check to see if the user presses the mouse button down,
    elif event.type == P.MOUSEBUTTONDOWN:
        P.mixer.Sound('media/slap.wav').play()
        #if the mouse click/touch is in kenny's rectangle kenny dies
        if kenny.rectangle.collidepoint(P.mouse.get_pos()) and kenny.live:
            kenny.die()
            bg_colour = dark_red
        #if hit cartman he farts
        elif cartman.rectangle.collidepoint(P.mouse.get_pos()):
            P.mixer.Sound('media/fart.wav').play()

    main_window.fill(bg_colour) #this sets the background colour
    for s in sprite_array:
        main_window.blit(s.image, s.rectangle) #this is the command to put sprites on the screen
    P.display.flip() #this updates the screen


P.quit()
