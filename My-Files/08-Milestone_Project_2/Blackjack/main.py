"""
BLACKJACK MILESTONE PROJECT #2
"""
import os

from colorama import Fore, Style

from game_package.game_module import Deck, Player, Dealer

def clear():
    """
    Clear the terminal screen
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def det_winner(player, dealer):
    """
    Determines who won, player or dealer
    """
    if player.hand_value > dealer.hand_value:
        if player.hand_value <= 21:
            return 1
        if dealer.hand_value <= 21:
            return -1

    if player.hand_value < dealer.hand_value:
        if dealer.hand_value <= 21:
            return -1
        if player.hand_value <= 21:
            return 1

    return 0

def main():
    """
    Blackjack main function.
    """

    dealer = Dealer("Dealer", 1000000)

    op = 'y'
    # Game logic goes here
    # name = input("Dealer: What should we call you?\n")
    player = Player("Rob")

    while op.startswith('y'):
        clear()
        deck = Deck()
        deck.shuffle()
        player.empty_hand()
        dealer.empty_hand()

        print("Dealer: Your balance is "
            + Fore.GREEN + f"${player.balance}.00"
            + Style.RESET_ALL + ".")

        # Bets here: Default 10
        if player.balance > 0:
            total_bet = player.withdraw() + dealer.withdraw()

        print("The total bet is "
            + Fore.GREEN + f"${total_bet}.00"
            + Style.RESET_ALL + ".")

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

        player.show_hand()

        # Dealer decides if they want to hit or stay
        if (dealer.hand_value < 21 and
                player.hand_value > dealer.hand_value and
                player.hand_value <= 21):
            op = 'h'
        else:
            op = 's'

        while op.startswith('h'):
            dealer.add_card(deck.deal_one())
            dealer.show_hand()
            if (dealer.hand_value < 21 and
                    player.hand_value > dealer.hand_value and
                    player.hand_value <= 21):
                op = 'h'
            else:
                op = 's'

        # Resolve game
        player.show_hand()
        dealer.show_full_hand()

        winner = det_winner(player, dealer)

        if winner == 1:
            print("Dealer: *sigh* You won")
            player.deposit(total_bet)
        elif winner == -1:
            print("Dealer: I won")
            dealer.deposit(total_bet)
        else:
            print("Dealer: It's a tie...")
            player.deposit(total_bet/2)
            dealer.deposit(total_bet/2)

        total_bet = 0

        op = input("Do you want to play again? (Y/n)\n").lower()

        # Repeat

if __name__=='__main__':
    main()
