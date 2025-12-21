from grid import singleCellSize
from blockcolors import Colors
import pygame
from positionInGrid import Positon

#Rysowanie poszczególnych bloków
class Block:
    def __init__(self, id):
        self.id = id
        #komurki ustawiamy w blockDef
        self.occupiedCells = {}
        self.cellSize = singleCellSize
        #Każdy ksztalt ma 4 różne możliwe obroty
        #0 - podstawowy , każdy blok pojawia się nie obrucony
        self.rowOffset = 0
        self.columnOffset =0
        self.rotationState = 0
        self.colors = Colors.getCellColor()

        
        
        
        #Przesunięcie bloku na planszy
    def move(self,rows,columns):
        self.rowOffset += rows
        self.columnOffset += columns
        
        #Zwraca pozycje ksztaltu z przesunięciem
    def getCellPositions(self):
        tiles = self.occupiedCells[self.rotationState]
        movedTiles = []
        for position in tiles:
            position = Positon(position.row + self.rowOffset , position.column + self.columnOffset)
            movedTiles.append(position)
        return movedTiles
        
        #Obrót bloku
    def rotate(self):
        self.rotationState +=1
        if self.rotationState == 4:
            self.rotationState = 0
            
        #Cofnięcie obrotu
    def undoRotate(self):
        self.rotationState -=1
        #Jeżeli obrót jest mniejszy niż 0 wraca do ostatniego obrotu(3)
        if self.rotationState == -1:
            self.rotationState = 3
        
    
            
        #Rysowanie bloku na ekranie
    def drawBlock(self, screen, offsetx, offsety):
        blockTiles = self.getCellPositions()
        for tile in blockTiles:
            tileRect = pygame.Rect(offsetx + tile.column * self.cellSize +280, offsety+ tile.row * self.cellSize +11,
                                   self.cellSize -1, self.cellSize -1)
                                        #wybieramy kolor osobny dla każdego kształtu
            pygame.draw.rect(screen , self.colors[self.id], tileRect)
            
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    