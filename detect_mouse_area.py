#! /usr/bin/env python3.10
  
# Do the imports
import pygame
import os
  
# Get current working directory
path = os.getcwd()
  
# Initialize pygame
pygame.init()
  
# Set screen size
screen = pygame.display.set_mode((800,600))
  
# Set and display the window icon
# game_icon = pygame.image.load(f'{path}/icons/ratt.ico')
#pygame.display.set_icon(game_icon)
  
# Set a hand cursor
hand = pygame.SYSTEM_CURSOR_HAND
arrow = pygame.SYSTEM_CURSOR_ARROW
  
# Set and display window title
pygame.display.set_caption('My Game')
  
# pygame clock for setting frame rate
clock = pygame.time.Clock()
  
font = pygame.font.SysFont(None, 120)
text = font.render('Test Text', True, 'ivory')
shadow = font.render('Test Text', True, 'steelblue')
  
btn_font = pygame.font.SysFont(None, 40)
button = pygame.Rect(350, 500, 120, 40)
btn_background = pygame.Rect(350, 500, 120, 40)
btn_shadow = pygame.Rect(352, 502, 120, 40)
btn_text = btn_font.render('Button', True, 'white')
  
# Draw rectangle
myrect = pygame.Rect(20, 10, 760, 80)
  
  
  
# Main program
def main():
    running = True
  
    while running:
        # Get mouse position
        mx, my = pygame.mouse.get_pos()
  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
  
        screen.fill('ivory')
  
        pygame.draw.rect(screen, 'lightskyblue', myrect)
        pygame.draw.rect(screen, 'royalblue', myrect, 2)
        screen.blit(shadow, (220, 15))
        screen.blit(text,(218, 13))
  
        pygame.draw.rect(screen, (170, 170, 170), btn_shadow)
        pygame.draw.rect(screen, 'tomato', btn_background)
        pygame.draw.rect(screen, 'black', button, 1)
  
        # Check if cursor is in the button area
        '''
        if mx >= btn_background[0] and mx <= btn_background[0]+119 \
        and my >= btn_background[1] and my <= btn_background[1]+39:
        '''
        if button.collidepoint (mx, my) :
            pygame.mouse.set_cursor(hand)
        else:
            pygame.mouse.set_cursor(arrow)
  
        screen.blit(btn_text, (363, 507))
  
  
        pygame.display.update()
        clock.tick(60)
  
if __name__ == '__main__':
    main()