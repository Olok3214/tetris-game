from blocksDef import Iblock, Jblock, Lblock, Oblock, Sblock, Tblock, Zblock
from grid import Grid
import random
import pygame

#Game mechanics,

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
        
        
        pygame.mixer.music.load("SoundEffects\kim-lightyear-leave-the-world-tonight.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.15)
        
    def getRandomBlock(self):
        # W grze każdy z bloków pojawia się przynajmniej raz podczas iteracji po wszytkich blokach
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
      
      
      
      
    def moveDown(self):
        self.currentBlock.move(1,0)
        if self.blockInside() == False or  self.blockFits() == False:
            self.currentBlock.move(-1,0)
    
                #Jeżeli blok jest poza dolną krawędziła pętli lub NIE PASUJE
                # zablokowujemy go
            self.lockBlock()
      
      #Przesunięcie bloku 
    def moveLeft(self):
        self.currentBlock.move(0,-1)
        if self.blockInside() == False or self.blockFits() == False:
            self.currentBlock.move(0,1)
        
    def moveRight(self):
        self.currentBlock.move(0,1)
        if self.blockInside() == False or self.blockFits() == False:
            self.currentBlock.move(0,-1)
        
    
            
            
            
            #Aktualizuje wartości grid 
    def lockBlock(self):
        tiles = self.currentBlock.getCellPositions()
        for positon in tiles:
            #Zamieniamy 0 na id bloku
            self.grid.grid[positon.row][positon.column] = self.currentBlock.id
        
        #Zamiana bloków, jeżeli zablokuje się obecny blok jest nastepnym, a następny jest od nowa wylowowany
        self.currentBlock = self.nextBlock
        self.nextBlock = self.getRandomBlock()
        rowsCleared = self.grid.clearFullRow()
        
        if rowsCleared > 0:
            self.ClarLineSound.play()
            self.updateSore(rowsCleared , 0)
        
        if self.blockFits() == False:
            self.GameOverSound.play()
            self.gameOver = True
            
            
            if self.score > self.maxScore:
                self.maxScore = self.score
                
        
        # Sprawdza czy blok pasuje 
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
        
        
    def updateSore(self , linesCleared, movedDownPoints):
        if linesCleared == 1:
            self.score += 50
        elif linesCleared ==2:
            self.score += 150
        elif linesCleared == 3:
            self.score += 250
        elif linesCleared >=4:
            self.score += 100 * linesCleared 
        self.score += movedDownPoints
            