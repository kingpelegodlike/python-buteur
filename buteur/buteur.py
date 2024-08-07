import os
import sys
import pathlib
import logging
from buttons2 import Button, buttons
from card import Card
from deck import Deck
import pygame

# from buttons2 import *
# import buttons2

logger = logging.getLogger('BUTEUR')
logger.setLevel(logging.DEBUG)
logger.handlers = []
logger.propagate = False
console_hdlr = logging.StreamHandler()
console_hdlr.setLevel(logging.INFO)
logger.addHandler(console_hdlr)
loghdlr = logging.FileHandler('buteur.log', mode='w', encoding = "utf-8")
loghdlr.setFormatter(
    logging.Formatter('[%(asctime)s] %(name)s - %(levelname)s - %(message)s'))
loghdlr.setLevel(logging.DEBUG)
logger.addHandler(loghdlr)

TILESIZE = 16
PLAYER_DECK_POS = (10, 370)
PLAY_DECK_POS = (300, 163)
CURRENT_DECK_POS = (300, 30)
TRASH_DECK_POS = (400, 30)
FOOTBALL_FIELD_POS = (10, 10)

def create_player_deck_surf(player_deck):
    player_deck_surf = pygame.Surface(size=(10+(65+10)*8, 123))
    # rect_list = []
    for i in range(0, len(player_deck.card_list)):
        rect = pygame.Rect(10+(65+10)*i, 10, 65, 103)
        card_obj = player_deck.get_card(i)
        # card_img = pygame.image.load(os.path.join("img", "{}.png".format(card_obj.front_img)))
        card_img = pygame.image.load(card_obj.front_img)
        player_deck_surf.blit(card_img, rect)
    return player_deck_surf

def create_play_deck_surf():
    play_deck_durf = pygame.Surface((140, 103))
    rect1 = pygame.Rect(0, 0, 65, 103)
    rect2 = pygame.Rect(75, 0, 65, 103)
    pygame.draw.rect(play_deck_durf,"red",rect1,0)
    pygame.draw.rect(play_deck_durf,"orange",rect2,0)
    return play_deck_durf

def create_current_deck_surf(last_card):
    current_deck_surf = pygame.Surface((65, 103))
    rect = pygame.Rect(0, 0, 65, 103)
    # last_card_img = pygame.image.load(os.path.join("img", "{}.png".format(last_card.front_img)))
    last_card_img = pygame.image.load(last_card.front_img)
    current_deck_surf.blit(last_card_img, rect.topleft)
    return current_deck_surf

def create_trash_deck_surf():
    trash_deck_durf = pygame.Surface((65, 103))
    rect = pygame.Rect(0, 0, 65, 103)
    # last_card_img = pygame.image.load(os.path.join("img", "{}.png".format(last_card.front_img)))
    pygame.draw.rect(trash_deck_durf,"red",rect,0)
    return trash_deck_durf

def create_football_field_surf(ball_x_pos, ball_y_pos):
    football_field_surf = pygame.Surface((TILESIZE*16, TILESIZE*22))
    dark = False
    for yaxis in range(22):
        for xaxis in range(16):
            rect = pygame.Rect(xaxis*TILESIZE, yaxis*TILESIZE, TILESIZE, TILESIZE)
            # football_field_piece_img = pygame.image.load(os.path.join("img", "football_field_x0_y0.png"))
            try:
                football_field_piece_img = pygame.image.load(os.path.join("img", f"football_field_x{xaxis}_y{yaxis}.png"))
            # except FileNotFoundError as fnfe:
            except FileNotFoundError:
                # logger.error(fnfe)
                football_field_piece_img = pygame.image.load(os.path.join("img", "football_field_x0_y0.png"))
            football_field_piece_img = pygame.transform.scale(football_field_piece_img, (TILESIZE, TILESIZE))
            # pygame.draw.rect(football_field_surf, pygame.Color('darkgrey' if dark else 'beige'), rect)
            football_field_surf.blit(football_field_piece_img, rect.topleft)
            dark = not dark
        dark = not dark
    rect = pygame.Rect(ball_x_pos*TILESIZE, ball_y_pos*TILESIZE, TILESIZE, TILESIZE)
    ball_img = pygame.image.load(os.path.join("img", "ball.png"))
    football_field_surf.blit(ball_img, rect.topleft)
    return football_field_surf

