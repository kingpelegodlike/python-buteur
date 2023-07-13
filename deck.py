class Deck():
    def __init__(self):
        self.card_list = []

    def add_card(self, card_obj):
        self.card_list.append(card_obj)

    def get_card(self, pos = -1):
        if len(self.card_list) == 0:
            return None
        elif pos > len(self.card_list):
            return None
        else:
            return self.card_list[pos]

    def remove_card(self):
        self.card_list.pop()