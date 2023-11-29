from models import Deck
import os
from dotenv import load_dotenv
import pytest

load_dotenv

# Test to check if deck is created
def test_create_deck():
    deck = Deck()

    assert len(deck.playing_cards) == 40
    assert "Ac" in deck.playing_cards
    assert "7o" in deck.playing_cards
    assert "Kb" in deck.playing_cards
    assert "4e" in deck.playing_cards

def test_create_players():
    deck = Deck()

    assert len(deck.players)== int(os.getenv('PLAYERS'))
    assert deck.players['player0'] == []

# Test to check if deck is mixed
def test_mix_deck():
    deck = Deck()
    deck.playing_cards = []
    ordened_deck = deck.get_playing_cards()
    deck.shuffle()

    assert len(deck.playing_cards) == 40
    assert deck.playing_cards != ordened_deck

def test_deal_cards():
    deck = Deck()
    deck.deal_cards()
    players = int(os.getenv('PLAYERS'))
    if players % 2 == 0:
        assert len(deck.players['player0']) == len(deck.playing_cards) / players
    else:
        assert deck.discard_cards != []
    for i in range(players):
        assert deck.players['player'+str(i)][0] == deck.playing_cards[i]