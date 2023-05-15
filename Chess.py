class Board:
    def __init__(self):
        # Holds a 2d array of pieces
        self._board = [['R','N','B','Q','K','B','N','R'],
                        ['P','P','P','P','P','P','P','P'],
                            ['x','x','x','x','x','x','x','x'],
                                ['x','x','x','x','x','x','x','x'],
                                    ['x','x','x','x','x','x','x','x'],
                                        ['x','x','x','x','x','x','x','x'],
                                            ['P','P','P','P','P','P','P','P'],
                                                ['R','N','B','Q','K','B','N','R']]
    def get_board(self):
        return self._board

    def set_board(self, board):
        self._board = board

    def print_board(self):
        print("   a b c d e f g h   \n")
        for i in range(len(self._board)):
            row = str(8-i) + "  "
            for q in range(len(self._board)):
                row += self._board[i][q]
                row += " "
            row += " " + str(8-i)
            print(row)
        print("\n   a b c d e f g h   \n")

    def translate_move(self, pos):
        # returns an array of length 2, 0th value is the x axis, 1st value is the y axis
        translated_pos = [0,0]
        for i in range(len(pos)):
            match pos[i]:
                # translates to a number, 0 for 1 as to be used in the board array
                # Because the 2d array reads from top left to bottom right, its opposite to the board on the y axis.
                # Builds it in such a way to match the visual board to the array board
                # Could i have built the board differently?
                case 'a' | '8':
                    translated_pos[1-i] = 0
                case 'b' | '7':
                    translated_pos[1-i] = 1
                case 'c' | '6':
                    translated_pos[1-i] = 2
                case 'd' | '5':
                    translated_pos[1-i] = 3
                case 'e' | '4':
                    translated_pos[1-i] = 4
                case 'f' | '3':
                    translated_pos[1-i] = 5
                case 'g' | '2':
                    translated_pos[1-i] = 6
                case 'h' | '1':
                    translated_pos[1-i] = 7
                case _:
                    print("Invalid Input")
                    return None
        return translated_pos

    def move_piece(self, start_pos, end_pos):
        self._board[end_pos[0]][end_pos[1]] = self._board[start_pos[0]][start_pos[1]]
        self._board[start_pos[0]][start_pos[1]] = 'x'

    def legality_check(self,start_pos, end_pos):
        match self._board[start_pos[0]][start_pos[1]]:
            case 'R':
                if #line from start to end pos is empty then yes, check whether in check for all moves
            case _:
                print("Invalid Move for piece: " + self._board[start_pos[0]][start_pos[1]])
        self.move_piece(start_pos, end_pos)

class Piece:
    def __init__(self):
        _pos = [0,0]
        _colour = "white"
        _value = None
        _relative_value = None

    def move_piece(self):
        # Update Position
        None

def main():
    board = Board()
    game_over = False
    while not game_over:
        board.print_board()
        starting_pos = board.translate_move(input("Please enter starting square (in the form xN, where x is a lowercase letter a-h and N is a number 1-8):\n"))
        # Takes the user input and translates xN to a [N][M]
        ending_pos = board.translate_move(input("Please enter desired square (in the form xN, where x is a lowercase letter a-h and N is a number 1-8):\n"))
        board.move_piece(starting_pos, ending_pos)

if __name__ == "__main__":
    main()
