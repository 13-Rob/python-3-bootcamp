"""
BLACKJACK MILESTONE PROJECT #2
"""
from game_package.game_module import Deck, Player, Dealer

def main():
    """
    Blackjack main function.
    """
    deck = Deck()
    deck.shuffle()

    dealer = Dealer("Dealer", 1000000)

    op = 'y'
    # op = input('Dealer: Do you want to play Blackjack? Y/n\n').lower()

    if op.startswith('y'):
        # Game logic goes here
        # name = input("Dealer: What should we call you?\n")
        player = Player("Rob")

        # while game_on:
        print(f"Dealer: Your balance is ${player.balance}.00.")

        # Bets here: Default 10
        if player.bet() > 0:
            total_bet = player.bet() + dealer.bet()

        print(f"The total bet is ${total_bet}.00.")

        player.add_card(deck.deal_one())
        dealer.add_card(deck.deal_one())
        player.add_card(deck.deal_one())
        dealer.add_card(deck.deal_one())

        player.show_hand()
        dealer.show_hand()

        # Ask the player if they want to hit or stay
        op = input("Dealer: Hit or Stay? H/s\n").lower()

        while op.startswith('h'):
            player.add_card(deck.deal_one())
            player.show_hand()
            op = input("Delaer: Hit or Stay? H/s\n").lower()

        # Dealer decides if they want to hit or stay
        # Resolve game
        # Repeat

    print("Dealer: Bye-bye!")

if __name__=='__main__':
    main()
