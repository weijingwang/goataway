import pygame
import random
from fadein import *
from displayText import *
pygame.mixer.pre_init()
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("goataway (pyweek 30)")
clock = pygame.time.Clock()

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
    def __init__(self,x,y,w,h,outcome,image,screen):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.outcome = outcome
        self.image = image
        self.screen = screen
        self.talking_goat = False

    def draw(self):
        self.screen.blit(self.image,(self.x,self.y))
        # print(self.x,self.y)
    # def place_all_objects(self,background_x,background_y,level_objects):
    #         background_x = level_objects[0]
    #         background_y = level_objects[1]
    #         if background_x==0 and background_y==0:
    #             pass#loop goat objects?


    def collision_check(self,pX,pY,pW,pH):
        if pX+pW >= self.x: #check x axis
            if pX <= self.x+self.w:
                if pY+pH >= self.y: #check y axis
                    if pY <= self.y+self.h:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                quit()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_SPACE:
                                    goatVoice()
                                    self.talking_goat =True
                                    # print("goat")
                                    return self.talking_goat 
        self.talking_goat =False
        return self.talking_goat

    def interaction_screen(self):
        if self.talking_goat == True:
            print("yaya!")



class level():
    def __init__(self,screen):
        self.screen = screen

        # self.background_list = []
        # self.background_list.append(pygame.image.load("./assets/r0c0.png"))#,pygame.image.load("./assets/r0c1.png"),pygame.image.load("./assets/r0c2.png")
        # self.background_list.append(pygame.image.load("./assets/r0c0.png"),pygame.image.load("./assets/r0c1.png"),pygame.image.load("./assets/r0c2.png")

        self.background_count_x = 1
        self.background_count_y = 0
        self.current_background_count_x = self.background_count_x
        self.current_background_count_y = self.background_count_y

        self.current_background = pygame.image.load("./assets/x1y0.png")


        self.level_walls_exits = [[0,"exit"],[800,"exit"],[0,"exit"],[520,"wall"]]
        self.current_level_walls_exits = self.level_walls_exits

    def set_my_background(self):
        if self.background_count_x !=self.current_background_count_x or self.background_count_y != self.current_background_count_y:
            if self.background_count_x==0 and self.background_count_y==0:
                self.current_background = pygame.image.load("./assets/x0y0.png")
                self.current_background_count_x =0
                self.current_background_count_y=0
                self.current_level_walls_exits = [[0,"wall"],[800,"exit"],[0,"exit"],[520,"wall"]]

            elif self.background_count_x==1 and self.background_count_y==0:
                self.current_background = pygame.image.load("./assets/x1y0.png")
                self.current_background_count_x =1
                self.current_background_count_y=0
                self.current_level_walls_exits = [[0,"exit"],[800,"exit"],[0,"exit"],[520,"wall"]]

            elif self.background_count_x==2 and self.background_count_y==0:
                self.current_background = pygame.image.load("./assets/x2y0.png")
                self.current_background_count_x=2
                self.current_background_count_y=0
                self.current_level_walls_exits = [[0,"exit"],[800,"wall"],[0,"exit"],[520,"wall"]]
                
            elif self.background_count_x==0 and self.background_count_y==1:
                self.current_background = pygame.image.load("./assets/y1.png")
                self.current_background_count_x=0
                self.current_background_count_y=1
                self.current_level_walls_exits = [[0,"wall"],[800,"exit"],[0,"wall"],[520,"exit"]]

            elif self.background_count_x==1 and self.background_count_y==1:
                self.current_background = pygame.image.load("./assets/x1y1.png")
                self.current_background_count_x=1
                self.current_background_count_y=1
                self.current_level_walls_exits = [[0,"exit"],[800,"exit"],[0,"exit"],[520,"exit"]]

            elif self.background_count_x==2 and self.background_count_y==1:
                self.current_background = pygame.image.load("./assets/y1.png")
                self.current_background_count_x=2
                self.current_background_count_y=1
                self.current_level_walls_exits = [[0,"exit"],[800,"wall"],[0,"wall"],[520,"exit"]]

            elif self.background_count_x==1 and self.background_count_y==2:
                self.current_background = pygame.image.load("./assets/x1y2.png")
                self.current_background_count_x=1
                self.current_background_count_y=2
                self.current_level_walls_exits = [[0,"wall"],[800,"wall"],[0,"exit"],[520,"exit"]]
            elif self.background_count_x==1 and self.background_count_y==3:
                self.current_background = pygame.image.load("./assets/x1y3.png")
                self.current_background_count_x=1
                self.current_background_count_y=3
                self.current_level_walls_exits = [[0,"wall"],[800,"exit"],[0,"exit"],[520,"exit"]]
            elif self.background_count_x==2 and self.background_count_y==3:
                self.current_background = pygame.image.load("./assets/x2y3.png")
                self.current_background_count_x=2
                self.current_background_count_y=3
                self.current_level_walls_exits = [[0,"exit"],[800,"exit"],[0,"wall"],[520,"wall"]]

            return self.current_level_walls_exits

    def decide_background(self,player_exit_right,player_exit_left,player_exit_top,player_exit_bottom):
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

        self.set_my_background()
        self.screen.blit(self.current_background,(0,0))
        return self.background_count_x,self.background_count_y, self.current_level_walls_exits


