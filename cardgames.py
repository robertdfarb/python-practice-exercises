

class Deck():

    suit = ['HEARTS', 'SPADES', 'DIAMONDS','OTHER']
    cards = [[{i, j} for j in range(1,11)] for i in signs]

    print (deck)

'''
class TexasHoldem():
    pass
    #input("Welcome to Texas Holdem Press any key to begin")


class Games():

    game_list = ['Solitaire', 'Tic Tac Toe','Texas Holdem']
    selected = 0

    for num, game in enumerate(game_list):
            print(str(num+1) +'. ' + game)

    game_selected = input("Enter Selection:   ")

    if game_selected == 1:
        TexasHoldem()
    else:
        print ("Enter a valid selection")

'''
if __name__ == '__main__':

    print("Welcome to Roberts games, select a game you want to play?")
    #game = Games()
    Deck()


