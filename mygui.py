import playsound # allows the playing of sound files
import time #download current time for sleep function
import pygame #Library for running graphical interface
import os

folder_path = 'D://recordings/InteractionHumanAndMachine/images'

class imageHandler:
  def __init__ ( self ):
    self.pics = dict()

  def loadFromFile ( self, filename, id=None ):
    if id == None: id = filename
    self.pics [ id ] = pygame.image.load ( filename ).convert()

  def loadFromSurface ( self, surface, id ):
    self.pics [ id ] = surface.convert_alpha()

  def render ( self, surface, id, position = None, clear = False, size = None ):
    if clear == True:
      surface.fill ( (0,0,0) ) #

    if position == None:
      picX = int ( surface.get_width() / 2 - self.pics [ id ].get_width() / 2 )
      picY = int ( surface.get_height()  - self.pics [ id ].get_height()  )
    else:
      picX = position [0]
      picY = position [1]

    if size == None:
      surface.blit ( self.pics [ id ], ( picX, picY ) ) #

    else:
      surface.blit ( pygame.transform.smoothscale ( self.pics [ id ], size ), ( picX, picY ) )


#Initialises the display-------------------------------------------------------
pygame.display.init() # Initiates the display pygame
#screen = pygame.display.set_mode((400,400), pygame.RESIZABLE) #uncomment this line for smaller window
screen = pygame.display.set_mode((400,600), pygame.RESIZABLE) #allows fullscreen #comment this line out for smaller window
pygame.display.set_caption("Pixel")
handler = imageHandler()


def display():
    items = os.listdir(folder_path)
    num_items = len(items)
    file_name_prefix = 'new_name_'
    
    for x in range(num_items):
        handler.loadFromFile ( f'{folder_path}/{file_name_prefix}{x}.jpg', x ) #add your own file location here
       
display()


def face():
    A = 25
    B = -175
    x = 400
    y = 600
    
    items = os.listdir(folder_path)
    num_items = len(items)

    for x in range(num_items):
      handler.render ( screen, x, ( A, B ), True, ( x, y ) )
      pygame.display.update(A,B,x,y)
      time.sleep(.02)



A = 25
B = -175
x = 400
y = 600
while True:
    # Handle events
    for event in pygame.event.get():
        face()
        screen.fill((0, 0, 0))
        pygame.display.update(A,B,x,y)
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
