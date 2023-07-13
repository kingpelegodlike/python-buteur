import pygame
import os
import logging

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

from card import Card
from deck import Deck

TILESIZE = 16
PLAYER_DECK_POS = (10, 370)
CURRENT_DECK_POS = (300, 30)
TRASH_DECK_POS = (400, 30)
FOOTBALL_FIELD_POS = (10, 10)

def create_player_deck_surf(player_deck):
    player_deck_surf = pygame.Surface(size=(10+(65+10)*8, 123))
    # rect_list = []
    for i in range(0, len(player_deck.card_list)):
        rect = pygame.Rect(10+(65+10)*i, 10, 65, 103)
        card_obj = player_deck.get_card(i)
        card_img = pygame.image.load(os.path.join("img", "{}.png".format(card_obj.front_img)))
        player_deck_surf.blit(card_img, rect)
    return player_deck_surf

def create_current_deck_surf(last_card):
    current_deck_surf = pygame.Surface((65, 103))
    rect = pygame.Rect(0, 0, 65, 103)
    last_card_img = pygame.image.load(os.path.join("img", "{}.png".format(last_card.front_img)))
    current_deck_surf.blit(last_card_img, rect.topleft)
    return current_deck_surf

def create_trash_deck_surf():
    trash_deck_durf = pygame.Surface((65, 103))
    rect = pygame.Rect(0, 0, 65, 103)
    # last_card_img = pygame.image.load(os.path.join("img", "{}.png".format(last_card.front_img)))
    pygame.draw.rect(trash_deck_durf,"red",rect,0)
    return trash_deck_durf

def create_football_field_surf():
    football_field_surf = pygame.Surface((TILESIZE*16, TILESIZE*22))
    dark = False
    for y in range(22):
        for x in range(16):
            rect = pygame.Rect(x*TILESIZE, y*TILESIZE, TILESIZE, TILESIZE)
            # football_field_piece_img = pygame.image.load(os.path.join("img", "football_field_x0_y0.png"))
            try:
                football_field_piece_img = pygame.image.load(os.path.join("img", "football_field_x{}_y{}.png".format(x, y)))
            except FileNotFoundError as fnfe:
                # logger.error(fnfe)
                football_field_piece_img = pygame.image.load(os.path.join("img", "football_field_x0_y0.png"))
            football_field_piece_img = pygame.transform.scale(football_field_piece_img, (TILESIZE, TILESIZE)) 
            # pygame.draw.rect(football_field_surf, pygame.Color('darkgrey' if dark else 'beige'), rect)
            football_field_surf.blit(football_field_piece_img, rect.topleft)
            dark = not dark
        dark = not dark
    return football_field_surf

def is_player_card_under_mouse():
    mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
    mouse_pos_x = mouse_pos[0]
    mouse_pos_y = mouse_pos[1]
    logger.debug("Check mouse pos is ({},{}) with player cards".format(mouse_pos_x, mouse_pos_y))
    player_card_under_mouse = -1
    for i in range (0, 8):
        min_pos_x_expected =  10+(65+10)*i
        max_pos_x_expected = min_pos_x_expected + 65
        if mouse_pos_x >= min_pos_x_expected and mouse_pos_x < max_pos_x_expected and mouse_pos_y >= 380 and mouse_pos_y < 483:
            logger.debug("found under card number '{}'".format(i))
            player_card_under_mouse = i
    return player_card_under_mouse

def is_current_deck_card_under_mouse():
    mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
    mouse_pos_x = mouse_pos[0]
    mouse_pos_y = mouse_pos[1]
    logger.debug("mouse pos is ({},{})".format(mouse_pos_x, mouse_pos_y))
    if mouse_pos_x >= 300 and mouse_pos_x < 365 and mouse_pos_y >= 30 and mouse_pos_y < 133:
        return True
    else:
        return False

def is_trash_deck_card_under_mouse():
    mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
    mouse_pos_x = mouse_pos[0]
    mouse_pos_y = mouse_pos[1]
    logger.debug("Check mouse pos ({},{}) with trash".format(mouse_pos_x, mouse_pos_y))
    if mouse_pos_x >= 400 and mouse_pos_x < 465 and mouse_pos_y >= 30 and mouse_pos_y < 133:
        return True
    else:
        return False

