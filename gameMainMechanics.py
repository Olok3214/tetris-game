from operator import truediv
from blocksDef import Iblock, Jblock, Lblock, Oblock, Sblock, Tblock, Zblock
from grid import Grid
import random
import pygame

#Główne mechaniky gry

class GameMechanic:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [Iblock(), Jblock(), Oblock(), Lblock(), Sblock(), Tblock(), Zblock()]
        self.gameOver = False
        self.currentBlock = self.getRandomBlock()
        self.nextBlock = self.getRandomBlock()
        self.score = 0
        self.maxScore =0
        
        self.ClarLineSound = pygame.mixer.Sound("SoundEffects\ClearLine-floraphonic.mp3")
        self.ClarLineSound.set_volume(0.7)
        
        self.GameOverSound = pygame.mixer.Sound("SoundEffects\GameOver-floraphonic.mp3")
        
        self.hardDropSound = pygame.mixer.Sound("SoundEffects\difChange-floraphonic.mp3")
        self.hardDropSound.set_volume(0.2)
        
        pygame.mixer.music.load("SoundEffects\kim-lightyear-leave-the-world-tonight.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.15)
        
        #Zwraca lowowy blok z listy dostępnych bloków
    def getRandomBlock(self):
        # W grze każdy z bloków pojawia się przynajmniej raz podczas iteracji po liście z wszystkimi blokami
        if len(self.blocks) == 0:
            self.blocks = [Iblock(), Jblock(), Oblock(), Lblock(), Sblock(), Tblock(), Zblock()]     
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block
    
    #rysowanie bloków i grid na ekranie
    def draw(self,screen):
        #rysowanie siatki
        self.grid.drawGrid(screen)
        #rysowanie aktualnego bloku
        self.currentBlock.drawBlock(screen,0,0)
        
        #Żeby bloki I i O były na środku nastepnego bloku
        if self.nextBlock.id == 2:
            self.nextBlock.drawBlock(screen,-305,360)
        elif self.nextBlock.id == 3:
            self.nextBlock.drawBlock(screen,-310,340)
        else:
            self.nextBlock.drawBlock(screen,-290,350)
      
      
      
      #Przesunięcie bloku w dół
    def moveDown(self):
        self.currentBlock.move(1,0)
        #Jeżeli blok nie pasuje po wykonaniu ruchu , cofamy ruch i go blokujemy
        if self.blockInside() == False or  self.blockFits() == False:
            self.currentBlock.move(-1,0)
    
                #Blokujemy blok zapisując go na planszy
            self.lockBlock()
      
      #Przesunięcie bloku w lewo
    def moveLeft(self):
        self.currentBlock.move(0,-1)
        #Jeżeli blok nie pasuje po wykonaniu ruchu, cofamy blok 
        if self.blockInside() == False or self.blockFits() == False:
            self.currentBlock.move(0,1)
        
        #Przesunięcie bloku w prawo
    def moveRight(self):
        self.currentBlock.move(0,1)
        if self.blockInside() == False or self.blockFits() == False:
            self.currentBlock.move(0,-1)
        
    
        #Harddrop - przesuwa blok na sam dół
    def hardDrop(self):
        isFalling = True
        
        while isFalling:
            self.currentBlock.move(1,0)
            
            if self.blockInside() == False or  self.blockFits() == False:
                self.currentBlock.move(-1,0)
                isFalling = False
                self.hardDropSound.play()
                self.lockBlock()
            
            #Aktualizuje wartości grid poprzez zablokowanie bloku
    def lockBlock(self):
        tiles = self.currentBlock.getCellPositions()
        for positon in tiles:
            #Zamieniamy wartości grid 0(pusty element) na id bloku
            self.grid.grid[positon.row][positon.column] = self.currentBlock.id
        
        #Zamiana bloków, następny blok jest obecnym, a następny jest od nowa wylowowany
        self.currentBlock = self.nextBlock
        self.nextBlock = self.getRandomBlock()
        rowsCleared = self.grid.clearFullRow()
        #
        if rowsCleared > 0:
            self.ClarLineSound.play()
            self.updateSore(rowsCleared , 0)
        #Jeżeli blok nie pasuje koniec gry
        if self.blockFits() == False:
            self.GameOverSound.play()
            self.gameOver = True
            
            #Hugh score
            if self.score > self.maxScore:
                self.maxScore = self.score
                
        
        # Funnkcja sprawdza czy blok pasuje(wszytkie karatki są puste), zwraca True jeżeli tak
    def blockFits(self):
        tiles = self.currentBlock.getCellPositions()
        for tile in tiles:
            if self.grid.isCellEmpty(tile.row, tile.column) == False:
                return False
        return True
                
            
        
    def blockInside(self):
        #Sprawdza pozycje bloku, jeżeli nie jest na planszy zwraca False
        tiles = self.currentBlock.getCellPositions()
        for tile in tiles:
            if self.grid.isInside(tile.row, tile.column) == False:
                return False
        return True
        
        #Fruncka obrotu bloku
    def rotateBlock(self):
        self.currentBlock.rotate()
        
        #Jeżeli blok po rotacji jest poza planszą lub nie pasuje cofa rotację
        if self.blockInside() == False  or self.blockFits() == False:
            self.currentBlock.undoRotate()
        
        #Reset gry
    def resetGame(self):
        self.grid.resetGrid()
        self.score = 0
        self.blocks = [Iblock(), Jblock(), Oblock(), Lblock(), Sblock(), Tblock(), Zblock()]
        self.currentBlock = self.getRandomBlock()
        self.nextBlock = self.getRandomBlock()
        
        #Aktualizacja wyniku
    def updateSore(self , linesCleared, movedDownPoints):
        if linesCleared == 1:
            self.score += 75
        elif linesCleared ==2:
            self.score += 200
        elif linesCleared == 3:
            self.score += 350
        elif linesCleared >=4:
            self.score += 200 * linesCleared 
        self.score += movedDownPoints
            