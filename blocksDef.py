from blocks import Block
from positionInGrid import Positon

#Definicje wszystkich blocków
#Każdy z bloków dziedziczy funcje klasy Block

# blok L id = 1
class Lblock(Block):
    def __init__(self):
        super().__init__(id = 1)
        # klucz dziennika - obecny obrót
        #Position(row, coulumn)
        self.occupiedCells = {
            0: [
                Positon(0,2), Positon(1,0), Positon(1,1), Positon(1,2)
            ],
            1:[
                Positon(0,1) , Positon(1,1), Positon(2,1), Positon(2,2)
            ],
            2:[
                Positon(1,0), Positon(1,1), Positon(1,2), Positon(2,0)
            ],
            3:[
                Positon(0,0), Positon(0,1), Positon(1,1), Positon(2,1)
            ]
        }
        #Blok pojawia się na środku ekranu
        self.move(0,3)
  
# blok I id = 2
class Iblock(Block):
    def __init__(self):
        super().__init__(id =2)
        #Position(row, coulumn)
        self.occupiedCells = {
            0: [
                Positon(1,0), Positon(1,1), Positon(1,2), Positon(1,3)
            ],
            1:[
                Positon(0,2) , Positon(1,2), Positon(2,2), Positon(3,2)
            ],
            2:[
                Positon(2,0), Positon(2,1), Positon(2,2), Positon(2,3)
            ],
            3:[
                Positon(0,1), Positon(1,1), Positon(2,1), Positon(3,1)
            ]
        }
        self.move(-1,3)
  
# blok O id = 3
class Oblock(Block):
    def __init__(self):
        super().__init__(id = 3)
        #Position(row, coulumn)
        self.occupiedCells = {
            0: [
                Positon(0,0), Positon(0,1), Positon(1,0), Positon(1,1)
            ],
            1:[
                Positon(0,0) , Positon(0,1), Positon(1,0), Positon(1,1)
            ],
            2:[
                Positon(0,0), Positon(0,1), Positon(1,0), Positon(1,1)
            ],
            3:[
                Positon(0,0), Positon(0,1), Positon(1,0), Positon(1,1)
            ]
        }
        self.move(0,4)
        
# blok J id = 4
class Jblock(Block):
    def __init__(self):
        super().__init__(id = 4)
        #Position(row, coulumn)
        self.occupiedCells = {
            0: [
                Positon(0,0), Positon(1,0), Positon(1,1), Positon(1,2)
            ],
            1:[
                Positon(0,1) , Positon(0,2), Positon(1,1), Positon(2,1)
            ],
            2:[
                Positon(1,0), Positon(1,1), Positon(1,2), Positon(2,2)
            ],
            3:[
                Positon(0,1), Positon(1,1), Positon(2,0), Positon(2,1)
            ]
        }
        self.move(0,3)
        
        
# blok T id = 5
class Tblock(Block):
    def __init__(self):
        super().__init__(id = 5)
        #Position(row, coulumn)
        self.occupiedCells = {
            0: [
                Positon(0,1), Positon(1,0), Positon(1,1), Positon(1,2)
            ],
            1:[
                Positon(0,1) , Positon(1,1), Positon(1,2), Positon(2,1)
            ],
            2:[
                Positon(1,0), Positon(1,1), Positon(1,2), Positon(2,1)
            ],
            3:[
                Positon(0,1), Positon(1,0), Positon(1,1), Positon(2,1)
            ]
        }
        self.move(0,3)
  
        
# blok S id = 6
class Sblock(Block):
    def __init__(self):
        super().__init__(id = 6)
        #Position(row, coulumn)
        self.occupiedCells = {
            0: [
                Positon(0,1), Positon(0,2), Positon(1,0), Positon(1,1)
            ],
            1:[
                Positon(0,1) , Positon(1,1), Positon(1,2), Positon(2,2)
            ],
            2:[
                Positon(1,1), Positon(1,2), Positon(2,0), Positon(2,1)
            ],
            3:[
                Positon(0,0), Positon(1,0), Positon(1,1), Positon(2,1)
            ]
        }
        self.move(0,3)
        
# blok Z id = 7
class Zblock(Block):
    def __init__(self):
        super().__init__(id = 7)
        #Position(row, coulumn)
        self.occupiedCells = {
            0: [
                Positon(0,0), Positon(0,1), Positon(1,1), Positon(1,2)
            ],
            1:[
                Positon(0,2) , Positon(1,1), Positon(1,2), Positon(2,1)
            ],
            2:[
                Positon(1,0), Positon(1,1), Positon(2,1), Positon(2,2)
            ],
            3:[
                Positon(0,1), Positon(1,0), Positon(1,1), Positon(2,0)
            ]
        }     
        self.move(0,3) 