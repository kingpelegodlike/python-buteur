class Deck():
    def __init__(self):
        self.card_list = []

    def add_card(self, card_obj):
        self.card_list.append(card_obj)

    def get_nb_cards(self):
        return len(self.card_list)

    def get_cards(self):
        return self.card_list

    def get_card(self, pos = -1):
        if len(self.card_list) == 0:
            return None
        elif pos > len(self.card_list):
            return None
        else:
            return self.card_list[pos]

    def remove_card(self, pos = -1):
        try:
            if pos != -1:
                self.card_list.pop(pos)
            else:
                self.card_list.pop()
        except IndexError as e:
            pass