def render_all_objects(level_info,object_info,playerX,playerY,playerW,playerH):
    background_x = level_info[0]
    background_y = level_info[1]
    do_diologue = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                goatVoice()
                do_diologue = True
    if background_x == 0 and background_y == 0:
        #look at how many objects there are in object_info
        for goat in object_info[0]:
            # print(goat)
            # draw_goats = myObject(object_info[0][0],object_info[0][1],object_info[0][2],object_info[0][3],object_info[0][4],object_info[0][5],object_info[0][6])
            draw_goat = myObject(goat[0],goat[1],goat[2],goat[3],goat[4],goat[5],goat[6])
            draw_goat.draw()
            draw_goat.collision_check(playerX,playerY,playerW,playerH)
            if do_diologue ==True:
                gameIntro(screen,"goat")
                do_diologue= False
        #create objects based off given info in list with object class

    elif background_x == 1 and background_y == 0:
        for goat in object_info[1]:
            draw_goat = myObject(goat[0],goat[1],goat[2],goat[3],goat[4],goat[5],goat[6])
            draw_goat.draw()
            draw_goat.collision_check(playerX,playerY,playerW,playerH)

            if do_diologue ==True:
                gameIntro(screen,"first")
                do_diologue= False

    elif background_x == 2 and background_y == 0:
        for goat in object_info[2]:
            draw_goat = myObject(goat[0],goat[1],goat[2],goat[3],goat[4],goat[5],goat[6])
            draw_goat.draw()
            draw_goat.collision_check(playerX,playerY,playerW,playerH)
            if do_diologue ==True:
                gameIntro(screen,"goat")
                do_diologue= False
    elif background_x == 0 and background_y == 1:
        for goat in object_info[3]:
            draw_goat = myObject(goat[0],goat[1],goat[2],goat[3],goat[4],goat[5],goat[6])
            draw_goat.draw()
            draw_goat.collision_check(playerX,playerY,playerW,playerH)
            if do_diologue ==True:
                gameIntro(screen,"goat")
                do_diologue= False
    elif background_x == 1 and background_y == 1:
        for goat in object_info[4]:
            draw_goat = myObject(goat[0],goat[1],goat[2],goat[3],goat[4],goat[5],goat[6])
            draw_goat.draw()
            draw_goat.collision_check(playerX,playerY,playerW,playerH)
            if do_diologue ==True:
                gameIntro(screen,"ethan")
                do_diologue= False
    elif background_x == 2 and background_y == 1:
        for goat in object_info[5]:
            draw_goat = myObject(goat[0],goat[1],goat[2],goat[3],goat[4],goat[5],goat[6])
            draw_goat.draw()
            draw_goat.collision_check(playerX,playerY,playerW,playerH)
            if do_diologue ==True:
                gameIntro(screen,"goat")
                do_diologue= False
    elif background_x == 1 and background_y == 2:
        for goat in object_info[6]:
            draw_goat = myObject(goat[0],goat[1],goat[2],goat[3],goat[4],goat[5],goat[6])
            draw_goat.draw()
            draw_goat.collision_check(playerX,playerY,playerW,playerH)
            if do_diologue ==True:
                gameIntro(screen,"monk")
                do_diologue= False
    elif background_x == 1 and background_y == 3:
        for goat in object_info[7]:
            draw_goat = myObject(goat[0],goat[1],goat[2],goat[3],goat[4],goat[5],goat[6])
            draw_goat.draw()
            draw_goat.collision_check(playerX,playerY,playerW,playerH)
            if do_diologue ==True:
                gameIntro(screen,"second")
                do_diologue= False
    elif background_x == 2 and background_y == 3:
        for goat in object_info[8]:
            draw_goat = myObject(goat[0],goat[1],goat[2],goat[3],goat[4],goat[5],goat[6])
            draw_goat.draw()
            draw_goat.collision_check(playerX,playerY,playerW,playerH)
            if do_diologue ==True:
                gameIntro(screen,"second")
                do_diologue= False
    else:
        pass

