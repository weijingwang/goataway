import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
done = False

tile = pygame.image.load("./tile.png")
back1 = pygame.image.load("./back1.png")
man = pygame.image.load("./man.png")
class player():
    def __init__(self,x,y,w,h,hp,image,screen):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.hp = hp
        self.image = image
        self.screen = screen
    def draw(self):
        pressed = pygame.key.get_pressed()	
        if pressed[pygame.K_LEFT]: self.x -= 10
        elif pressed[pygame.K_RIGHT]: self.x += 10
        elif pressed[pygame.K_UP]: self.y -= 10
        elif pressed[pygame.K_DOWN]: self.y += 10
        self.screen.blit(self.image,(self.x,self.y))
        print(self.x,self.y)
    def collide(self):
        pass

class myObject():
    def __init__(self,x,y,w,h,outcome,image,screen):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.outcome = outcome
        self.image = image
        self.screen = screen
    def draw(self):
        self.screen.blit(self.image,(self.x,self.y))
        print(self.x,self.y)

class level():
    def __init__(self,walls,exits,image,screen):
        self.walls = walls
        self.exits = exits
        self.image = image
        self.screen = screen
    def draw(self):
        self.screen.blit(self.image,(0,0))
        print(self.walls,self.exits)
        return self.walls,self.exits
    

me = player(0,0,50,50,100,man,screen)
testObject = myObject(500,200,50,50,"poo",tile,screen)
level1 = level([" "],[" "],back1,screen)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    # for gX in range(0, 800, 50):
    #     print(gX)
    #     for gY in range(0, 600, 50):
    #         print(gY)
    #         # pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(gX, gY, 50, 50))
    #         screen.blit(tile,(gX,gY))

    level1.draw()
    me.draw()
    testObject.draw()
    
    pygame.display.flip()




