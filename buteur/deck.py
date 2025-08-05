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
        if pos >= len(self.card_list):
            return None
        return self.card_list[pos]

    def set_card_rect(self, pos, rect):
        if pos < 0 or pos >= len(self.card_list):
            return False
        self.card_list[pos].rect = rect
        return True

    def remove_card(self, pos = -1):
        try:
            if pos != -1:
                return self.card_list.pop(pos)
            return self.card_list.pop()
        except IndexError:
            return None
