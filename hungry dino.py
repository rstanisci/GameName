from gamelib import *

game = Game(640, 460, "Hungry Dino")

bk = Image("images\\city.png", game)
bk.resizeTo(game.width, game.height)
game.setBackground(bk)

title = Image("images\\dinologo.png",game)
bk.draw()
title.draw()
game.drawText("Press [SPACE] to Begin",320, 400)
game.update(1)
game.wait(K_SPACE)

dino = Image("images\\dino.gif",game)

bricks = Image("images\\bricks.png",game)
bricks.moveTo(game.width/2, game.height-50)
bricks.resizeTo(game.width, bricks.height)


cake = Image("images\\cake.png",game)
cake.resizeBy(-80)
y = randint(100,300)
cake.moveTo(game.width+100,y)
cake.setSpeed(5, 90)

blue = Image("images\\blue.png",game)
blue.setSpeed(5, 90)
blue.moveTo(cake.x,cake.y + 175)




gameover= Image("images\\gameoverr.png",game)

while not game.over:
    game.processInput()
     
    game.scrollBackground("left",2)
    dino.draw()
    bricks.draw()
    cake.move()
    blue.move()
    
    
    
    if keys.Pressed[K_SPACE]:
        dino.y -= 7

    if dino.collidedWith(cake):
        cake.makeVisible(False)
        game.score += 10

    if blue.isOffScreen("left"):
        x = game.width + 10
        y = randint(100,300)
        cake.moveTo(x , y)
        cake.makeVisible(True)
        blue.moveTo(cake.x, cake.y + 175)
        
    
    if dino.collidedWith(bricks,"rectangle") or dino.collidedWith(blue,"rectangle"):
        game.over = True
        
    dino.y += 2
    game.displayScore()
    game.update(30)
    
gameover.draw()
game.drawText("Press [SPACE] to Exit",320, 400)
game.update(1)
game.update(1)
game.quit()
