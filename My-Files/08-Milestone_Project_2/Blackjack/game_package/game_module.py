"""
Game components module
"""
from random import shuffle

from colorama import Fore, Style

suits = ('♥️', '♦️', '♠️', '♣️')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
         'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

class Card:
    """
    Card class
    """
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __repr__(self):
        return f"{type(self).__name__}('{self.suit}', '{self.rank}')"

    def __str__(self):
        return f'{self.rank}{self.suit}'

class Deck:
    """
    Deck class
    """
    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                new_card = Card(suit, rank)
                self.all_cards.append(new_card)

    def __len__(self):
        return len(self.all_cards)

    def shuffle(self):
        """
        Shuffle all the cards in deck
        """
        shuffle(self.all_cards)

    def deal_one(self):
        """
        Deals one card to a player
        """
        return self.all_cards.pop()

class Player:
    """
    Player class
    """

    def __init__(self, name, balance=100):
        self.name = name
        self.balance = balance
        self.hand = []
        self.hand_value = 0

    def __str__(self):
        return f"The player has ${self.balance}.00."

    def withdraw(self, amount=10):
        """
        Withdraw money from the player's balance
        """
        if amount > self.balance:
            print("Sorry, but you don have sufficient funds.")
            return 0
        self.balance -= amount
        return amount

    def deposit(self, amount):
        """
        Deposit money to the player's balance
        """
        self.balance += amount

    def add_card(self, new_card):
        """
        Adds one card to the player's hand
        """
        self.hand.append(new_card)
        self.hand_value += new_card.value

        if self.hand_value > 21:
            for card in self.hand:
                if card.rank == 'Ace' and card.value == 11:
                    card.value = 1
                    break

    def show_hand(self):
        """
        Prints the player's current hand
        """
        print(self.name + "'s hand: ", end=Fore.RED)
        for c in self.hand:
            print(c, end=' ')
        print(f"= {self.hand_value}" + Style.RESET_ALL)

    def empty_hand(self):
        """
        Empties the player's hand
        """
        self.hand = []
        self.hand_value = 0

class Dealer(Player):
    """
    Dealer class, extends from Player
    """

    def show_hand(self):
        """
        Prints the dealer's current hand without the card facing down
        """
        print(self.name + "'s hand: ", end=Fore.BLUE)
        for c in self.hand:
            if self.hand.index(c) == 1:
                print("▓▓▓▓", end=' ')
            else:
                print(c, end=' ')
        print(Style.RESET_ALL)

    def show_full_hand(self):
        """
        Prints the dealer's full hand
        """
        print(f"{self.name}'s hand: ", end=Fore.BLUE)
        for c in self.hand:
            print(c, end=' ')
        print(f"= {self.hand_value}" + Style.RESET_ALL)
