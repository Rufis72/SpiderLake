'''import time
import pygame
screen = pygame.display.set_mode((900, 900))
pygame.display.init()
pygame.init()
fonty1 = pygame.font.Font("Arial Unicode.ttf", 32)
fonty2 = pygame.font.Font()
font_list = [fonty1, fonty2]
help(pygame.font.Font.render)
texty1 = fonty1.render("aba, aba", True, (255, 255, 255), None)
recty1 = texty1.get_rect()
recty1.topleft = (300, 300)
pygame.display.set_caption("ur mum, get rekt")
screen.blit(texty1, recty1)
while(True):
    pygame.display.flip()'''
import pygame
pygame.init()
while True:
    print(pygame.mouse.get_pos())