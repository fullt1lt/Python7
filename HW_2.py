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
        if self.cheking_for_board_limits(new_place) == True:
            self.place = new_place
        else:
            print(f"You can't put the piece in place {new_place}")
    
    def ceck_move(self)-> None:
        raise NotImplementedError
    
test = ChessPiece()

test._set_place((5,2))
print(test.place)


class Pawn(ChessPiece):

    def __cheking_for_board_limits(self,move):
        return super().cheking_for_board_limits(move)
    
    def __move_condition(self)->tuple:
        if self.color == "White":
            return (self.place[0], self.place[1] + 1)
        else:
            return (self.place[0], self.place[1] - 1)

    def ceck_move(self, move: tuple)-> None:
        if self.__cheking_for_board_limits(move) == True and self.__move_condition() == move:
                print(f"This move {move} is possible")
                self._set_place(move)
        else:
            print(f"This move {move} is impossible")



# white_pawn = Pawn()
# white_pawn.ceck_move((0,1))
# print(white_pawn.place)
# white_pawn.ceck_move((0,3))
# print(white_pawn.place)

black_pawn = Pawn()
black_pawn.set_color()
black_pawn._set_place((5,5))
print(black_pawn.place)
black_pawn.ceck_move((5,4))
black_pawn.ceck_move((5,3))
black_pawn.ceck_move((5,2))
black_pawn.ceck_move((5,1))
black_pawn.ceck_move((5,0))
black_pawn.ceck_move((5,-1))

