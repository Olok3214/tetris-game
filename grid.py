import pygame
from blockcolors import Colors

rows = 20
columns = 10
singleCellSize = 30

#Siatka gry 
class Grid:
    
    def __init__(self):
        self.numOfRows = rows
        self.numOfColumns = columns
        self.cellSize = singleCellSize
        #Opis siatki gry - zmieniając jej wartosci zmieniamy kolory
        self.grid = [[ 0 for j in range(self.numOfColumns)]
                     for i in range(self.numOfRows)]
        self.colors = Colors.getCellColor()
        
        
        
        #Funkcja sprawdza czy podana kratka jest w planszy
    def isInside(self,row,column):
        if row >=0 and row < self.numOfRows and column >=0 and column < self.numOfColumns:
            return True
        return False

    
    
    
    #rysowanie siatki, kolory kształtów są zależnie od indeksów kolorów w liście
    # 0 - szary (pusty) 2-7 - kolory
    def drawGrid(self, screen):
        for row in range(self.numOfRows):
            for column in range(self.numOfColumns):
                currentCellValue = self.grid[row][column]
                #Określenie pozycji
                cellRect = pygame.Rect(column * self.cellSize +280, row * self.cellSize +11
                                       , self.cellSize -1 ,self.cellSize -1)
                #Rysowanie komórek
                pygame.draw.rect(screen, self.colors[currentCellValue], cellRect)
                 
                #sprawdza czy komórka jest pusta
    def isCellEmpty(self,row,column):
        if self.grid[row][column] ==0:
            return True
        return False
    
        #sprawdza czy wiersz jest pełny
    def isRowFull(self,row):
        for column in range(self.numOfColumns):
            if self.grid[row][column] ==0:
                return False
        return True

        #Czysci wiersz
    def clearRow(self,row):
        for column in range(self.numOfColumns):
            self.grid[row][column] = 0
            
            #przesunięcie wierszy w dół o wartość downoffset (ile wierszy zostało wyczyszczonych)
    def moveRowDown(self,row, downoffset):
        for column in range(self.numOfColumns):
            self.grid[row + downoffset][column] = self.grid[row][column]
            self.grid[row][column] = 0
            
            #wyczyszczenie wierszy gdy są pełne. Zwraca ich liczbę
    def clearFullRow(self):
        completedRows = 0
        for row in range(self.numOfRows -1 , 0 , -1):
            if self.isRowFull(row):
                self.clearRow(row)
                completedRows +=1
            elif completedRows >0:
                self.moveRowDown(row, completedRows)
        
        return completedRows

        #Reset grida, ustawiamy wszystkie kratki na 0 (pusta kratka)
    def resetGrid(self):
        for row in range(self.numOfRows):
            for column in range(self.numOfColumns):
                self.grid[row][column] = 0