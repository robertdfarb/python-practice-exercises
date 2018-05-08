import random

class Deck:

    suits = ['HEARTS', 'SPADES', 'DIAMONDS', 'CLUBS']
    cards = []
    #cards = [[(suit, face) for face in range(1,11)] for suit in suits]
    def create_deck(self):
        for face in range(1,14):
            for suit in self.suits:
                self.cards.append((face, suit))
        print ("Deck Created")

    def shuffle(self,num=1):
        '''
        Shuffles Cards in the deck

            kwargs: Number of Times to Shuffle, Defaults to 1
        '''
        for shufflenum in range(1,num+1):
            for i in range (1,53):
                shuffled_card = self.cards.pop(random.randint(0,51))
                self.cards.insert(0,shuffled_card)
            print('shuffled {} time'.format(str(shufflenum)))

    def show_deck(self):
        print(self.cards)


class Game():

    game_list = ['Solitaire', 'Tic Tac Toe','Texas Holdem']
    game_selected = '0'
    current_game = ''

    def game_selection(self):
        for num, game in enumerate(self.game_list):
            print(str(num+1) +'. ' + game)

        self.game_selected = input("Enter Selection:   ")

        if self.game_selected == '3':
            current_game = TexasHoldem()
            return current_game
        else:
            return print("Game not available yet, check back in 2019!")

    def welcome(self,game_name):
        print ("\n \n")
        print("************************************************************************")
        print("          Welcome to {game_name} press any key to begin".format(game_name=game_name))
        print("************************************************************************ \n")
        input()



class TexasHoldem(Game,Deck):

    def __str__(self):
        return "Texas Holdem!"

    def play(self):


def main():

    game = Game()
    game.welcome('Robert\'s House of Cards')
    current_game = game.game_selection()
    current_game.welcome(current_game)
    current_game.create_deck()
    current_game.shuffle(3)
    current_game.show_deck()


if __name__ == '__main__':
    main()
