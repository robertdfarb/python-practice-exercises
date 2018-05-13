import argparse
import random


class Game:

    difficulty = 'E'
    size = 10
    board_size = size*size
    won_board = []

    board = []
    choices = []

    if difficulty == 'E':
        matches = int(size / 5)

        '''
    elif difficulty == 'M':
        matches = int(size / 4)
    elif difficulty == 'H':
        matches = int(size / 2)
        '''


    def set_choices(self):
        for i in range(int(self.board_size/self.matches)):
            self.choices.append(i)
        self.choices.extend(self.choices*(self.matches-1))

    def create_board(self):

        for i in range(self.board_size):
            number = random.randint(0, len(self.choices)-1)
            card = self.choices[number]
            self.board.append(card)

        for i in range(self.board_size):
            self.won_board.append('x')

    def show_board(self):

        for x in range(0, self.board_size, 10):
            print(self.won_board[x:x+10])

    def flip_cards(self):

        self.show_board()

        x = input("Enter Row Number to flip")
        y = input("Enter Column Number to flip")
        x = str(int(x) - 1)
        y = str(int(y)- 1)
        xy1 = int(x+y)
        square_one = self.board[xy1]
        print (square_one)
        x = input("Enter Row Number to flip")
        y = input("Enter Column Number to flip")
        x = str(int(x) - 1)
        y = str(int(y) - 1)
        xy2 = int(x+y)
        square_two = self.board[xy2]
        print(square_two)
        if square_one is square_two:
            print ('Congrats a match was found')
            self.won_board[xy1] = square_one
            self.won_board[xy2] = square_two
            self.check_winner()

    def check_winner(self):
        for cardno, card in enumerate(self.won_board):
            if card == 'x':
                return self.flip_cards()

    def play_game(self):
        pass



if __name__ == '__main__':
    game = Game()
    game.set_choices()
    game.create_board()
    game.flip_cards()
    game.check_winner()
