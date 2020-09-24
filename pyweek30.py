import pygame

class player():
    def __init__(self,x,y,w,h,hp,screen):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.hp = hp
        # self.image = image
        self.screen = screen
        self.speed = 7

        self.walk = False
        #right
        self.sprites = []
        self.sprites.append(pygame.image.load('./assets/player1.png'))
        self.sprites.append(pygame.image.load('./assets/player2.png'))
        self.sprites.append(pygame.image.load('./assets/player3.png'))
        self.sprites.append(pygame.image.load('./assets/player4.png'))
        self.sprites.append(pygame.image.load('./assets/player5.png'))
        self.sprites.append(pygame.image.load('./assets/player6.png'))
        self.sprites.append(pygame.image.load('./assets/player7.png'))

        #left
        self.sprites_left = []
        self.sprites_left.append(pygame.image.load('./assets/player_left1.png'))
        self.sprites_left.append(pygame.image.load('./assets/player_left2.png'))
        self.sprites_left.append(pygame.image.load('./assets/player_left3.png'))
        self.sprites_left.append(pygame.image.load('./assets/player_left4.png'))
        self.sprites_left.append(pygame.image.load('./assets/player_left5.png'))
        self.sprites_left.append(pygame.image.load('./assets/player_left6.png'))
        self.sprites_left.append(pygame.image.load('./assets/player_left7.png'))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x,self.y]	

        self.facing_right = True

        self.exit_right =False
        self.exit_left = False
        self.exit_top = False
        self.exit_bottom = False

    def update(self,speed):
        if self.walk == True:
            self.current_sprite +=speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.walk = False
        if self.facing_right == True:
            self.image = self.sprites[int(self.current_sprite)]
        elif self.facing_right == False:
            self.image = self.sprites_left[int(self.current_sprite)]

    def draw(self,level_data):
        # print(self.exit)
        pressed = pygame.key.get_pressed()	
        if pressed[pygame.K_LEFT]:
            self.x -= self.speed
            self.walk = True
            self.facing_right = False
        elif pressed[pygame.K_RIGHT]:
            self.x += self.speed
            self.walk = True
            self.facing_right = True
        elif pressed[pygame.K_UP]:
            self.y -= self.speed
            self.walk = True
        elif pressed[pygame.K_DOWN]:
            self.y += self.speed
            self.walk = True

        self.screen.blit(self.image,(self.x,self.y))
        # print(self.x,self.y)

        if self.x <= level_data[0][0]-80: #right edge
            self.x = level_data[0][0]-80
            if level_data[0][1] == "exit":
                self.x+=700
                self.exit_left =True
                # print("x background -1 left",self.exit_left)

                
        elif self.x+self.w >= level_data[1][0]+80:
            self.x = level_data[1][0]+80-self.w
            if level_data[1][1] == "exit":
                self.x-=700
                self.exit_right =True
                # print("x background +1 right",self.exit_right)

            
        elif self.y <= level_data[2][0]-80:
            self.y = level_data[2][0]-80
            if level_data[2][1] == "exit":
                self.y+=280
                self.exit_top =True
                # print("y background -1 up",self.exit_top)


        elif self.y+self.h >= level_data[3][0]+80:
            self.y = level_data[3][0]-self.h+80
            if level_data[3][1] == "exit":
                self.y-=280
                self.exit_bottom =True
                # print("y background +1 down",self.exit_bottom)

        else:
            self.exit_right = False
            self.exit_left = False
            self.exit_top = False
            self.exit_bottom = False
            
    def info(self):
        return [self.x,self.y,self.w,self.h,self.hp,self.image,self.screen,self.exit_right,self.exit_left,self.exit_top,self.exit_bottom]




