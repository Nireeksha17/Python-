
import pygame
import sys
import os
import random 
import math

pygame.init()
pygame.display.set_caption("Snaky Peeky")
pygame.font.init()
random.seed()

#on 17-04-2023 
#screen initiaization
display_screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),pygame.HWSURFACE)
# hwsurface = hardware surface refers to using memory on the video card for storing
# draws as opposed to main memory

#Resources needed for the game [score_card,snake_food,background]
scoreCard_font = pygame.font.Font(None,40)
scoreCardNumber_font = pygame.font.Font(None,30)
gameOver_text_font =  pygame.font.Font(None,46)
background_color = pygame.Color(0,0,0)    # we will fill background color as black
black = pygame.Color(0,0,0)

