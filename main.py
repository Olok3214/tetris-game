from platform import python_branch
import sys
import pygame
from game import GameMechanic
from textDisplay import text

pygame.init()

backgroundColor = (48 , 25,52)
txtColor = (255,255,255)
boxColor = (54,15,90)

#szybkośc spadania bloków
blockFallTimer = 200

#Wielkość okna gry
screen = pygame.display.set_mode((600,700))

text = text()
game = GameMechanic()

title_txt = text.renderTitle("TETRIS", txtColor)
score_txt = text.renderText("SCORE:", txtColor)
next_txt = text.renderText("NEXT:", txtColor)
gameOver_txt = text.renderText("GAME OVER", txtColor)
maxScore_txt= text.renderSmallText("MAX SCORE:", txtColor)
SoundtrackCredit = text.renderSmallText("Soundtrack: Kim Lightyear", txtColor)
AudioEffectsCredit = text.renderSmallText("Sound Effects: floraphonic", txtColor)

scoreBackground = pygame.Rect(20,120,200,80)
nextBackground = pygame.Rect(20,290,200,200)


pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()
isRunning = True




timer_event = pygame.USEREVENT 
pygame.time.set_timer(timer_event , blockFallTimer)

#Głowna pętla gry
while isRunning:
    for event in pygame.event.get():
        #Zamknięcie gry
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
        if event.type == pygame.KEYDOWN:
            if game.gameOver == True:
                game.gameOver = False
                game.resetGame()
                
            if event.key == pygame.K_LEFT and game.gameOver == False:
                game.moveLeft()
            if event.key == pygame.K_RIGHT and game.gameOver == False:
                game.moveRight()
            if event.key == pygame.K_DOWN and game.gameOver == False:
                game.moveDown()
                game.updateSore(0,3)
            if event.key == pygame.K_UP and game.gameOver == False:
                game.rotateBlock()
        
        if event.type == timer_event and game.gameOver == False:
            game.moveDown()
     
    #Game score
    scoreValue = text.renderText(str(game.score), txtColor)
    #max score
    maxScoreValue = text.renderText(str(game.maxScore), txtColor)
    
    
    screen.fill(backgroundColor)
    screen.blit(title_txt , (20,20,50,50))
    screen.blit(score_txt , (20,80,50,50))
    screen.blit(SoundtrackCredit,(20,670,50,50))
    screen.blit(AudioEffectsCredit, (20,645,50,50))
    screen.blit(maxScore_txt,(20,570,50,50))
    pygame.draw.rect(screen, boxColor, scoreBackground, 0 ,10)
    
    screen.blit(maxScoreValue,(20,595,50,50))
    screen.blit(scoreValue, scoreValue.get_rect(centerx = scoreBackground.centerx,
                                                centery = scoreBackground.centery))
    screen.blit(next_txt , (20,240,50,50))
    pygame.draw.rect(screen, boxColor, nextBackground, 0 ,10)
    
    
    
    if game.gameOver == True:
        screen.blit(gameOver_txt , (20,510,50,50))
        
    game.draw(screen)
    
    pygame.display.update()
    #Ograniczenie fps do 60
    clock.tick(60) 