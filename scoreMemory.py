from pathlib import Path

#Odczytywanie wyników z pamięci
# easy 250 / normal 200 / hard 150 / ekstreme 50 
class scoreMemory:
    maxEasyScore = 0
    maxNormalScore = 0
    maxHardSode = 0
    maxExtremeScore =0
    
    curentGameDif = 200
    
    #Ustawienie obecnego poziomu trudnosci
    @classmethod
    def setCurentGameDiff(cls, diff):
        cls.curentGameDif = diff

        
    #aktualizacja max wyniku w programie 
    @classmethod
    def updateHighScore(cls, newDiff):
        match cls.curentGameDif:
            case 250:
                cls.maxEasyScore = newDiff
            case 200:
                cls.maxNormalScore = newDiff
            case 150:
                cls.maxHardSode = newDiff
            case 50:
                cls.maxEasyScore = newDiff
        cls.updateLocalMemory()     
            
                
                
    #Zwraca obecny maksymalny posiom zależnie od obecnego poziomu trudnosci
    @classmethod
    def getCurrentMaxScore(cls):
        match cls.curentGameDif:
            case 250:
                return cls.maxEasyScore
            case 200:
                return cls.maxNormalScore
            case 150:
                return cls.maxHardSode
            case 50:
                return cls.maxEasyScore
            
    #odczytanie wyników z pliku (na początku gry)
    @classmethod
    def loadMaxScoreFromLocalFile(cls):
        #jeżeli plik nie istnieje, tworzy go
        if (Path('maxScore.txt').exists() == False):
            cls.createLocalMemory()
        
        with open('maxScore.txt' , 'r') as file:
            memory = file.read()
            memory = memory.split('\n')
            cls.maxEasyScore = int(memory[0])
            cls.maxNormalScore = int(memory[1])
            cls.maxHardSode = int(memory[2])
            cls.maxExtremeScore = int(memory[3])
            print(cls.maxEasyScore)
    
    
    def createLocalMemory():
        with open('maxScore.txt', "w") as file:
            file.write('0\n0\n0\n0')
            
    @classmethod
    def updateLocalMemory(cls):
        with open('maxScore.txt', "w") as file:
            file.write(f'{int(cls.maxEasyScore)}\n{int(cls.maxNormalScore)}\n{int(cls.maxHardSode)}\n{int(cls.maxExtremeScore)}')