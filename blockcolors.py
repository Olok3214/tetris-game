class Colors:
    #Kolory bloków
    cyan = (0,255,255)
    yellow = (255,255,0)
    purple = (128,0,128)
    green = (0,255,0)
    red = (255,0,0)
    blue = (0,0,255)
    orange = (255,127,0)
    
    #kolor pustej komurki
    grey = (26,31,40) 
        
    @classmethod
    def getCellColor(cls):
        return [cls.grey,cls.cyan,cls.yellow,cls.purple,cls.green,cls.red,cls.blue,cls.orange]

        