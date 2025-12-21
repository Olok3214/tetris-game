import pygame

txtColor = (255,255,255)

#Klasa odpowiada za funkcjie związane z wypisywaniem tekstu
class text:
    
    def __init__(self):
        self.fontTitle = pygame.font.Font("Eight-Bit Madness.ttf",70)
        self.font = pygame.font.Font("Eight-Bit Madness.ttf",50)
        self.smallFont = pygame.font.Font("Eight-Bit Madness.ttf",25)
        self.bigfFont = pygame.font.Font("Eight-Bit Madness.ttf",125)
        
        #renderowanie tytułu
    def renderTitle(self,txt,color = txtColor):
        rendered_text =  self.fontTitle.render(txt, True , color)
        return  rendered_text
        
        #renderowanie zwykłego tekstu
    def renderText(self,txt,color = txtColor):
        rendered_text = self.font.render(txt, True, color)
        return rendered_text

        #renderowanie małego tekstu
    def renderSmallText(self,txt,color = txtColor):
        rendered_text = self.smallFont.render(txt, True, color)
        return rendered_text

        #renderowanie dużego tekstu
    def renderBigText(self,txt,color = txtColor):
        rendered_text = self.bigfFont.render(txt, True, color)
        return rendered_text