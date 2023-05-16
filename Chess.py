class Board:
    def __init__(self):
        self._turn_counter = 0
        # Holds a 2d array of pieces
        self._board = [[Piece([0,0], 'R', "Black", 5), Piece([0,1], 'N', "Black", 3), Piece([0,2], 'B', "Black", 3.5), Piece([0,3], 'Q', "Black", 9), Piece([0,4], 'K', "Black", 1000), Piece([0,5], 'B', "Black", 3.5), Piece([0,6], 'N', "Black", 3), Piece([0,7], 'R', "Black", 5)],
                        [Piece([1,0], 'P', "Black", 1), Piece([1,1], 'P', "Black", 1), Piece([1,2], 'P', "Black", 1), Piece([1,3], 'P', "Black", 1), Piece([1,4], 'P', "Black", 1), Piece([1,5], 'P', "Black", 1), Piece([1,6], 'P', "Black", 1), Piece([1,7], 'P', "Black", 1)],
                            ['x','x','x','x','x','x','x','x'],
                                ['x','x','x','x','x','x','x','x'],
                                    ['x','x','x','x','x','x','x','x'],
                                        ['x','x','x','x','x','x','x','x'],
                                            [Piece([6,0], 'P', "White", 1), Piece([6,1], 'P', "White", 1), Piece([6,2], 'P', "White", 1), Piece([6,3], 'P', "White", 1), Piece([6,4], 'P', "White", 1), Piece([6,5], 'P', "White", 1), Piece([6,6], 'P', "White", 1), Piece([6,7], 'P', "White", 1)],
                                                [Piece([7,0], 'R', "White", 5), Piece([7,1], 'N', "White", 3), Piece([7,2], 'B', "White", 3.5), Piece([7,3], 'Q', "White", 9), Piece([7,4], 'K', "White", 1000), Piece([7,5], 'B', "White", 3.5), Piece([7,6], 'N', "White", 3), Piece([7,7], 'R', "White", 5)]]
    def get_board(self):
        return self._board

    def set_board(self, board):
        self._board = board

    def print_board(self):
        print("   a b c d e f g h   \n")
        for i in range(len(self._board)):
            row = str(8-i) + "  "
            for q in range(len(self._board)):
                if self._board[i][q] != 'x':
                    row += self._board[i][q].get_type()
                else:
                    row += 'x'
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

    def legality_check(self, start_pos, end_pos):
        match self._board[start_pos[0]][start_pos[1]].get_type():
            case 'P':
                if start_pos[1] == end_pos[1]:
                    if self._board[start_pos[0]][start_pos[1]].get_colour() == "White" and self._turn_counter == 0:
                        if start_pos[0] == end_pos[0] + 1 or (start_pos[0] == end_pos[0] + 2 and not self._board[start_pos[0]][start_pos[1]].get_has_moved()):
                            self._board[start_pos[0]][start_pos[1]].set_has_moved(True)
                            return True
                    if self._board[start_pos[0]][start_pos[1]].get_colour() == "Black" and self._turn_counter == 1:
                        if start_pos[0] == end_pos[0] - 1 or (start_pos[0] == end_pos[0] - 2 and not self._board[start_pos[0]][start_pos[1]].get_has_moved()):
                            # If hasn't moved, can move 2
                            self._board[start_pos[0]][start_pos[1]].set_has_moved(True)
                            return True

                print("Invalid Move for piece")
                return False               
            case _:
                print("Invalid Move for piece")
                return False

    def in_check():
        return False

    def increment_turn_counter(self):
        if self._turn_counter == 1:
            self._turn_counter = 0
            return
        self._turn_counter += 1
class Piece:
    def __init__(self, pos, type, colour, value):
        self._pos = pos
        self._piece_type = type
        self._colour = colour
        self._value = value
        self._relative_value = None
        self._has_moved = False

    def get_type(self):
        return self._piece_type

    def get_colour(self):
        return self._colour

    def get_has_moved(self):
        return self._has_moved

    def set_has_moved(self, has_moved):
        self._has_moved = has_moved

def main():
    board = Board()
    game_over = False
    while not game_over:
        board.print_board()
        start_pos = board.translate_move(input("Please enter starting square (in the form xN, where x is a lowercase letter a-h and N is a number 1-8):\n"))
        # Takes the user input and translates xN to a [N][M]
        end_pos = board.translate_move(input("Please enter desired square (in the form xN, where x is a lowercase letter a-h and N is a number 1-8):\n"))
        if board.legality_check(start_pos, end_pos):
            board.move_piece(start_pos, end_pos)
            board.increment_turn_counter()

if __name__ == "__main__":
    main()
