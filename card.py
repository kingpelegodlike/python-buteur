import pygame

class Card():
    def __init__(self, front_image, back_image="img/base_2.png"):
        # self.front_img = pygame.image.load("img/{}.png".format(front_image))
        self.front_img = front_image
        self.back_img = pygame.image.load("img/base_2.png")
        self.back_imgage_path = back_image

    def __repr__(self):
        return "Card front image path is '{}' and back image path is '{}'".format(self.front_img, self.back_imgage_path)

    def __str__(self):
        return "Card front image path is '{}' and back image path is '{}'".format(self.front_img, self.back_imgage_path)

    def print(self):
        return "Card front image path is '{}' and back image path is '{}'".format(self.front_img, self.back_imgage_path)