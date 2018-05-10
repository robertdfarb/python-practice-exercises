import random
import math
import os


clear = lambda: os.system('cls')
#os.system('cls' if os.name == 'nt' else 'clear')

class Deck():

    SPADES = '\u2660'
    DIAMONDS = '\u25C6'
    HEARTS = '\u2764'
    CLUBS = '\u2618'

    suits = [SPADES, DIAMONDS, HEARTS, CLUBS]
    cards = []
    num_decks = 1

    def create_deck(self,num_decks=1):
        #Certain games may require more than one deck.
        self.num_decks=num_decks
        for deck_num in range(1,num_decks+1):
            for face in range(1,14):
                for suit in self.suits:
                    self.cards.append((face, suit))
        #print ("Deck created using {} sets of cards.".format({self.num_decks}))
        #print (self.SPADES)

    def shuffle(self,num=1):
        '''
        Shuffles Cards in the deck

            kwargs: Number of Times to Shuffle, Defaults to 1
        '''
        for shufflenum in range(1,num+1):
            for i in range (1,53*self.num_decks):
                shuffled_card = self.cards.pop(random.randint(0,51))
                self.cards.insert(0,shuffled_card)
            #print('shuffled {} time'.format(str(shufflenum)))

    def show_deck(self):
        print(self.cards)


class Game():

    game_list = ['Solitaire', 'Tic Tac Toe','Texas Holdem']
    terminal_size = os.get_terminal_size().columns
    border = ''.center(terminal_size,'*')
    game_selected = '0'
    current_game = ''
    playercount = 1
    playernames = []
    playerhands = {}

    def game_selection(self):
        for num, game in enumerate(self.game_list):
            print(str(num+1) +'. ' + game)

        self.game_selected = input("Enter Selection:   ")

        if self.game_selected == '3':
            current_game = TexasHoldem()
            return current_game
        else:
            print("\n \n Game not available yet, check back in 2019! \n \n ")
            return self.game_selection()
            clear()

    def welcome(self,game_name):
        print ("\n \n")
        print (self.border)
        print("Welcome to {game_name} press any key to begin".format(game_name=game_name).center(self.terminal_size))
        print(self.border + "\n")

    def player_setup(self):
        self.playercount = int(input("Enter number of players:  "))
        for i in range(1,self.playercount+1):
            player_name = input("Enter player number {}'s name:   ".format(i))
            self.playernames.append(player_name)

# Fix the betting
class Betting(Game):

    playerchips = {}
    playerbets = {}
    min_bet = 5


    def __init__(self):
        playerchips =  dict.fromkeys(self.playernames)

    small_blinds = 1
    big_blinds = 2

    def initialize_chips(self, startingamt=100):
        for player in self.playernames:
            self.playerchips[player] = startingamt

    def place_blinds(self, player, type):
        if amount.is_integer():
            if amount == 0:
                return
            if amount > self.playerchips[player]:
                print ("You only have {}, and you tried to bet {}, nice try big shot!".format(self.playerchips[player],amount).center(self.terminal_size))
            else:
                self.playerchips[player] =+ amount
                self.playerbets[player] =+ amount
        else:
            print ("Amount must be an integer!")

    def show_chips(self,player):
        print ("You have {chips} chips use them wisely! \n".format(chips=self.playerchips[player]))
        return self.playerchips[player]

    def place_bet(self, player):
        bet = int(input("Hi {p} enter the amount you would like to bet: ".format(p=player)))
        if bet == 0:
            return
        elif bet > self.playerchips[player]:
            print ("You only have {} chips, and you tried to bet {}, nice try big shot!".format(player,bet))
        elif bet < self.min_bet:
            print ("Sorry you must bet at least {}".format(self.min_bet))
        else:
            if player in self.playerbets:
                self.playerbets[player] =+ bet
                self.playerchips[player] = self.playerchips[player] - bet
                print("{p} bet {a} \n ".format(p=player, a=bet))
            else:
                self.playerbets[player] = bet
                self.playerchips[player] = self.playerchips[player] - bet
                print("{p} bet {a} \n ".format(p=player, a=bet))


    def distribute_winnings(self, *winner):
        # No Winner results in a distribution back to original players
        if winner == None:
            for player, allbets in playerbets.items():
                self.playerchips[player] =+ amount


class TexasHoldem(Betting,Deck):

    initialcards = 7
    max_players = 7
    times_to_shuffle = 3
    house_cards =  []

    def __str__(self):
        return "Texas Holdem!"

    def player_deal(self,num_cards=7):
        for num in range(num_cards):
            for player in self.playernames:
                popped_card = self.cards.pop()
                print(popped_card)
                if player in self.playerhands:
                    self.playerhands[player].append(popped_card)
                else:
                    self.playerhands[player] = [self.cards.pop()]

    def show_all_hands(self):
        for player, hand in self.playerhands.items():
            print (player)
            print (hand)

    def show_house(self):
        print (self.border)
        print("The Flop Cards Are: \n".center(self.terminal_size))
        for index, card in enumerate(self.house_cards):
            print (index+1, '.  ', card)
        print (self.border)

    def show_hand(self,player):
        print ("HERE IS YOUR HAND:\n")
        for index, card in enumerate(self.playerhands[player]):
            print (index+1, '.  ', card)
        print('\n')

    #need to see what the center cards are actually called!
    def house_deal(self,player,num_cards=3):
        for i in range(num_cards):
            self.house_cards.append(self.cards.pop())

    def play_card(self,player,cardindex):
        pass

    def initiate_game(self):
        self.create_deck()
        self.shuffle(self.times_to_shuffle)
        self.player_deal(self.initialcards)
        self.house_deal(3)
        self.initialize_chips()

    def play_round(self,num=1):
        for i in range(num):
            for player in self.playernames:
                self.show_house()
                print ("{player}'s turn \n".format(player=player).center(self.terminal_size))
                self.show_chips(player)
                self.show_hand(player)
                self.place_bet(player)
                clear()

    def play(self):
        self.play_round(3)
        self.house_deal(1)
        self.play_round(1)
        self.house_deal(1)
        print (show_all_hands)


def main():
    clear()
    game = Game()
    game.welcome('Robert\'s House of Cards!  When all you have is a terminal')
    current_game = game.game_selection()
    clear()
    current_game.welcome(current_game)
    current_game.player_setup()
    current_game.initiate_game()
    current_game.play()


if __name__ == '__main__':
    main()
