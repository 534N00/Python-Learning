# Class for making a Tic-Tac-Toe game
class TicTacToe:
    def __init__(self):
        start = input("Type something for P1 to play O and nothing for X: ")
        if start:
            print("P1 will be O")
            self.p1 = 'O'
            self.p2 = 'X'
        else:
            print("P1 will be X")
            self.p1 = 'X'
            self.p2 = 'O'
       
        self.board = []
        for _ in range(3):
            inner = [" "] * 3
            self.board.append(inner)
        self.print_board()
        ''' 
        You can do this too of course:
        self.board = [[None, None, None],
                      [None, None, None],
                      [None, None, None]]
        '''
        turn = 1
        check = self.check_for_winner() 
        while check is None:
            self.make_move(turn)
            self.print_board()
            turn += 1
            check = self.check_for_winner() 
        else:
            print(check)

    def make_move(self, turn):
        coord_str = input("Select row & col to place (CSV form): ")
        coord_list = coord_str.split(',')
        coord_tuple = tuple([int(x) for x in coord_list])
        if len(coord_tuple) != 2: raise ValueError('Not 2 values')
        if coord_tuple[0] not in range(0,3) or coord_tuple[1] not in range(0,3):
            raise ValueError('Value in tupple not in range')
        # If P1 turn
        if turn % 2 == 1:
            self.board[coord_tuple[0]][coord_tuple[1]] = self.p1
        else:
            self.board[coord_tuple[0]][coord_tuple[1]] = self.p2

    def check_for_winner(self):
        winner = []
        winner.append(self.check_rows())
        winner.append(self.check_cols())
        winner.append(self.check_diags())
        if 'X' in winner:
            return 'The winner is X'
        if 'O' in winner:
            return 'The winner is O'

    def check_rows(self):
        for row in self.board:
            if row[0] == row[1] and row[1] == row[2]: return row[0]

    def check_cols(self):
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col]:
                return self.board[0][col]

    def check_diags(self):
        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return self.board[0][2]
    
    def print_board(self):
        print('* --------------------- *')
        print("   0   1   2")
        print('0  ' + str(self.board[0][0]) + ' | ' + str(self.board[0][1]) + ' | ' + str(self.board[0][2]))
        print('  ------------')
        print('1  ' + str(self.board[1][0]) + ' | ' + str(self.board[1][1]) + ' | ' + str(self.board[1][2]))
        print('  ------------')
        print('2  ' + str(self.board[2][0]) + ' | ' + str(self.board[2][1]) + ' | ' + str(self.board[2][2]))