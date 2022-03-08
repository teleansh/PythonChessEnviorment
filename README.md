# PythonChessEnviorment
Python Module to work on Chess related projects.

**display()** : Prints current view of the chessboard (white side view)

![display](https://user-images.githubusercontent.com/34571056/157228111-53136e41-d8ad-4a0b-9e94-fcfed2a6cf8b.png)

**newBoard()** : Resets the board to initial position

**move(from,to)** : Moves a piece from one square to another. From and to arguments takes Algebraic Notations in string format. Move need not be a valid move to use this function.

![move](https://user-images.githubusercontent.com/34571056/157228761-6f9bd2d8-d71d-49ba-b268-9641f5e1ee59.png)

**moves(position)** : Returns all valid moves that can be played by a piece in specified square position , it takes one argument , which is the Algebraic Notation address of that piece.

![moves](https://user-images.githubusercontent.com/34571056/157230451-02295695-165d-45cb-9528-ad6c8bc3af18.png)

**rookMoves(pos), pawnMoves(pos), queenMoves(pos), kingMoves(pos), knightMoves(pos), bishopMoves(pos)** also does the same thing but for a particular class of pieces only.

**rookValid(fr,to), pawnValid(fr,to), queenValid(fr,to), kingValid(fr,to), knightValid(fr,to), bishopValid(fr,to)** returns a boolean value depending upon if a particular move is valid or not. This can also be done by comparing the input moves to moves() function list. However these functions donot focus on storing or calculating all the possible moves therefore are faster.

![image](https://user-images.githubusercontent.com/34571056/157231581-78c28a40-8eac-416b-8385-3ea3537f79ce.png)

**isCheck(position_of_king)** : Returns True if the king mentioned in argument is in check else False.

Note: This project is under-development and contains many bugs. Contribution and reviews are appriciated.
