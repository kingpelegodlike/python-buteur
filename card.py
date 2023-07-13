import pygame

class Card():
    def __init__(self, front_image):
        # self.front_img = pygame.image.load("img/{}.png".format(front_image))
        self.front_img = front_image
        self.back_img = pygame.image.load("img/base_2.png")