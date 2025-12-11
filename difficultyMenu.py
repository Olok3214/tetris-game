import pygame

#Zmienia poziom trudności gry
# easy 250 / normal 200 / hard 150 / ekstreme 50 
class Difficulty:
    def __init__(self):
        #Stndardowa trudność 
        self.blockFallTimer = 200
        self.difficultyChangeSound = pygame.mixer.Sound("SoundEffects\difChange-floraphonic.mp3")
        self.difficultyChangeSound.set_volume(0.1)
        self.easy = 250
        self.normal = 200
        self.hard = 150
        self.extreme = 50 
            
            
    def difficultyDown(self):
        self.difficultyChangeSound.play()
        if self.blockFallTimer ==  self.hard:
            self.blockFallTimer = self.normal
        elif self.blockFallTimer == self.normal:
            self.blockFallTimer = self.easy
        elif self.blockFallTimer == self.easy:
            self.blockFallTimer = self.extreme
        elif self.blockFallTimer == self.extreme:
            self.blockFallTimer =  self.hard
            
    def difficultyUp(self):
        self.difficultyChangeSound.play()
        if self.blockFallTimer ==  self.extreme:
            self.blockFallTimer = self.easy
        elif self.blockFallTimer == self.hard:
            self.blockFallTimer =  self.extreme
        elif self.blockFallTimer == self.normal:
            self.blockFallTimer = self.hard
        elif self.blockFallTimer == self.easy:
            self.blockFallTimer = self.normal


