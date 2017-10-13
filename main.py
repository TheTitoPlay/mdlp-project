''' git@github.com:TheTitoPlay/mdlp-project.git '''

import pygame

pygame.init()

# open new window
window = pygame.display.set_mode((600, 420), pygame.DOUBLEBUF)
pygame.display.set_caption('POP CULTURE VOL.1')
pygame.display.set_icon(pygame.image.load('icon.png'))


done = False
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            done = True
    



