## Settings
TITLE = 'Awesome Untitled Platformer Game'
WIDTH = 1024
HEIGHT = 640
FPS = 60

#player
FRICTION = -0.1
SPEED = 0.5
GRAVITY = 0.5
JUMP = 18

#platforms sprite size
BS = 128

#plateforms
PLATFORMS = [(0, HEIGHT - 128, WIDTH * 2, 128),
             (20, 156, 128, 32),
             (800, 200, 500, 32),
             ]
#player player_pick
PICK = [(0,0,80,110),(80,0,80,110),(160,0,80,110),(240,0,80,110),(320,0,80,110)]
        #adventurer   #women        #men           #sodier        #zombie
P_PICK = ['adventurer', 'female', 'male', 'soldier', 'zombie']

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

bgcolor = (0, 191, 255)
