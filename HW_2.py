class ChessPiece:
    color: str = "White"
    place: tuple = (0,0)

    def set_color(self)-> None:
        if self.color =="White":
            self.color = "Black"
        else:
            self.color = "White"

    def cheking_for_board_limits(self,new_place: tuple)-> bool:
        return len([number for number in new_place if 0 <= number <= 7]) == 2

    def _set_place(self, new_place: tuple)-> None:
        if self.cheking_for_board_limits(new_place):
            self.place = new_place
        else:
            print(f"You can't put the piece in place {new_place}")
    
    def ceck_move(self)-> None:
        raise NotImplementedError
    
class Pawn(ChessPiece):
    name: str = "Pawn"
    def __cheking_for_board_limits(self,move):
        return super().cheking_for_board_limits(move)
    
    def __move_condition(self)->list:
        all_moves = []
        if self.color == "White":
            all_moves.append((self.place[0], self.place[1] + 1))
            return all_moves
        else:
            all_moves.append((self.place[0], self.place[1] - 1))
            return all_moves

    def ceck_move(self, move: tuple)-> bool:
        return self.__cheking_for_board_limits(move) and move in self.__move_condition()

class Officer(ChessPiece):
    name: str = "Officer"
    def __cheking_for_board_limits(self,move) -> bool:
        return super().cheking_for_board_limits(move)
    
    def __move_condition(self)->list:
        x, y = self.place
        all_moves = []
        # diagonal moves
        for i in range(1, 8):
            if x + i <= 7 and y + i <= 7:
                all_moves.append((x + i, y + i))  # right down
            if x - i >= 0 and y - i >= 0:
                all_moves.append((x - i, y - i))  # left up
            if x + i <= 7 and y - i >= 0:
                all_moves.append((x + i, y - i))  # right up
            if x - i >= 0 and y + i <= 7:
                all_moves.append((x - i, y + i))  # left down
        return all_moves
        
    def ceck_move(self, move: tuple)-> bool:
        return self.__cheking_for_board_limits(move) and move in self.__move_condition()

class Queen(ChessPiece):
    name: str = "Queen"
    def __cheking_for_board_limits(self,move) -> bool:
        return super().cheking_for_board_limits(move)
    
    def __move_condition(self)->list:
        x, y = self.place
        all_moves = []
        # diagonal moves
        for i in range(1, 8):
            if x + i <= 7 and y + i <= 7:
                all_moves.append((x + i, y + i))  # right down
            if x - i >= 0 and y - i >= 0:
                all_moves.append((x - i, y - i))  # left up
            if x + i <= 7 and y - i >= 0:
                all_moves.append((x + i, y - i))  # right up
            if x - i >= 0 and y + i <= 7:
                all_moves.append((x - i, y + i))  # left down
        # moves up and down
        for i in range(1, 8):
            if y + i <= 7:
                all_moves.append((x, y + i))  # up
            if y - i >= 0:
                all_moves.append((x, y - i))  # down
        # moves left and right
        for i in range(1, 8):
            if x + i <= 7:
                all_moves.append((x + i, y))  # right
            if x - i >= 0:
                all_moves.append((x - i, y))  # left
        return all_moves
        
    def ceck_move(self, move: tuple)-> bool:
        return self.__cheking_for_board_limits(move) and move in self.__move_condition()

class Rook(ChessPiece):
    name: str = "Rook"
    def __cheking_for_board_limits(self,move) -> bool:
        return super().cheking_for_board_limits(move)
    
    def __move_condition(self)->list:
        x, y = self.place
        all_moves = []
        # moves up and down
        for i in range(1, 8):
            if y + i <= 7:
                all_moves.append((x, y + i))  # up
            if y - i >= 0:
                all_moves.append((x, y - i))  # down
        # moves left and right
        for i in range(1, 8):
            if x + i <= 7:
                all_moves.append((x + i, y))  # right
            if x - i >= 0:
                all_moves.append((x - i, y))  # left
        return all_moves
        
    def ceck_move(self, move: tuple)-> bool:
        return self.__cheking_for_board_limits(move) and move in self.__move_condition()


class King(ChessPiece):
    name: str = "King"
    def __cheking_for_board_limits(self,move) -> bool:
        return super().cheking_for_board_limits(move)
    
    def __move_condition(self)->list:
        x, y = self.place
        all_moves = []
        # diagonal moves
        for i in range(1, 2):
            if x + i <= 7 and y + i <= 7:
                all_moves.append((x + i, y + i))  # right down
            if x - i >= 0 and y - i >= 0:
                all_moves.append((x - i, y - i))  # left up
            if x + i <= 7 and y - i >= 0:
                all_moves.append((x + i, y - i))  # right up
            if x - i >= 0 and y + i <= 7:
                all_moves.append((x - i, y + i))  # left down
        # moves up and down
        for i in range(1, 2):
            if y + i <= 7:
                all_moves.append((x, y + i))  # up
            if y - i >= 0:
                all_moves.append((x, y - i))  # down
        # moves left and right
        for i in range(1, 2):
            if x + i <= 7:
                all_moves.append((x + i, y))  # right
            if x - i >= 0:
                all_moves.append((x - i, y))  # left
        return all_moves
        
    def ceck_move(self, move: tuple)-> bool:
        return self.__cheking_for_board_limits(move) and move in self.__move_condition()

class Horse(ChessPiece):
    name: str = "Horse"
    def __cheking_for_board_limits(self,move) -> bool:
        return super().cheking_for_board_limits(move)
    
    def __move_condition(self)->list:
        x, y = self.place
        all_moves = []
        # moves horse 
        if x + 2 <= 7 and y + 1 <= 7:
            all_moves.append((x + 2, y + 1))  # right up
        if x - 2 >= 0 and y + 1 <= 7:
            all_moves.append((x - 2, y + 1))  # left up
        if x + 2 <= 7 and y - 1 >= 0:
            all_moves.append((x + 2, y - 1))  # right down
        if x - 2 >= 0 and y - 1 >= 0:
            all_moves.append((x - 2, y - 1))  # left down
        if x + 1 <= 7 and y + 2 <= 7:
            all_moves.append((x + 1, y + 2))  # up right
        if x - 1 >= 0 and y + 2 <= 7:
            all_moves.append((x - 1, y + 2))  # up left
        if x + 1 <= 7 and y - 2 >= 0:
            all_moves.append((x + 1, y - 2))  # down right
        if x - 1 >= 0 and y - 2 >= 0:
            all_moves.append((x - 1, y - 2))  # down left
        return all_moves
        
    def ceck_move(self, move: tuple)-> bool:
        return self.__cheking_for_board_limits(move) and move in self.__move_condition()

chess_piece = ChessPiece()
white_pawn = Pawn()
black_pawn = Pawn()
black_pawn.set_color()
officer = Officer()
queen = Queen()
rook = Rook()
king = King()
horse = Horse()
сhess_pieces = [white_pawn,black_pawn,officer,queen,rook,king,horse]
move = (3,3)

def sorting_shapes(сhess_pieces: list, move: tuple ) -> list:
    return [f'{piece.name}' for piece in сhess_pieces if piece.ceck_move(move)]

print(f"Move from place {chess_piece.place} to place {move} can be done: {sorting_shapes(сhess_pieces, move)}")