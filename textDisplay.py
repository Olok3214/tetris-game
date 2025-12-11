import pygame



class text:
    
    def __init__(self):
        self.fontTitle = pygame.font.Font("Eight-Bit Madness.ttf",70)
        self.font = pygame.font.Font("Eight-Bit Madness.ttf",50)
        self.smallFont = pygame.font.Font("Eight-Bit Madness.ttf",25)
        self.bigfFont = pygame.font.Font("Eight-Bit Madness.ttf",125)
        
        
    def renderTitle(self,txt,color):
        rendered_text =  self.fontTitle.render(txt, True , color)
        return  rendered_text
    
    def renderText(self,txt,color):
        rendered_text = self.font.render(txt, True, color)
        return rendered_text
    
    def renderSmallText(self,txt,color):
        rendered_text = self.smallFont.render(txt, True, color)
        return rendered_text
    
    def renderBigText(self,txt,color):
        rendered_text = self.bigfFont.render(txt, True, color)
        return rendered_text