def is_player_card_under_mouse():
    mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
    mouse_pos_x = mouse_pos[0]
    mouse_pos_y = mouse_pos[1]
    logger.debug(f"Check mouse pos is ({mouse_pos_x},{mouse_pos_y}) with player cards")
    player_card_under_mouse = -1
    for i in range (0, 8):
        min_pos_x_expected =  10+(65+10)*i
        max_pos_x_expected = min_pos_x_expected + 65
        if mouse_pos_x >= min_pos_x_expected and mouse_pos_x < max_pos_x_expected and mouse_pos_y >= 380 and mouse_pos_y < 483:
            logger.debug(f"found under card number '{i}'")
            player_card_under_mouse = i
    return player_card_under_mouse

def is_current_deck_card_under_mouse():
    """Check if the mouse is over the current deck card."""
    mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
    mouse_pos_x = mouse_pos[0]
    mouse_pos_y = mouse_pos[1]
    logger.debug(f"mouse pos is ({mouse_pos_x},{mouse_pos_y})")
    if mouse_pos_x >= 300 and mouse_pos_x < 365 and mouse_pos_y >= 30 and mouse_pos_y < 133:
        return True
    else:
        return False

def is_trash_deck_card_under_mouse():
    mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
    mouse_pos_x = mouse_pos[0]
    mouse_pos_y = mouse_pos[1]
    logger.debug(f"Check mouse pos ({mouse_pos_x},{mouse_pos_y}) with trash")
    is_under_mouse = mouse_pos_x >= 400 and mouse_pos_x < 465 and mouse_pos_y >= 30 and mouse_pos_y < 133
    return is_under_mouse

def is_play_deck_card_under_mouse(number):
    mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
    mouse_pos_x = mouse_pos[0]
    mouse_pos_y = mouse_pos[1]
    if number == 1:
        logger.debug(f"Check mouse pos ({mouse_pos_x},{mouse_pos_y}) with play area 1")
        if mouse_pos_x >= 300 and mouse_pos_x < 365 and mouse_pos_y >= 163 and mouse_pos_y < 266:
            return True
        else:
            return False
    elif number == 2:
        logger.debug(f"Check mouse pos ({mouse_pos_x},{mouse_pos_y}) with play area 2")
        if mouse_pos_x >= 375 and mouse_pos_x < 440 and mouse_pos_y >= 163 and mouse_pos_y < 266:
            return True
        else:
            return False
    else:
        return False

def update_player_deck_surf(surface, player_deck):
    for i in range(0, 8):
        rect = pygame.Rect(10+(65+10)*i, 10, 65, 103)
        if i < len(player_deck.card_list):
            card_obj = player_deck.get_card(i)
            # card_img = pygame.image.load(os.path.join("img", "{}.png".format(card_obj.front_img)))
            card_img = pygame.image.load(card_obj.front_img)
            logger.debug(f"Update player card number {i} with {card_obj.front_img} image")
            surface.blit(card_img, rect)
        else:
            logger.debug(f"Update player card number {i} with red image")
            pygame.draw.rect(surface, "red", rect, 0)

def draw_play_deck_card(surface, card1, card2):
    rect1 = pygame.Rect(0, 0, 65, 103)
    rect2 = pygame.Rect(75, 0, 65, 103)
    if card1 is not None:
        # card1_img = pygame.image.load(os.path.join("img", "{}.png".format(card1.front_img)))
        card1_img = pygame.image.load(card1.front_img)
        surface.blit(card1_img, rect1)
    else:
        pygame.draw.rect(surface,"red",rect1,0)
    if card2 is not None:
        # card2_img = pygame.image.load(os.path.join("img", "{}.png".format(card2.front_img)))
        card2_img = pygame.image.load(card2.front_img)
        surface.blit(card2_img, rect2)
    else:
        pygame.draw.rect(surface,"red",rect2,0)

def draw_current_deck_card(surface, last_card):
    rect = pygame.Rect(0, 0, 65, 103)
    if last_card is not None:
        # last_card_img = pygame.image.load(os.path.join("img", "{}.png".format(last_card.front_img)))
        last_card_img = last_card.back_img
        surface.blit(last_card_img, rect.topleft)
    else:
        pygame.draw.rect(surface,"red",rect,0)

