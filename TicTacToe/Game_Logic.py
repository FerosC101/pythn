import random

class TicTacToe:
    def __init__(self, current_user, user_manager):
        self.board = [ ' ' for _ in range(9)]
        self.current_user = current_user
        self.user_manager = user_manager
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i * 3:(i + 1) *3] for i in range(3)]:
            print('| ' + '| '.join(row) + '| ')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print('| ' + '| '.join(row) + '| ')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        row_ind = square // 3
        row = self.board[row_ind * 3:(row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False

    def play_game(self):
        print('Welcome to Tic Tac Toe!')
        self.print_board_nums()

        letter = 'X'
        while self.empty_squares():
            if self.num_empty_squares() == 0:
                break

            if letter == 'X':
                square = self.get_move(letter)
            else:
                square = random.choice(self.available_moves())
            
            if self.make_move(square, letter):
                print(f'{letter} makes a move to square {square}')
                self.print_board()
                print('')

                if self.current_winner:
                    print(f'{letter} wins!')
                    if letter == 'X':
                        self.user_manager.update_record(self.current_user, 'win')
                    else:
                        self.user_manager.update_record(self.current_user, 'loss')
                    return

                letter = 'O' if letter == 'X' else 'X'
        print('It\'s a tie!')

    def get_move(self, letter):
        valid_square = False
        val = None
        while not valid_square:
            square = input(f'{letter}\'s turn. Input move (0-8): ')
            try:
                val = int(square)
                if val not in self.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val