def get_square_under_mouse(board):
    mouse_pos = pygame.Vector2(pygame.mouse.get_pos()) - BOARD_POS
    x, y = [int(v // TILESIZE) for v in mouse_pos]
    try: 
        if x >= 0 and y >= 0: return (board[y][x], x, y)
    except IndexError: pass
    return None, None, None

def create_board():
    board = []
    for y in range(8):
        board.append([])
        for x in range(8):
            board[y].append(None)

    for x in range(0, 8):
        board[1][x] = ('black', 'pawn')
    for x in range(0, 8):
        board[6][x] = ('white', 'pawn') 

    return board

def draw_current_deck_card(surface, last_card):
    rect = pygame.Rect(0, 0, 65, 103)
    if last_card is not None:
        last_card_img = pygame.image.load(os.path.join("img", "{}.png".format(last_card.front_img)))
        surface.blit(last_card_img, rect.topleft)
    else:
        pygame.draw.rect(surface,"red",rect,0)

def draw_trash_deck_card(surface, last_card):
    rect = pygame.Rect(0, 0, 65, 103)
    if last_card is not None:
        last_card_img = pygame.image.load(os.path.join("img", "{}.png".format(last_card.front_img)))
        surface.blit(last_card_img, rect.topleft)
    else:
        pygame.draw.rect(surface,"red",rect,0)


def draw_pieces(screen, board, font, selected_piece):
    sx, sy = None, None
    if selected_piece:
        piece, sx, sy = selected_piece

    for y in range(8):
        for x in range(8): 
            piece = board[y][x]
            if piece:
                selected = x == sx and y == sy
                color, type = piece
                s1 = font.render(type[0], True, pygame.Color('red' if selected else color))
                s2 = font.render(type[0], True, pygame.Color('darkgrey'))
                pos = pygame.Rect(BOARD_POS[0] + x * TILESIZE+1, BOARD_POS[1] + y * TILESIZE + 1, TILESIZE, TILESIZE)
                screen.blit(s2, s2.get_rect(center=pos.center).move(1, 1))
                screen.blit(s1, s1.get_rect(center=pos.center))

def draw_selector(screen, piece, x, y):
    if piece != None:
        rect = (BOARD_POS[0] + x * TILESIZE, BOARD_POS[1] + y * TILESIZE, TILESIZE, TILESIZE)
        pygame.draw.rect(screen, (255, 0, 0, 50), rect, 2)

def is_player_card_to_drop(player_card_selected):
    if player_card_selected is not None:
        if is_trash_deck_card_under_mouse():
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

def draw_drag(screen, board, selected_piece, font):
    if selected_piece:
        piece, x, y = get_square_under_mouse(board)
        if x != None:
            rect = (BOARD_POS[0] + x * TILESIZE, BOARD_POS[1] + y * TILESIZE, TILESIZE, TILESIZE)
            pygame.draw.rect(screen, (0, 255, 0, 50), rect, 2)
            logger.debug("draw_drag draw rect with (0, 255, 0, 50) color at {}".format(rect))

        color, type = selected_piece[0]
        s1 = font.render(type[0], True, pygame.Color(color))
        s2 = font.render(type[0], True, pygame.Color('darkgrey'))
        pos = pygame.Vector2(pygame.mouse.get_pos()) - BOARD_POS
        expected_pos = [int(v // TILESIZE) for v in pos]
        if abs(expected_pos[0] - selected_piece[1]) > 0:
            expected_pos[0] = selected_piece[1]
            x = expected_pos[0]
        if expected_pos[1] - selected_piece[2] > 2:
            expected_pos[1] = selected_piece[2] + 2
            y = y + 2
        if expected_pos[1] - selected_piece[2] < -2:
            expected_pos[1] = selected_piece[2] - 2
            y = y - 2
        # expected_pos = ((BOARD_POS[0] + (BOARD_POS[0]/2) + (expected_pos[0]*TILESIZE)), (BOARD_POS[1] + (BOARD_POS[1]/2) + (expected_pos[1]*TILESIZE)))
        # expected_pos = (21.0,236.0)
        print("pos={},{}, expected_pos={},{}, selected_piece pos ={}, {}" \
                .format(pos[0], pos[1], expected_pos[0], expected_pos[1], selected_piece[1], selected_piece[2]))
        # screen.blit(s2, s2.get_rect(center=expected_pos + (1, 1)))
        screen.blit(s1, s1.get_rect(center=expected_pos))
        selected_rect = pygame.Rect(BOARD_POS[0] + selected_piece[1] * TILESIZE, BOARD_POS[1] + selected_piece[2] * TILESIZE, TILESIZE, TILESIZE)
        expected_rect = pygame.Rect(BOARD_POS[0] + expected_pos[0] * TILESIZE, BOARD_POS[1] + expected_pos[1] * TILESIZE, TILESIZE, TILESIZE)
        pygame.draw.line(screen, pygame.Color('red'), selected_rect.center, expected_rect.center)
        logger.debug("draw_drag draw line red collored starting at {} pos and ending at {} pos".format(selected_rect.center, pygame.Vector2((BOARD_POS[0] + x * TILESIZE, BOARD_POS[1] + y * TILESIZE))))
        # return (x, y)
        return (expected_pos[0], expected_pos[1])

def main():
    pygame.init()
    font = pygame.font.SysFont('', 32)
    screen = pygame.display.set_mode((640, 540))
    player1_deck = Deck()
    player2_deck = Deck()
    current_deck = Deck()
    trash_deck = Deck()
    card = Card("front_blue_at3l")
    player1_deck.add_card(card)
    current_deck.add_card(card)
    card = Card("front_blue_at4s_1")
    player1_deck.add_card(card)
    player1_deck.add_card(card)
    player1_deck.add_card(card)
    player1_deck.add_card(card)
    player1_deck.add_card(card)
    player1_deck.add_card(card)
    player1_deck.add_card(card)
    current_deck.add_card(card)
    player_deck_surf = create_player_deck_surf(player1_deck)
    current_deck_surf = create_current_deck_surf(current_deck.get_card())
    trash_deck_surf = create_trash_deck_surf()
    # board = create_board()
    football_field_surf = create_football_field_surf()
    clock = pygame.time.Clock()
    turn = "player1"
    selected_piece = None
    player_card_selected = None
    current_deck_card_selected = None
    drop_player_card_to_trash = False
    drag_current_deck_card_to_trash = False
    drop_pos = None
    while True:
        # piece, x, y = get_square_under_mouse(board)
        current_deck_card = None
        current_deck_card_under_mouse = is_current_deck_card_under_mouse()
        player_card_under_mouse = is_player_card_under_mouse()
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                return
            if e.type == pygame.MOUSEBUTTONDOWN:
                pass
                # if piece != None:
                    # selected_piece = piece, x, y
                    # logger.debug("Selected piece at ( {},{} ) position".format(x,y))
                if current_deck_card_under_mouse:
                    current_deck_card_selected = current_deck.get_card()
                    if current_deck_card_selected is not None:
                        logger.debug("Selected current deck card with front image {}".format(current_deck_card_selected.front_img))
                if player_card_under_mouse != -1:
                    if turn == "player1":
                        player_card_selected = player1_deck.get_card(player_card_under_mouse)
                        logger.info("Selected player1 card with front image {}".format(player_card_selected.front_img))
            if e.type == pygame.MOUSEBUTTONUP:
                if drop_pos:
                    # piece, old_x, old_y = selected_piece
                    # board[old_y][old_x] = 0
                    new_x, new_y = drop_pos
                    # board[new_y][new_x] = piece
                    # logger.debug("Drop piece at ( {},{} ) position".format(new_x,new_y))
                if drop_player_card_to_trash:
                    trash_deck.add_card(player_card_selected)
                    if turn == "player1":
                        player1_deck.remove_card(player_card_under_mouse)
                if drop_current_deck_card_to_trash:
                    trash_deck.add_card(current_deck_card_selected)
                    current_deck.remove_card()
                selected_piece = None
                player_card_selected = None
                current_deck_card_selected = None
                drop_pos = None

        screen.fill(pygame.Color('grey'))
        if turn == "player1":
            screen.blit(player_deck_surf, PLAYER_DECK_POS)
        screen.blit(current_deck_surf, CURRENT_DECK_POS)
        screen.blit(trash_deck_surf, TRASH_DECK_POS)
        screen.blit(football_field_surf, FOOTBALL_FIELD_POS)
        draw_current_deck_card(current_deck_surf, current_deck.get_card())
        if len(trash_deck.card_list) == 0:
            draw_trash_deck_card(trash_deck_surf, None)
        else:
            draw_trash_deck_card(trash_deck_surf, trash_deck.get_card())
        # draw_pieces(screen, board, font, selected_piece)
        # draw_selector(screen, piece, x, y)
        drop_player_card_to_trash = is_player_card_to_drop(player_card_selected)
        if drop_player_card_to_trash:
            logger.info("Drop player card to trash")
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