def goatVoice():
    pygame.mixer.stop()
    whichVoice = random.choice([goat1,goat2,goat3,goat4,goat5])
    whichVoice.play()	

def displayText(surface,message,x,y,size,r,g,b):
    myfont = pygame.font.Font(None,size)
    textImage = myfont.render(message, True, (r,g,b))
    surface.blit(textImage,(x,y))

def stillScene(image,x,y,button):
	done = False
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			elif event.type == pygame.KEYDOWN: 
				if event.key == button:
					done = True
			screen.blit(image,(x,y))
			pygame.display.flip()

def gameIntro(surface,which_diologue):
    done = False
    pictureCount = 0
    sayWhat = None
    person = face_player
    skip = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pictureCount +=1
                elif event.key == pygame.K_RETURN:
                    skip = True
            if which_diologue == "first":
                if pictureCount == 0:
                    sayWhat = "where where am i?! hello hello"
                elif pictureCount == 1:
                    person = face_colonel
                    sayWhat = "over over i cant find you on the gps whe-"
                elif pictureCount == 2:
                    person = face_player
                    sayWhat = "hey guys hey guys hey guys HEEEEYYY GUYYYYSSS"
                elif pictureCount == 3:
                    person = goat
                    goatVoice()
                    sayWhat = 'baaa'
                elif pictureCount ==4:
                    person = face_player
                    sayWhat = 'shut up'
                if skip == True or pictureCount > 4:
                    done = True
                
            if which_diologue == "goat":
                if pictureCount == 0:
                    sayWhat = random.choice(["well hello there","i hate goats","hey guys","punch goat","AADWDWAAWDHWOAHDIQ*@","(*#@$Y(@*#$(@#$&","hi friend."])
                elif pictureCount == 1:
                    person = goat
                    goatVoice()
                    sayWhat = random.choice(["baaaa","meeeee","hey guys",".............","I AM SHEEP"])
                elif pictureCount == 2:
                    person = face_player
                    sayWhat = random.choice(["hey guys hey guys hey guys HEEEEYYY GUYYYYSSS","are you a gamer","how do i get out","im gonna eat you","oh no i have to poo","what is your secret?", "what is the secret of the island?"])
                elif pictureCount == 3:
                    person = goat
                    goatVoice()
                    sayWhat = random.choice(["hey guys hey guys hey guys","baaaaaaa","meee","..........","go away"])
                elif pictureCount ==4:
                    person = face_player
                    sayWhat = 'shut up'
                if skip == True or pictureCount > 4:
                    done = True

            if which_diologue == "ethan":
                if pictureCount == 0:
                    sayWhat = "A food source. finally"
                elif pictureCount == 1:
                    person = goat
                    goatVoice()
                    sayWhat = "i am not your food, i am your salvation"
                elif pictureCount == 2:
                    person = face_player
                    sayWhat = "wtf"
                elif pictureCount == 3:
                    person = goat
                    goatVoice()
                    sayWhat = "I shall be the messiah that brings u to the next level"
                elif pictureCount ==4:
                    person = face_player
                    sayWhat = "ok bro ima eat yo kids-player"
                elif pictureCount ==5:
                    person = goat
                    sayWhat = "i will become your-"
                elif pictureCount ==6:
                    person = face_player
                    sayWhat = "shut up"
                if skip == True or pictureCount > 6:
                    done = True

            if which_diologue == "monk":
                if pictureCount == 0:
                    sayWhat = "what is this!"
                elif pictureCount == 1:
                    person = monk
                    goatVoice()
                    sayWhat = "........"
                elif pictureCount == 2:
                    person = face_player
                    sayWhat = "????"
                elif pictureCount == 3:
                    person = monk
                    sayWhat = "...."
                elif pictureCount ==4:
                    person = face_player
                    sayWhat = "ok bye"
                if skip == True or pictureCount > 4:
                    done = True

            if which_diologue == "second":
                if pictureCount == 0:
                    person = face_colonel
                    sayWhat = "where are you! over"
                elif pictureCount == 1:
                    person = face_player
                    sayWhat = "apparentally i am on an island at the moment"
                elif pictureCount == 2:
                    sayWhat = "except there are goats everywhere"
                elif pictureCount == 3:
                    person = face_colonel
                    sayWhat = "i-"
                elif pictureCount ==4:
                    person = face_player
                    sayWhat = "EVERYWHERE damn...."
                elif pictureCount ==5:
                    sayWhat = "hello? hello? over over"
                    goatVoice()
                if skip == True or pictureCount > 5:
                    done = True

        pygame.draw.rect(surface, (0,0,0), pygame.Rect(0, 500, 800, 100))


        surface.blit(pygame.transform.scale(person, (100, 100)), (0, 500))
        messageText(sayWhat,100,550,20,surface,255,255,255,"Roboto")
        pygame.display.update()



