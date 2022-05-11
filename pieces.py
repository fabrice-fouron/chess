from abc import ABC, abstractmethod


def let_to_num(rowLet):
    '''Author: Kylash'''
    rowNum = 0
    if rowLet.upper() == "A":
        rowNum = 8
    elif rowLet.upper() == "B":
        rowNum = 7
    elif rowLet.upper() == "C":
        rowNum = 6
    elif rowLet.upper() == "D":
        rowNum = 5
    elif rowLet.upper() == "E":
        rowNum = 4
    elif rowLet.upper() == "F":
        rowNum = 3
    elif rowLet.upper() == "G":
        rowNum = 2
    elif rowLet.upper() == "H":
        rowNum = 1

    return rowNum - 1


def num_to_let(rowNum):
    if rowNum == 'A':
        return 7
    elif rowNum == 'B':
        return 6
    elif rowNum == 'C':
        return 5
    elif rowNum == 'D':
        return 4
    elif rowNum == 'E':
        return 3
    elif rowNum == 'F':
        return 2
    elif rowNum == 'G':
        return 1
    elif rowNum == 'H':
        return 0
    return "Not valid"

class GamePiece(ABC):
    '''Author: Fabrice'''

    def __init__(self, team: str, piece: str, position: list):
        """
        @:param team is whether the game piece is white or black team
        @:param piece The name of the game piece
        @:param position The starting coordinates of the game piece
        """
        self.team = team
        self.piece = piece
        self.position = position
        self.init_position = position
        self.alive = True
        self.valid_moves = []

    @abstractmethod
    def is_valid_position(self, target: list) -> bool:
        """
        Checks if the target position is valid
        """

    def move(self, target: list) -> None:
        """
        @:param target the desired new position of the game piece
        The Game Piece moves to the target position
        Set the position to the new target position
        """
        if self.is_valid_position(target):
            self.position = target
        else:
            raise Exception("Game Piece cannot move there")

    def get_position(self) -> list:
        """
        Returns the position of the game piece
        """
        return self.position

    def change_status(self):
        '''Change the status of the piece to alive or eaten(not alive)'''
        self.alive = not self.alive

    def __str__(self) -> str:
        return self.piece[0:3] + self.team[0]
#################################################################


class Rook(GamePiece):
    '''
    Class for the Rook piece
    '''

    def __init__(self, team: str, piece: str, position: list):
        super().__init__(team, piece, position)
        self.valid_moves = []

    def is_valid_position(self, target):
        if target[0] == self.position[0]:
            return True
        elif target[1] == self.position[1]:
            return True
        else:
            return False
###############################################################


class Bishop(GamePiece):
    '''Author: Henry'''

    def is_valid_position(self, target: list) -> bool:
        """
        Checks if the target position is valid
        
        """
        x = self.position[0]
        y = self.position[1]
        possible_path = []

        tempX = x + 1
        tempY = y - 1

        # northeast
        while tempX < 7 and tempY > 0:
            possible_path.append([tempX, tempY])
            tempX += 1
            tempY -= 1

        tempX = x + 1
        tempY = y - 1

        # northwest
        while tempX < 7 and tempY > 0:
            possible_path.append([tempX, tempY])
            tempX -= 1
            tempY -= 1

        tempX = x + 1
        tempY = y - 1

        # southeast
        while tempX < 7 and tempY > 0:
            possible_path.append([tempX, tempY])
            tempX += 1
            tempY += 1

        tempX = x - 1
        tempY = y + 1

        # southwest
        while tempX < 7 and tempY > 0:
            possible_path.append([tempX, tempY])
            tempX -= 1
            tempY += 1

        if target in possible_path:
            return True
        return False
##############################################################


class Pawn(GamePiece): # Have to work for both sides (black and white) 
    '''Author: Sean'''
    def __init__(self, team: str, piece: str, position: list):
        super().__init__(team, piece, position)
        self.move = 0

    def is_valid_position(self, target: list) -> bool:
        
        # checks      if positon is valid when moving 2 spaces
        if target[0] == let_to_num(self.position[0]) + 2 and target[1] == self.position[1] and self.move == 1:
            return False
        # this       checks if the move is valif for any normal pawn move
        elif target[0] == let_to_num(self.position[0]) + 1 and target[1] == self.position[1]:
            return True
        elif target[0] == let_to_num(self.position[0]) + 1 and target[1] == self.position[1] + 1: 
            return True
        else:
            return False
        self.move = 1
##############################################################


class Queen(GamePiece):
    '''
    Class for the Queen piece
    '''

    def is_valid_position(self, target):
        if target[0] == self.position[0]:
            return True
        elif target[1] == self.position[1]:
            return True
        else:
            x = self.position[0]
            y = self.position[1]
            possible_path = []

            tempX = x + 1
            tempY = y - 1

            # northeast
            while tempX < 7 and tempY > 0:
                possible_path.append([tempX, tempY])
                tempX += 1
                tempY -= 1

            tempX = x + 1
            tempY = y - 1

            # northwest
            while tempX < 7 and tempY > 0:
                possible_path.append([tempX, tempY])
                tempX -= 1
                tempY -= 1

            tempX = x + 1
            tempY = y - 1

            # southeast
            while tempX < 7 and tempY > 0:
                possible_path.append([tempX, tempY])
                tempX += 1
                tempY += 1

            tempX = x - 1
            tempY = y + 1

            # southwest
            while tempX < 7 and tempY > 0:
                possible_path.append([tempX, tempY])
                tempX -= 1
                tempY += 1

            if target in possible_path:
                return True
            return False

##############################################################


class Knight(GamePiece):
    '''
    Class for the Knight piece
    '''

    def is_valid_position(self, target: list) -> bool:
        """
        Checks if the target position is valid
        """
        try:
            if target[0] == self.position[0] - 2 and target[1] == self.position[1] + 1:
                return True
            elif target[0] == self.position[0] - 2 and target[1] == self.position[1] - 1:
                return True
            elif target[0] == self.position[0] + 2 and target[1] == self.position[1] + 1:
                return True
            elif target[0] == self.position[0] + 2 and target[1] == self.position[1] - 1:
                return True
            elif target[0] == self.position[0] + 1 and target[1] == self.position[1] + 2:
                return True
            elif target[0] == self.position[0] - 1 and target[1] == self.position[1] + 2:
                return True
            elif target[0] == self.position[0] + 1 and target[1] == self.position[1] - 2:
                return True
            elif target[0] == self.position[0] - 1 and target[1] == self.position[1] - 2:
                return True
            else:
                return False
        except Exception:
            return False
##############################################################


class King(GamePiece):
    '''
    Author: Marty
    '''

    def __init__(self, team: str, piece: str, position: list):
        super().__init__(team, piece, position)
        self.valid_moves = []
    

    def is_valid_position(self, target: list):

        try:

            if target[0] == self.position[0] + 1 and target[1] == self.position[1] + 1:
                return True
            elif target[0] == self.position[0] + 1 and target[0] == self.position[0]:
                return True
            elif target[0] == self.position[0] + 1 and target[0] == self.position[0] - 1:
                return True
            elif target[0] == self.position[0] and target[0] == self.position[0] - 1:
                return True
            elif target[0] == self.position[0] - 1 and target[0] == self.position[0] - 1:
                return True
            elif target[0] == self.position[0] - 1 and target[0] == self.position[0]:
                return True
            elif target[0] == self.position[0] - 1 and target[0] == self.position[0] + 1:
                return True
            elif target[0] == self.position[0] and target[0] == self.position[0] + 1:
                return True
            else:
                return False
        except IndexError:
            return False
