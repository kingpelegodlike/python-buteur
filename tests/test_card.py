import pytest
from card import Card

def test_card_unknown():
    card = Card("unknown_card.png")
    assert not hasattr(card, "type")
    assert not hasattr(card, "color")
    assert not hasattr(card, "first_move_list")
    assert not hasattr(card, "second_move_list")

def test_card_unknown_type():
    card = Card("card_unknown.png")
    assert not hasattr(card, "type")
    assert not hasattr(card, "color")
    assert not hasattr(card, "first_move_list")
    assert not hasattr(card, "second_move_list")

def test_card_attacker_one_direction():
    card = Card("card_attacker_red_at3l.png")
    assert card.type == "attacker"
    assert card.color == "red"
    assert card.first_move_list == [(-3, 0)]
    assert not hasattr(card, "second_move_list")

def test_card_attacker_two_directions():
    card = Card("card_attacker_blue_at3l3dl3s3dr3r_at2l2dl2s2dr2r.png")
    assert card.type == "attacker"
    assert card.color == "blue"
    assert card.first_move_list == [(-3, 0), (-3, 3), (0, 3), (3, 3), (3, 0)]
    assert card.second_move_list == [(-2, 0), (-2, 2), (0, 2), (2, 2), (2, 0)]

def test_card_freekick_one_direction():
    card = Card("card_freekick_at1l1dl1s1dr1r.png")
    assert card.type == "freekick"
    assert card.color == None
    assert card.first_move_list == [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0)]
    assert not hasattr(card, "second_move_list")

def test_card_freekick_two_directions():
    card = Card("card_freekick_at1l1dl1s1dr1r_at2l2dl2s2dr2r.png")
    assert card.type == "freekick"
    assert card.color == None
    assert card.first_move_list == [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0)]
    assert card.second_move_list == [(-2, 0), (-2, 2), (0, 2), (2, 2), (2, 0)]

def test_card_corner():
    card = Card("card_corner_red.png")
    assert card.type == "corner"
    assert card.color == "red"
    assert not hasattr(card, "first_move_list")
    assert not hasattr(card, "second_move_list")

def test_card_goalkeeper_one_direction():
    card = Card("card_goalkeeper_at4s.png")
    assert card.type == "goalkeeper"
    assert card.color == None
    assert card.first_move_list == [(0, 4)]
    assert not hasattr(card, "second_move_list")

def test_card_goalkeeper_two_directions():
    card = Card("card_goalkeeper_at1l1dl1s1dr1r_at4l4dl4s4dr4r.png")
    assert card.type == "goalkeeper"
    assert card.color == None
    assert card.first_move_list == [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0)]
    assert card.second_move_list == [(-4, 0), (-4, 4), (0, 4), (4, 4), (4, 0)]