class myObject():
    def __init__(self,x,y,w,h,outcome,image,screen,isWall):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.outcome = outcome
        self.image = image
        self.screen = screen
        self.isWall = isWall
    def draw(self):
        self.screen.blit(self.image,(self.x,self.y))
        # print(self.x,self.y)

    def collision_check(self,pX,pY,pW,pH):
        if pX+pW >= self.x: #check x axis
            if pX <= self.x+self.w:
                if pY+pH >= self.y: #check y axis
                    if pY <= self.y+self.h:
                        return True, self.isWall
        return False


class level():
    def __init__(self,x1,x2,y1,y2,screen):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.screen = screen

        # self.background_list = []
        # self.background_list.append(pygame.image.load("./assets/r0c0.png"))#,pygame.image.load("./assets/r0c1.png"),pygame.image.load("./assets/r0c2.png")
        # self.background_list.append(pygame.image.load("./assets/r0c0.png"),pygame.image.load("./assets/r0c1.png"),pygame.image.load("./assets/r0c2.png")

        self.background_count_x = 1
        self.background_count_y = 0
        # self.current_background = pygame.image.load("./assets/r0c2.png")

    # def find_background():


    def locate(self,player_exit_right,player_exit_left,player_exit_top,player_exit_bottom):
        # print("current coords: ", self.background_count_x,self.background_count_y)
        if self.background_count_x>=2:
            self.background_count_x=2

        elif self.background_count_x<=0:
            self.background_count_x=0

        if player_exit_right==True:
            self.background_count_x+=1
            # print ("++++++++++++++++++++++++++", self.background_count_x)

        elif player_exit_left==True:
            self.background_count_x-=1
            # print (self.background_count_x)

        elif player_exit_top==True:
            self.background_count_y+=1
            # print (self.background_count_y)

        elif player_exit_bottom==True:
            self.background_count_y-=1
            # print (self.background_count_y)
        return self.background_count_x,self.background_count_y


        # self.screen.blit(self.current_background,(0,0))

        # print(self.walls,self.exits)
        return [self.x1, self.x2, self.y1, self.y2]
        # return [[self.x1,exit], [self.x2,exit], [self.y1,exit], [self.y2,wall]]
        #define level borders first (where player can move)
        #then define if edge is a wall or an exit.

    def draw(self,image):
        self.screen.blit(image,(0,0))







pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("pyweek 30 - castaway") 
done = False

#images
goat = pygame.image.load("./assets/goat.png")
#backgrounds
r0c0 = pygame.image.load("./assets/r0c0.png")
r0c1 = pygame.image.load("./assets/r0c1.png")
r0c2 = pygame.image.load("./assets/r0c2.png")
r1 = pygame.image.load("./assets/r1.png")
# backgrounds= [
# [r0c0,r0c1,r0c2],
# [r1,r1,r1]
# ]

#objects
me = player(100,100,185,400,100,screen)
testObject = myObject(500,200,75,82,"poo",goat,screen,False)#loop information (for loop from list) into here for every level
testObject2 = myObject(100,400,75,82,"poo",goat,screen,True)#loop information (for loop from list) into here for every level

#game information
level1_walls_exits = [[0,"exit"],[800,"exit"],[0,"exit"],[520,"wall"]]
level1 = level(0,800,0,500,screen)







#================================================MAIN GAME LOOP============================================================
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    player_info = me.info()

    object_collision_check_result_1 = testObject.collision_check(player_info[0],player_info[1],player_info[2],player_info[3])
    object_collision_check_result_2 = testObject2.collision_check(player_info[0],player_info[1],player_info[2],player_info[3])

    object_collision_check_results = [object_collision_check_result_1, object_collision_check_result_2]

    test = level1.locate(player_info[7],player_info[8],player_info[9],player_info[10])
    level1.draw(r0c2)
    testObject.draw()
    

    me.draw(level1_walls_exits)
    print(test)
    # print(object_collision_check_result_1)
    # print(object_collision_check_result_2)
    testObject2.draw()
    me.update(0.25)
    clock.tick(60)
    pygame.display.flip()