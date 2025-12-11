
#Zmienia poziom trudności gry
# easy 250 / normal 200 / hard 150 / ekstreme 50 
class Difficulty:
    def __init__(self):
        #Stndardowa trudność 
        self.blockFallTimer = 200

            
    def difficultyUp(self):
        if self.blockFallTimer == 150:
            self.blockFallTimer = 200
        elif self.blockFallTimer == 200:
            self.blockFallTimer = 250
        elif self.blockFallTimer == 250:
            self.blockFallTimer = 50
        elif self.blockFallTimer == 50:
            self.blockFallTimer = 150
            
    def difficultyDown(self):
        if self.blockFallTimer == 50:
            self.blockFallTimer = 250
        if self.blockFallTimer == 150:
            self.blockFallTimer = 50
        elif self.blockFallTimer == 200:
            self.blockFallTimer = 150
        elif self.blockFallTimer == 250:
            self.blockFallTimer = 200


