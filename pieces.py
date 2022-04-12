from abc import ABC, abstractmethod

class GamePiece(ABC):

    def __init__(self, team:str, piece:str, position:list):
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


    @abstractmethod
    def is_valid_position(self, target:list) -> bool:
        """
        Checks if the target position is valid
        """

    @abstractmethod
    def is_legal_move(self, target) -> bool:
        return


    def move(self, target:list) -> None:
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
        return self.piece[0] + self.team[0]
#################################################################

class Rook(GamePiece):
    '''
    Class for the Rook piece
    '''
    def is_valid_position(self, target:list) -> bool:
        """
        Checks if the target position is valid
        """
        return True

    def is_legal_move(self, target) -> bool:
        return True
###############################################################

class Bishop(GamePiece):
    '''
    Class for the Bishop piece
    '''
    def is_valid_position(self, target:list) -> bool:
        """
        Checks if the target position is valid
        """
        return True

    def is_legal_move(self, target) -> bool:
        return True
##############################################################

class Pawn(GamePiece):
    def __init__(self, team: str, piece: str, position: list):
        super().__init__(team, piece, position)
        self.has_moved = False

    def is_valid_position(self, target:list) -> bool:
        """
        Checks if the target position is valid
        """
        # if not self.has_moved:
        #     if self.team == 'black':

        return True

    def is_legal_move(self, target) -> bool:
        return True
##############################################################

class Queen(GamePiece):
    '''
    Class for the Queen piece
    '''
    def is_valid_position(self, target:list) -> bool:
        """
        Checks if the target position is valid
        """
        return True

    def is_legal_move(self, target) -> bool:
        return True
##############################################################

class Knight(GamePiece):
    '''
    Class for the Knight piece
    '''
    def is_valid_position(self, target:list) -> bool:
        """
        Checks if the target position is valid
        """
        return True

    def is_legal_move(self, target) -> bool:
        return True
##############################################################

class King(GamePiece):
    '''
    Class for the King piece
    '''
    def is_valid_position(self, target:list) -> bool:
        """
        Checks if the target position is valid
        """
        return True

    def is_legal_move(self, target) -> bool:
        return True
