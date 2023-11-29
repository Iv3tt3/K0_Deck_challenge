# Cards Deck Challenge

This is a Python challenge of creating a cards Deck.

The challenge is about:
1. building a complete deck using iteration
2. shuffling the cards. The chosen method is to got through the dech from the first to the last card and exchange its position with another postion randomly, without using functions that Python provides (shuffle).
3. dealing all cards to the players. The dealing is done card-by-car.
4. using TDD

Languages: English

## Spanish Deck Rules

The code uses Spanish version. It can be customized changing the environment variables (see section)

Spanish-suited cards have four suits: "Bastos" (b), "Copas" (c), "Espadas" (e) and "Oros" (o). In this game we will use the 40-card version. In this version, every suit has 10 cards: 6 numerical cards ranging from 2-7 and 4 that is the "As" (A), "Sota" (S), "Caballo" (C) and "Rey" (R), cavalier and king, usually assigned the respective numerical values of 1, 10, 11, and 12.

It is used a mix of both to descrive a playing card, for example the "As" of "Bastos" would be Ab or 6 of "Copas" would be 6c.

## Installation - Step by step

### Environment variables

1. Replicate `.env_template` file and rename it to `.env`
2. Provide the follwing variables:
    - SUITS: List of all suites. Example: SUITS=o,c,e,b (Use this format without space)
    - NUMBERS: List of cards of one suite. Example: NUMBERS=A,2,3,4,5,6,7,S,C,K (Use this format without space)
    - PLAYERS: Numbero fo players. Example: PLAYERS=4

### Libraries

To run the code is necessary to install the required libraries. Steps:

1. (Optional) Create and activate a virtual environment
2. Install all the dependencies from `requirements.txt` file by introducing the following:
```
pip install -r requirements.txt
```