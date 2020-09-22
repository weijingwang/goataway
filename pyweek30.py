import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("pyweek 30 - castaway") 

done = False

tile = pygame.image.load("./tile.png")
back1 = pygame.image.load("./back1.png")
man = pygame.image.load("./player.png")
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
        # print(self.x,self.y)
    def info(self):
        return [self.x,self.y,self.w,self.h,self.hp,self.image,self.screen]

    # def collision_check(self,objectX,objectY,objectW,objectH):
    #     if(self.x) >= objectX:
    #         self.x = self.x

    #     if(self.x) <= objectX+objectW:
    #         self.y = self.y

    #     if(self.y) >= objectY:
    #         self.y = self.y

    #     if(self.y) <= objectY+objectH:
    #         self.y = self.y


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
        # print(self.x,self.y)

    def collision_check(self,pX,pY,pW,pH):
        if pX+pW >= self.x: #check x axis
            if pX <= self.x+self.w:
                if pY+pH >= self.y: #check y axis
                    if pY <= self.y+self.h:
                        return True

class level():
    def __init__(self,walls,exits,image,screen):
        self.walls = walls
        self.exits = exits
        self.image = image
        self.screen = screen
    def draw(self):
        self.screen.blit(self.image,(0,0))
        # print(self.walls,self.exits)
        return self.walls,self.exits



level_exits = [
    ("any x",0)#LEVEL 1
]
#add: if value is not an integer, ignore term.


me = player(0,0,50,50,100,man,screen)


testObject = myObject(500,200,50,50,"poo",tile,screen)#loop information (for loop from list) into here for every level

testObject2 = myObject(100,400,50,50,"poo",tile,screen)#loop information (for loop from list) into here for every level


level1 = level([" "],[" "],back1,screen)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    player_info = me.info()

    object_collision = testObject.collision_check(player_info[0],player_info[1],player_info[2],player_info[3])
    object_collision2 = testObject2.collision_check(player_info[0],player_info[1],player_info[2],player_info[3])


    level1.draw()
    me.draw()
    testObject.draw()
    testObject2.draw()
    print(object_collision)
    print(object_collision2)
    pygame.display.flip()