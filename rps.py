# Rock Paper Scissors game

moves = ['rock', 'paper', 'scissors']


class Player:
    def __init__(self):
        self.counter = 0
        self.my_move = ""
        self.their_move = ""

    def move(self):
        return 'rock'

    def reset(self):
        self.counter = 0

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        while True:
            move = input("What's your move? ").lower()
            if move in moves:
                self.counter += 1
                return move
            else:
                print("Wrong input! Try again...")


class ReflectPlayer(Player):
    def move(self):
        if self.counter < 1:
            self.counter += 1
            return random.choice(moves)
        return self.their_move


class CyclePlayer(Player):
    counter = 0
    last_index = 0

    def move(self):
        if self.counter < 1:
            self.counter += 1
            first_choice = random.choice(moves)
            self.last_index = moves.index(first_choice)
            return first_choice
        else:
            self.counter += 1
            self.last_index += 1
            return moves[self.last_index % len(moves)]


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    score1 = 0
    score2 = 0

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def reset(self):
        self.p1.reset()
        self.p2.reset()

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}\nPlayer 2: {move2}")
        if move1 == move2:
            print(f"A tie! \nScore; {self.score1}:{self.score2}")
        elif beats(move1, move2) is True:
            self.score1 += 1
            print(f"Player 1 wins this round \nScore;"
                  f"{self.score1}:{self.score2}")
        else:
            self.score2 += 1
            print(f"Player 2 wins this round \nScore;"
                  f"{self.score1}:{self.score2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print()
        print("Game start!")
        for _ in range(5):
            print(f"\n\nRound {_ + 1}:")
            self.play_round()
        if self.score1 > self.score2:
            print("PLAYER 1 WINS!")
        elif self.score1 == self.score2:
            print("THAT'S A DRAW.")
        else:
            print("PLAYER 2 WINS!")
        print(f'Final score {self.score1}:{self.score2}')
        self.score1 = 0
        self.score2 = 0
        again = input('Will you like to play again? (Enter y or n) ')
        if again == 'y':
            game.reset()
            game.play_game()
        else:
            print('Game over!')


if __name__ == '__main__':
    import random

    game = Game(HumanPlayer(), CyclePlayer())
    # game = Game(HumanPlayer(), ReflectPlayer())
    # game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
