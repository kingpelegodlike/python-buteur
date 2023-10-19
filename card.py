import pygame

class Card():
    def __init__(self, front_image, back_image="img/base_2.png"):
        # self.front_img = pygame.image.load("img/{}.png".format(front_image))
        self.front_img = front_image
        self.back_img = pygame.image.load("img/base_2.png")
        self.back_imgage_path = back_image
        self.get_attributes(front_image)

    def __repr__(self):
        return  "type:'{}', color:'{}', direction:'{}'" \
                .format(self.type, self.color, self.direction_list)

    def __str__(self):
        return  "type:'{}', color:'{}', direction:'{}'" \
                .format(self.type, self.color, self.direction_list)

    def print(self):
        return  "type:'{}', color:'{}', direction:'{}'" \
                .format(self.type, self.color, self.direction_list)

    def get_attributes(self, definition):
        definition_list = definition.split("_")
        self.type = definition_list[0]
        self.color = definition_list[1]
        self.direction_list = []
        for sub_def in definition_list[2:]:
            if sub_def.startswith("at"):
                path = sub_def[2:]
                direction_len = path[0]
                direction = path[1]
                if direction == "s":
                    self.direction_list.append((0, int(direction_len)))
                elif direction == "l":
                    self.direction_list.append((-int(direction_len), 0))
                elif direction == "r":
                    self.direction_list.append((int(direction_len), 0))