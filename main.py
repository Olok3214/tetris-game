
import sys
import pygame
from gameMainMechanics import GameMechanic
from textDisplay import text
from difficultyMenu import Difficulty

pygame.init()

backgroundColor = (48 , 25,52)
txtColor = (255,255,255)
boxColor = (54,15,90)



#Wielkość okna gry
screen = pygame.display.set_mode((600,700))

dif = Difficulty()
text = text()
game = GameMechanic()

#szybkośc spadania bloków


blockFallTimer = dif.blockFallTimer



title_txt = text.renderTitle("TETRIS", txtColor)
menuTitle_txt = text.renderBigText("TETRIS" , txtColor)
score_txt = text.renderText("SCORE:", txtColor)
next_txt = text.renderText("NEXT:", txtColor)
gameOver_txt = text.renderText("GAME OVER", txtColor)
maxScore_txt= text.renderSmallText("MAX SCORE:", txtColor)
SoundtrackCredit = text.renderSmallText("Soundtrack: Kim Lightyear", txtColor)
AudioEffectsCredit = text.renderSmallText("Sound Effects: floraphonic", txtColor)
start_txt = text.renderText("PRESS SPACE TO START" , txtColor)
selectDif_txt = text.renderSmallText("Use arrows <- -> to change difficulty",txtColor)
easy_txt = text.renderText("< EASY >" , txtColor)
normal_txt = text.renderText("< NORMAL >" , txtColor)
hard_txt = text.renderText("< HARD >" , txtColor)
extreme_txt = text.renderText("< EXTREME >" , txtColor)

scoreBackground = pygame.Rect(20,120,200,80)
nextBackground = pygame.Rect(20,290,200,200)
difficultyBackground = pygame.Rect(10 , 300 , 480 , 100)

pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()

menuRunning = True
isRunning = False




timer_event = pygame.USEREVENT 
pygame.time.set_timer(timer_event , blockFallTimer)

#Menu
while menuRunning:
    for event in pygame.event.get():
        #Zamknięcie gry
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                menuRunning = False
                isRunning = True
                #Zwiększenie / zmniejszenie trudności gry i ponowne przypisanie 
            if event.key == pygame.K_LEFT:
                dif.difficultyDown()
                blockFallTimer = dif.blockFallTimer
            if event.key == pygame.K_RIGHT:
                dif.difficultyUp()
                blockFallTimer = dif.blockFallTimer
                
  
    
    screen.fill(backgroundColor)
    pygame.draw.rect(screen, boxColor, difficultyBackground,0,10)
    screen.blit(start_txt , (20,250,50,50))
    screen.blit(menuTitle_txt  , (110,40,50,50))
    screen.blit(selectDif_txt, (20,310,50,50))
    screen.blit(SoundtrackCredit,(20,670,50,50))
    screen.blit(AudioEffectsCredit, (20,645,50,50))
    
    
    if dif.blockFallTimer == 150:
        screen.blit(easy_txt, (20,350,50,50))
    elif dif.blockFallTimer == 200:
        screen.blit(normal_txt, (20,350,50,50))
    elif dif.blockFallTimer == 250:
        screen.blit(hard_txt, (20,350,50,50))
    elif dif.blockFallTimer == 50:
        screen.blit(extreme_txt, (20,350,50,50))
    
    pygame.display.update()
    clock.tick(60)



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