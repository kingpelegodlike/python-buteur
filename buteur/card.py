import pathlib
import re
import pygame

class Card():
    """
    Create a new game card object from the given object.

    Attributes
    ----------
    front_img : str
        path to the front image of the card
    back_img : image
        image object of the back of the card
    back_imgage_path : str
        path to the back image of the card

    Methods
    -------
    get_attributes_from_file_name(file_name)
        add card attributes from the file name
    """
    def __init__(self, front_image, back_image="img/base_2.png"):
        """
        Parameters
        ----------
        front_image : str
            path to the front image of the card
        back_img : str
            path to the back image of the card
        """
        self.front_img = front_image
        self.back_img = pygame.image.load("img/base_2.png")
        self.back_imgage_path = back_image
        self.get_attributes_from_file_name(pathlib.Path(front_image).stem)

    def __repr__(self):
        direction = ""
        if hasattr(self, "first_move_list"):
            direction += "first moves:"
            for directions in self.first_move_list:
                direction += f"({directions[0]},{directions[1]})"
            # direction = self.first_directions
        if hasattr(self, "second_move_list"):
            direction += " second moves:"
            for directions in self.second_move_list:
                direction += f"({directions[0]},{directions[1]})"
            # direction = self.second_directions
        if hasattr(self, "third_move_list"):
            direction += " third moves:"
            for directions in self.third_move_list:
                direction += f"({directions[0]},{directions[1]})"
            # direction = self.third_directions
        return  f"type:'{self.type}', color:'{self.color}', direction:'{direction}'"

    def __str__(self):
        direction = ""
        if hasattr(self, "first_move_list"):
            direction += "first moves:"
            for directions in self.first_move_list:
                direction += f"({directions[0]},{directions[1]})"
            # direction = self.first_directions
        if hasattr(self, "second_move_list"):
            direction += " second moves:"
            for directions in self.second_move_list:
                direction += f"({directions[0]},{directions[1]})"
            # direction = self.second_directions
        if hasattr(self, "third_move_list"):
            direction += " third moves:"
            for directions in self.third_move_list:
                direction += f"({directions[0]},{directions[1]})"
            # direction = self.third_directions
        return  f"type:'{self.type}', color:'{self.color}', direction:'{direction}'"

    def print(self):
        direction = ""
        if hasattr(self, "first_move_list"):
            direction += "first moves:"
            for directions in self.first_move_list:
                direction += f"({directions[0]},{directions[1]})"
            # direction = self.first_directions
        if hasattr(self, "second_move_list"):
            direction += " second moves:"
            for directions in self.second_move_list:
                direction += f"({directions[0]},{directions[1]})"
            # direction = self.second_directions
        if hasattr(self, "third_move_list"):
            direction += " third moves:"
            for directions in self.third_move_list:
                direction += f"({directions[0]},{directions[1]})"
            # direction = self.third_directions
        return  f"type:'{self.type}', color:'{self.color}', direction:'{direction}'"

    def get_attributes_from_file_name(self, file_name):
        """
        Parameters
        ----------
        file_name : str
            path to an image file
        """
        attributes_list = file_name.split("_")
        print(f"len(attributes_list):{attributes_list}")
        if attributes_list[0] != "card":
            return
        if len(attributes_list) > 1:
            self.type = attributes_list[1]
            if self.type in ["attacker", "corner"]:
                if len(attributes_list) > 2:
                    self.color = attributes_list[2] # blue or red or hand
                    if len(attributes_list) > 3:
                        self.first_move_list = []
                        first_directions = attributes_list[3]
                        pattern = r"(\d+)(s|l|r|dl|dr)"
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
                            print("%s:%s", len(attributes_list), attributes_list)
                            second_directions = attributes_list[4]
                            if second_directions.startswith("v"):
                                return
                            self.second_move_list = []
                            pattern = r"(\d+)(s|l|r|dl|dr)"
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
                        if len(attributes_list) > 5:
                            print("%s:%s", len(attributes_list), attributes_list)
                            third_directions = attributes_list[5]
                            if third_directions.startswith("v"):
                                return
                            self.third_move_list = []
                            pattern = r"(\d+)(s|l|r|dl|dr)"
                            for match in re.finditer(pattern, third_directions):
                                for i in range(1, len(match.groups())):
                                    direction_len = match.groups(i)[0]
                                    direction = match.groups(i)[1]
                                    if direction == "s":
                                        self.third_move_list.append((0, int(direction_len)))
                                    elif direction == "l":
                                        self.third_move_list.append((-int(direction_len), 0))
                                    elif direction == "r":
                                        self.third_move_list.append((int(direction_len), 0))
                                    elif direction == "dl":
                                        self.third_move_list.append((-int(direction_len), int(direction_len)))
                                    elif direction == "dr":
                                        self.third_move_list.append((int(direction_len), int(direction_len)))
            elif self.type in ["freekick", "goalkeeper"]:
                self.color = None
                if len(attributes_list) > 2:
                    self.first_move_list = []
                    first_directions = attributes_list[2]
                    pattern = r"(\d+)(s|l|r|dl|dr)"
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
                        print("%s:%s", len(attributes_list), attributes_list)
                        self.second_move_list = []
                        second_directions = attributes_list[3]
                        pattern = r"(\d+)(s|l|r|dl|dr)"
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
            elif self.type == "penalty":
                self.color = None
                # move to the penalty spot
            else:
                delattr(self, "type")
        else:
            return