#images
title = pygame.image.load(("./assets/title.png"))
#intro
intro1 = pygame.image.load(("./assets/intro1.png"))
intro2 = pygame.image.load(("./assets/intro2.png"))
intro3 = pygame.image.load(("./assets/intro3.png"))
game_start = pygame.image.load(("./assets/game_start.png"))

goat = pygame.image.load("./assets/goat.png")
monk = pygame.image.load("./assets/monk.png")
walkie_talkie = pygame.image.load("./assets/walkie_talkie.png")
face_colonel = pygame.image.load("./assets/face_colonel.png")
face_player = pygame.image.load("./assets/face_player.png")
#music
pygame.mixer.music.load("./assets/sounds/poo_short.mp3") 
pygame.mixer.music.play(-1,0.0)

goat1 = pygame.mixer.Sound("./assets/sounds/goat1.ogg")
goat2 = pygame.mixer.Sound("./assets/sounds/goat2.ogg")
goat3 = pygame.mixer.Sound("./assets/sounds/goat3.ogg")
goat4 = pygame.mixer.Sound("./assets/sounds/goat4.ogg")
goat5 = pygame.mixer.Sound("./assets/sounds/goat5.ogg")

#================================================MAIN GAME LOOP============================================================

#game information

x1y0 = level(screen)
me = player(100,100,185,400,100,screen)
my_objects = [
    #0,0
    [
        [600,150,150,164,"poo",goat,screen],
        [50,200,150,164,"poo",goat,screen],
        [330,400,150,164,"poo",goat,screen]
        ],
    #1,0
    [
        [500,200,150,164,"poo",goat,screen],
        [100,400,150,164,"poo",goat,screen]
        ],
    #2,0
    [
        [400,200,150,164,"poo",goat,screen],
        [100,400,150,164,"poo",goat,screen],
        [300,500,150,164,"poo",goat,screen]
        ],
    #0,1
    [
        [400,100,150,164,"poo",goat,screen],
        [100,400,150,164,"poo",goat,screen],
        [300,500,150,164,"poo",goat,screen]
        ],
    #1,1
    [
        [200,300,150,164,"poo",goat,screen],
        ],
    #2,1
    [
        [50,150,150,164,"poo",goat,screen],
        [100,400,150,164,"poo",goat,screen],
        [300,500,150,164,"poo",goat,screen],
        [600,200,150,164,"poo",goat,screen]
        ],
    #1,2
    [
        [50,150,299,343,"poo",monk,screen],
        ],
    #1,3
    [
        [0,180,200,100,"poo",walkie_talkie,screen],
        ],
    #2,3
    [
        ],
]
def main_game():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        player_info = me.info() # return [self.x,self.y,self.w,self.h,self.hp,self.image,self.screen,self.exit_right,self.exit_left,self.exit_top,self.exit_bottom]

        current_level_info = x1y0.decide_background(player_info[7],player_info[8],player_info[9],player_info[10])
        
        # level_data_for_my_objects = current_level_info

        render_all_objects(current_level_info,my_objects,player_info[0],player_info[1],player_info[2],player_info[3])
        

        me.draw(current_level_info[2])
        # print(current_level_info)
        # print(object_collision_check_result_1)
        # print(object_collision_check_result_2)
        
        me.update(0.25)
        clock.tick(60)
        pygame.display.flip()







# fadein(title,screen,1,False)
# stillScene(intro1,0,0,pygame.K_SPACE)
# stillScene(intro2,0,0,pygame.K_SPACE)
# stillScene(intro3,0,0,pygame.K_SPACE)
# fadein(game_start,screen,2,True)
main_game()




