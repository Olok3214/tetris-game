
import sys
import pygame
from gameMainMechanics import GameMechanic
from textDisplay import text
from difficultyMenu import Difficulty

pygame.init()

backgroundColor = (48 , 25,52)
boxColor = (54,15,90)
titleFontColor =  (255,255,102)


#Wielkość okna gry
screen = pygame.display.set_mode((600,720))

dif = Difficulty()
text = text()
game = GameMechanic()

#szybkośc spadania bloków


blockFallTimer = dif.blockFallTimer



title_txt = text.renderTitle("TETRIS")
menuTitle_txt = text.renderBigText("TETRIS" , titleFontColor)
score_txt = text.renderText("SCORE:")
next_txt = text.renderText("NEXT:")
gameOver_txt = text.renderText("GAME OVER")
maxScore_txt= text.renderSmallText("MAX SCORE:")
SoundtrackCredit = text.renderSmallText("Soundtrack: Kim Lightyear")
AudioEffectsCredit = text.renderSmallText("Sound Effects: floraphonic")
FontCredit = text.renderSmallText("Font: tylerdunn99")
Author_txt = text.renderSmallText("Bartosz Godzieszka")
start_txt = text.renderText("PRESS SPACE TO START")
selectDif_txt = text.renderSmallText("Use arrows <- -> to change difficulty")
easy_txt = text.renderText("< EASY >")
normal_txt = text.renderText("< NORMAL >")
hard_txt = text.renderText("< HARD >")
extreme_txt = text.renderText("< EXTREME >")

#controls
control_txt = text.renderSmallText("Controls:")
moveLeft_txt = text.renderSmallText("Move right:  ->")
moveRight_txt = text.renderSmallText("Move left:  <-")
moveDown_txt = text.renderSmallText("Move down:  ^")
rotate_txt = text.renderSmallText("Rotate: \/")

scoreBackground = pygame.Rect(20,120,200,80)
nextBackground = pygame.Rect(20,290,200,200)
difficultyBackground = pygame.Rect(10 , 300 , 480 , 100)

pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()

menuRunning = True
isRunning = False




timer_event = pygame.USEREVENT 


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
                
  
    #Wyświetlanie menu
    screen.fill(backgroundColor)
    pygame.draw.rect(screen, boxColor, difficultyBackground,0,10)
    screen.blit(start_txt , (20,250,50,50))
    screen.blit(menuTitle_txt  , (110,80,50,50))
    screen.blit(selectDif_txt, (20,310,50,50))
    screen.blit(SoundtrackCredit,(20,670,50,50))
    screen.blit(AudioEffectsCredit, (20,645,50,50))
    screen.blit(FontCredit, (20,695,50,50))
    screen.blit(Author_txt, (10,10,50,50))
    
    screen.blit(control_txt,(20,420,50,50))
    screen.blit(moveRight_txt,(20,440,50,50))
    screen.blit(moveLeft_txt,(20,460,50,50))
    screen.blit(moveDown_txt,(20,480,50,50))
    screen.blit(rotate_txt,(20,500,50,50))
    
    #Wyświetlanie aktualnego poziomu trudności
    if dif.blockFallTimer == dif.easy:
        screen.blit(easy_txt, (20,350,50,50))
    elif dif.blockFallTimer == dif.normal:
        screen.blit(normal_txt, (20,350,50,50))
    elif dif.blockFallTimer == dif.hard:
        screen.blit(hard_txt, (20,350,50,50))
    elif dif.blockFallTimer == dif.extreme:
        screen.blit(extreme_txt, (20,350,50,50))
    
    pygame.display.update()
    clock.tick(60)
    
#Ustawienie timera do opadania bloków
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
    scoreValue = text.renderText(str(game.score))
    #max score
    maxScoreValue = text.renderText(str(game.maxScore))
    
    #Rysowanie elementów menu gry
    screen.fill(backgroundColor)
    screen.blit(title_txt , (20,20,50,50))
    screen.blit(score_txt , (20,80,50,50))
    screen.blit(SoundtrackCredit,(20,670,50,50))
    screen.blit(AudioEffectsCredit, (20,645,50,50))
    screen.blit(FontCredit, (20,695,50,50))
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