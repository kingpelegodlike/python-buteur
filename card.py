import pygame
import pathlib
import re

class Card():
    def __init__(self, front_image, back_image="img/base_2.png"):
        # self.front_img = pygame.image.load("img/{}.png".format(front_image))
        self.front_img = front_image
        self.back_img = pygame.image.load("img/base_2.png")
        self.back_imgage_path = back_image
        self.get_attributes_from_file_name(pathlib.Path(front_image).stem)

    def __repr__(self):
        return  "type:'{}', color:'{}', direction:'{}'" \
                .format(self.type, self.color, self.direction_list)

    def __str__(self):
        direction = ""
        if hasattr(self, "first_directions"):
            for directions in self.first_directions:
                direction += "{}{}".format(directions[0], directions[1])
            direction = self.first_directions
        if hasattr(self, "second_directions"):
            for directions in self.second_directions:
                direction += "{}{}".format(directions[0], directions[1])
            direction = self.second_directions
        return  "type:'{}', color:'{}', direction:'{}'" \
                .format(self.type, self.color, direction)

    def print(self):
        direction = ""
        if hasattr(self, "first_directions"):
            for directions in self.first_directions:
                direction += "{}{}".format(directions[0], directions[1])
            direction = self.first_directions
        if hasattr(self, "second_directions"):
            for directions in self.second_directions:
                direction += "{}{}".format(directions[0], directions[1])
            direction = self.second_directions
        return  "type:'{}', color:'{}', direction:'{}'" \
                .format(self.type, self.color, direction)

    def get_attributes_from_file_name(self, file_name):
        attributes_list = file_name.split("_")
        print("{}:{}".format(len(attributes_list), attributes_list))
        if attributes_list[0] != "card":
            return
        if len(attributes_list) > 1:
            self.type = attributes_list[1]
            if self.type == "attacker" or self.type == "corner":
                if len(attributes_list) > 2:
                    self.color = attributes_list[2]
                    if len(attributes_list) > 3:
                        self.first_move_list = []
                        first_directions = attributes_list[3]
                        pattern = "(\d+)(s|l|r|dl|dr)"
                        for match in re.finditer(pattern, first_directions):
                            for i in range(1, len(match.groups())):
                                direction_len = match.groups(i)[0]
                                direction = match.groups(i)[1]
                                if direction == "s":
                                    self.first_move_list.append((0, int(direction_len)))
                                elif direction == "l":
                                    self.first_move_list.append((-int(direction_len), 0))
                                elif direction == "r":
                                    self.first_move_list.append((int(direction_len), 0))
                                elif direction == "dl":
                                    self.first_move_list.append((-int(direction_len), int(direction_len)))
                                elif direction == "dr":
                                    self.first_move_list.append((int(direction_len), int(direction_len)))
                        if len(attributes_list) > 4:
                            print("{}:{}".format(len(attributes_list), attributes_list))
                            self.second_move_list = []
                            second_directions = attributes_list[4]
                            pattern = "(\d+)(s|l|r|dl|dr)"
                            for match in re.finditer(pattern, second_directions):
                                for i in range(1, len(match.groups())):
                                    direction_len = match.groups(i)[0]
                                    direction = match.groups(i)[1]
                                    if direction == "s":
                                        self.second_move_list.append((0, int(direction_len)))
                                    elif direction == "l":
                                        self.second_move_list.append((-int(direction_len), 0))
                                    elif direction == "r":
                                        self.second_move_list.append((int(direction_len), 0))
                                    elif direction == "dl":
                                        self.second_move_list.append((-int(direction_len), int(direction_len)))
                                    elif direction == "dr":
                                        self.second_move_list.append((int(direction_len), int(direction_len)))
            elif self.type == "freekick" or self.type == "goalkeeper" or self.type == "penalty":
                self.color = None
                if len(attributes_list) > 2:
                    self.first_move_list = []
                    first_directions = attributes_list[2]
                    pattern = "(\d+)(s|l|r|dl|dr)"
                    for match in re.finditer(pattern, first_directions):
                        for i in range(1, len(match.groups())):
                            direction_len = match.groups(i)[0]
                            direction = match.groups(i)[1]
                            if direction == "s":
                                self.first_move_list.append((0, int(direction_len)))
                            elif direction == "l":
                                self.first_move_list.append((-int(direction_len), 0))
                            elif direction == "r":
                                self.first_move_list.append((int(direction_len), 0))
                            elif direction == "dl":
                                self.first_move_list.append((-int(direction_len), int(direction_len)))
                            elif direction == "dr":
                                self.first_move_list.append((int(direction_len), int(direction_len)))
                    if len(attributes_list) > 3:
                        print("{}:{}".format(len(attributes_list), attributes_list))
                        self.second_move_list = []
                        second_directions = attributes_list[3]
                        pattern = "(\d+)(s|l|r|dl|dr)"
                        for match in re.finditer(pattern, second_directions):
                            for i in range(1, len(match.groups())):
                                direction_len = match.groups(i)[0]
                                direction = match.groups(i)[1]
                                if direction == "s":
                                    self.second_move_list.append((0, int(direction_len)))
                                elif direction == "l":
                                    self.second_move_list.append((-int(direction_len), 0))
                                elif direction == "r":
                                    self.second_move_list.append((int(direction_len), 0))
                                elif direction == "dl":
                                    self.second_move_list.append((-int(direction_len), int(direction_len)))
                                elif direction == "dr":
                                    self.second_move_list.append((int(direction_len), int(direction_len)))
            else:
                delattr(self, "type")