def draw_trash_deck_card(surface, last_card):
    rect = pygame.Rect(0, 0, 65, 103)
    if last_card is not None:
        # last_card_img = pygame.image.load(os.path.join("img", "{}.png".format(last_card.front_img)))
        last_card_img = pygame.image.load(last_card.front_img)
        surface.blit(last_card_img, rect.topleft)
    else:
        pygame.draw.rect(surface,"red",rect,0)

def is_player_card_to_drop(player_card_selected, play_area_number):
    if player_card_selected is not None:
        # if is_trash_deck_card_under_mouse():
        if is_play_deck_card_under_mouse(play_area_number):
            return True
        else:
            return False
    return False

def is_current_deck_card_to_drop(current_deck_card_selected):
    if current_deck_card_selected:
        if is_trash_deck_card_under_mouse():
            return True
        else:
            return False
    return False

def on_click_play():
    print("Player click Play button")
    # click_play = True

def main():
    # click_play = False
    pygame.init()
    # font = pygame.font.SysFont('', 32)
    pygame.font.SysFont('', 32)
    screen = pygame.display.set_mode((640, 540))
    player1_deck = Deck()
    player2_deck = Deck()
    current_deck = Deck()
    trash_deck = Deck()
    play_deck = Deck()
    # card = Card("img/card_attacker_blue_at3l.png")
    # player1_deck.add_card(card)
    # current_deck.add_card(card)
    # card = Card("img/card_corner_red.png")
    # player1_deck.add_card(card)
    # card = Card("img/card_attacker_blue_at4s.png")
    # player1_deck.add_card(card)
    # player1_deck.add_card(card)
    # player1_deck.add_card(card)
    # player1_deck.add_card(card)
    # player1_deck.add_card(card)
    # player1_deck.add_card(card)
    for card_file_path in pathlib.Path("./img").rglob("card_*.png"):
        card = Card(card_file_path)
        logger.debug(f"Add card {card} to Current Deck")
        current_deck.add_card(card)
    for _ in range(0, 8):
        # player1_deck.add_card(current_deck.remove_card())
        card = current_deck.remove_card()
        logger.debug(f"Add card {card} to Player1 Deck")
        player1_deck.add_card(card)
        # player2_deck.add_card(current_deck.remove_card())
        card = current_deck.remove_card()
        logger.debug(f"Add card {card} to Player2 Deck")
        player2_deck.add_card(card)
    ball_x_pos = 7
    ball_y_pos = 10
    # BUTTONS ISTANCES
    game_on = 1
    # buttons_def()
    play_button = Button((300, 300), "Play cards", 55, "black on grey", style=0,
        command=on_click_play)
    player_deck_surf = create_player_deck_surf(player1_deck)
    play_deck_surf = create_play_deck_surf()
    played_card_1 = None
    played_card_2 = None
    current_deck_surf = create_current_deck_surf(current_deck.get_card())
    trash_deck_surf = create_trash_deck_surf()
    # board = create_board()
    football_field_surf = create_football_field_surf(ball_x_pos, ball_y_pos)
    clock = pygame.time.Clock()
    turn = "player1"
    # selected_piece = None
    player_card_selected = None
    player_card_selected_number = -1
    played_card_number = 1
    current_deck_card_selected = None
    play_player_card = False
    # drag_current_deck_card_to_trash = False
    drop_current_deck_card_to_trash = False
    # drop_pos = None
    while True:
        # piece, x, y = get_square_under_mouse(board)
        # current_deck_card = None
        current_deck_card_under_mouse = is_current_deck_card_under_mouse()
        player_card_under_mouse = is_player_card_under_mouse()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                # if piece != None:
                    # selected_piece = piece, x, y
                    # logger.debug("Selected piece at ( {},{} ) position".format(x,y))
                if current_deck_card_under_mouse:
                    current_deck_card_selected = current_deck.get_card()
                    if current_deck_card_selected is not None:
                        logger.debug(f"Selected current deck card with front image {current_deck_card_selected.front_img}")
                if player_card_under_mouse != -1:
                    if turn == "player1":
                        player_card_selected = player1_deck.get_card(player_card_under_mouse)
                        player_card_selected_number = player_card_under_mouse
                        # logger.info("Selected player1 card number {} with front image {}".format(player_card_selected_number, player_card_selected.front_img))
            if event.type == pygame.MOUSEBUTTONUP:
                # if drop_pos:
                    # piece, old_x, old_y = selected_piece
                    # board[old_y][old_x] = 0
                    # new_x, new_y = drop_pos
                    # board[new_y][new_x] = piece
                    # logger.debug("Drop piece at ( {},{} ) position".format(new_x,new_y))
                if play_player_card:
                    # trash_deck.add_card(player_card_selected)
                    if played_card_number == 1:
                        played_card_1 = player_card_selected
                        play_deck.add_card(player_card_selected)
                    if played_card_number == 2:
                        played_card_2 = player_card_selected
                        play_deck.add_card(player_card_selected)
                    played_card_number += 1

                    if turn == "player1":
                        logger.debug(f"Remove Player card number {player_card_selected_number}")
                        player1_deck.remove_card(player_card_selected_number)
                        logger.debug(f"Player have {len(player1_deck.card_list)} cards left")
                if drop_current_deck_card_to_trash:
                    trash_deck.add_card(current_deck_card_selected)
                    current_deck.remove_card()
                # selected_piece = None
                player_card_selected = None
                player_card_selected_number = -1
                current_deck_card_selected = None
                # drop_pos = None

        screen.fill(pygame.Color('grey'))
        if game_on:
            # if click_play:
            if play_button.pressed == 0:
                logger.info("Play action")
                # click_play = False
                while play_deck.get_nb_cards() > 0:
                    logger.info("Remove card from Play Deck")
                    play_card = play_deck.remove_card()
                    logger.info(f"Add card {play_card} to Trash Deck")
                    trash_deck.add_card(play_card)
                    logger.info(f"Remove card from current Deck with {current_deck.get_nb_cards()} cards")
                    first_draw_card = current_deck.remove_card()
                    # first_draw_card = current_deck.get_card()
                    # logger.info(first_draw_card.print())
                    current_deck_card_selected = current_deck.get_card()
                    if turn == "player1" and first_draw_card is not None:
                        logger.info(f"Add card {first_draw_card} to Player1 Deck")
                        player1_deck.add_card(first_draw_card)
                played_card_1 = None
                played_card_2 = None
                player_card_selected = None
                player_card_selected_number = -1
                played_card_number = 1
                current_deck_card_selected = None
                play_button.style = 0
                play_button.pressed = 1
            buttons.update()
            buttons.draw(screen)
        else:
            pygame.quit()
            sys.exit()
        buttons.draw(screen)
        if turn == "player1":
            screen.blit(player_deck_surf, PLAYER_DECK_POS)
        screen.blit(play_deck_surf, PLAY_DECK_POS)
        screen.blit(current_deck_surf, CURRENT_DECK_POS)
        screen.blit(trash_deck_surf, TRASH_DECK_POS)
        screen.blit(football_field_surf, FOOTBALL_FIELD_POS)
        if turn == "player1":
            update_player_deck_surf(player_deck_surf, player1_deck)
        draw_play_deck_card(play_deck_surf, played_card_1, played_card_2)
        draw_current_deck_card(current_deck_surf, current_deck.get_card())
        if len(trash_deck.card_list) == 0:
            draw_trash_deck_card(trash_deck_surf, None)
        else:
            draw_trash_deck_card(trash_deck_surf, trash_deck.get_card())
        football_field_surf = create_football_field_surf(ball_x_pos, ball_y_pos)
        # draw_pieces(screen, board, font, selected_piece)
        # draw_selector(screen, piece, x, y)
        play_player_card = is_player_card_to_drop(player_card_selected, played_card_number)
        if play_player_card:
            logger.info(f"Play player card {player_card_selected.print()} number {played_card_number}")
            play_button.style = 1
        drop_current_deck_card_to_trash = is_current_deck_card_to_drop(current_deck_card_selected)
        if drop_current_deck_card_to_trash:
            logger.info("Drop current card to trash")
        # drop_pos = draw_drag(screen, board, selected_piece, font)
        # if drop_pos is not None:
            # print("Drop Position is {}".format(drop_pos))

        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()
