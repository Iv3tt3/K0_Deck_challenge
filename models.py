#Use dotenv library to import env variables and import os
from dotenv import load_dotenv
import os
import random

#Load env varibales from file .env
load_dotenv()


class Deck():
    def __init__(self):
        #Set suits and numbers form .env
        self.suits = os.getenv('SUITS').split(',')
        self.numbers = os.getenv('NUMBERS').split(',')
        #Create an empty list to store all deck cards and a dict to store players
        self.playing_cards = [] 
        self.discard_cards = []
        self.players={}
        #Call the method to fill the list playing_cards and the dict players
        self.get_playing_cards()
        self.get_players()

    def get_playing_cards(self):
        #Generate playing cards by addinng all suits of each numbers
        for suit in self.suits:
            for number in self.numbers:
                card = number + suit
                self.playing_cards.append(card)

    def get_players(self):
        players = int(os.getenv('PLAYERS'))
        for i in range(players):
            self.players["player"+str(i)] = []

    def shuffle(self):
        #Shuffle the playing cards using random library and an index to swap the cards 
        for i in range(len(self.playing_cards)):
            p = random.randrange(0,len(self.playing_cards),1)
            self.playing_cards[i], self.playing_cards[p] = self.playing_cards[p], self.playing_cards[i] 

    def deal_cards(self):
        cards_per_player = len(self.playing_cards) // int(os.getenv('PLAYERS'))
        discard_cards = len(self.playing_cards) - cards_per_player * int(os.getenv('PLAYERS'))
        if discard_cards >0:
            self.discard_cards = self.playing_cards[-discard_cards:]
            self.playing_cards = self.playing_cards[:-discard_cards]
        i = 0
        for card in self.playing_cards:
            if i >= int(os.getenv('PLAYERS')):
                i=0
            self.players["player"+str(i)].append(card)
            i += 1
