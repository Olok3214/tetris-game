import pygame

#Zmienia poziom trudności gry
# easy 250 / normal 200 / hard 150 / ekstreme 50 
class Difficulty:
    def __init__(self):
        #Stndardowa trudność 
        self.blockFallTimer = 200
        self.difficultyChangeSound = pygame.mixer.Sound("SoundEffects\difChange-floraphonic.mp3")
        self.difficultyChangeSound.set_volume(0.1)
            
    def difficultyUp(self):
        self.difficultyChangeSound.play()
        if self.blockFallTimer == 150:
            self.blockFallTimer = 200
        elif self.blockFallTimer == 200:
            self.blockFallTimer = 250
        elif self.blockFallTimer == 250:
            self.blockFallTimer = 50
        elif self.blockFallTimer == 50:
            self.blockFallTimer = 150
            
    def difficultyDown(self):
        self.difficultyChangeSound.play()
        if self.blockFallTimer == 50:
            self.blockFallTimer = 250
        elif self.blockFallTimer == 150:
            self.blockFallTimer = 50
        elif self.blockFallTimer == 200:
            self.blockFallTimer = 150
        elif self.blockFallTimer == 250:
            self.blockFallTimer = 200


