class ConnectFour(object):
    MAX_ROWS = 6
    MAX_COLS = 7

    def __init__(self):
        self.players = ['X', 'O']
        self.new_game()
    
    def new_game(self):
        self.board = [[] for _ in range(self.MAX_COLS)]
        self.current_player = 0
        self.turn = 1

    def play(self, column):
        col_index, _ = self.cell_indices(column + '1')
        self.board[col_index].append(self.players[self.current_player])
        win = self.check_for_win(column + str(len(self.board[col_index])))
        if win:
            print('Player {} wins!'.format(self.players[self.current_player]))
            print('Turn {} with {}'.format(self.turn, ', '.join(win)))
            self.print_board()
            return True
        self.current_player = (self.current_player + 1) % 2
        if self.current_player == 0:
            self.turn += 1
        return False

    def check_for_win(self, cell):
        column, row = self.cell_indices(cell)
        player = self.get_cell(cell)
        directions = [(1,0), (0,1), (1,1), (1,-1)]
        for d in directions:
        # Check / diagonal
            win_cells = [cell.upper()]
            plus, minus = True, True
            for i in range(1, 5):
                if plus == minus == False:
                    break
                if plus:
                    if self.get_cell((column + i*d[0], row + i*d[1])) == player:
                        win_cells.append(self.cell_name(column + i*d[0], row + i*d[1]))
                    else:
                        plus = False
                if minus:
                    if self.get_cell((column - i*d[0], row - i*d[1])) == player:
                        win_cells.append(self.cell_name(column - i*d[0], row - i*d[1]))
                    else:
                        minus = False
            if len(win_cells) >= 4:
                return sorted(win_cells)

    def cell_name(self, column, row):
        return chr(column + ord('A')) + str(row + 1)

    def cell_indices(self, cell_name):
        column, row = list(cell_name)
        return ord(column.upper()) - ord('A'), int(row) - 1

    def get_cell(self, cell):
        if isinstance(cell, str) or isinstance(cell[0], str):
            cell = self.cell_indices(cell)
        column, row = cell
        if column < 0 or row < 0:
            return None
        try:
            return self.board[column][row]
        except IndexError:
            return '.'

    def print_board(self):
        print('    a b c d e f g')
        for row in range(6, 0, -1):
            rowtext = str(row) + '  '
            for column in 'abcdefg':
                rowtext += ' ' + self.get_cell((column, row))
            print(rowtext)

if __name__ == '__main__':
    game = ConnectFour()
    moves = '''C  d
    D  d
    D  b
    C  f
    C  c
    B  a
    A  d
    G  e
    E  g'''
    
    for move in moves.split():
        if game.play(move):
            break
    
    print()
    
    game.new_game()
    moves = '''D  d
    D  c    
    C  c    
    C  c
    G  f
    F  d
    F  f
    D  f
    A  a
    E  b
    E  e
    B  g
    G  g
    B  a'''
    
    for move in moves.split():
        if game.play(move):
            break