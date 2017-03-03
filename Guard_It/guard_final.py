
import pygame
import random
import time

pygame.init()

screen = pygame.display.set_mode((500,500))
white = (255,255,255)
black = (0,0,0)
purple = (80,67,189)
red_orange = (255,34,0)
greyish = (230,230,230)
grey = (180,180,180)

pygame.display.set_caption("COBRA ATTACK")

colour_list = [white,black,purple,red_orange,grey]

clock = pygame.time.Clock()

done = False

guard_left_1 = pygame.image.load("Guard_left_1.png")
guard_left_2 = pygame.image.load("Guard_left_2.png")
guard_left_3 = pygame.image.load("Guard_left_3.png")
guard_right_1 = pygame.image.load("Guard_right_1.png")
guard_right_2 = pygame.image.load("Guard_right_2.png")
guard_right_3 = pygame.image.load("Guard_right_3.png")

guard = guard_left_1#This is needed so that Pygame can assign a rectangle to the sprite it draws first.
guard_list = [guard_left_1,guard_left_2,guard_left_3,guard_right_1,guard_right_2,guard_right_3]

plant =  pygame.image.load("plant.png")

ninja = pygame.image.load("ninja.png")#Can be used for key up, change to this.Must adjust code.

ninja_left_1 = pygame.image.load("ninja_left_1.png")
ninja_left_2 = pygame.image.load("ninja_left_2.png")
ninja_left_3 = pygame.image.load("ninja_left_3.png")
ninja_right_1 = pygame.image.load("ninja_right_1.png")
ninja_right_2 = pygame.image.load("ninja_right_2.png")
ninja_right_3 = pygame.image.load("ninja_right_3.png")

character = ninja

ninja_list = [ninja_left_1,ninja_left_2,ninja_left_3,ninja_right_1,ninja_right_2,ninja_right_3]

class Player():
    def __init__(self,x,y,show):
        self.x = x
        self.y = y
        self.show = show
        image_count = 3
        self.image_count = image_count
        
    def draw(self,screen):
        if self.show == True:
            character_rectangle = character.get_rect()
            character_rectangle.move_ip(self.x,self.y)
            screen.blit(ninja_list[self.image_count],(self.x,self.y))
        elif self.show == False:
            screen.blit(plant,(self.x,self.y))

    def left(self):
        if self.image_count > 2:
            self.image_count = 0
        if self.show == True:
            self.x -= 10
            self.image_count += 1
            if self.image_count > 2:
                self.image_count = 0
            

    def right(self):
        if self.show == True: 
            self.x += 10
            self.image_count += 1
            if self.image_count > 5:
                self.image_count = 3
            

    def show_player(self):
        self.show = True
        
    def hide(self):
        self.show = False
        

    def up(self):
        if self.x > 450 and self.y == 450:
            self.y = 300
        elif self.x < 50 and self.y == 300:
            self.y = 200
        elif self.x > 450 and self.y == 200:
            self.y = 100
        elif self.x < 50 and self.y == 100:
            self.y = 0
    
class Guard():
    
    def __init__(self,x,y,mov_ri):
        self.x = x
        self.y = y
        self.mov_ri = mov_ri
        x_speed = 1
        self.x_speed = x_speed
        image = 0#This variable is used to keep track of time to change
        self.image = image#the costumes of the guards.Change value if needed.
                          #It is set in the move function.

    def draw(self,screen):#Find the guard`s position, move rect to that position.
        if self.mov_ri == False:
            guard_rectangle = guard.get_rect()
            guard_rectangle.move_ip(self.x,self.y)
            self.left()
        else:
            guard_rectangle = guard.get_rect()
            guard_rectangle.move_ip(self.x,self.y)
            self.right()
  
        
    def left(self):
        #Use ifs to change the guards costume corisponding to self.image value.
        if self.image >= 0 and self.image < 10:
            screen.blit(guard_list[0], (self.x,self.y))#Blit to x and y.
        elif self.image >= 10 and self.image < 20:
            screen.blit(guard_list[1], (self.x,self.y))
        elif self.image >= 20 and self.image < 30:
            screen.blit(guard_list[2], (self.x,self.y))
        elif self.image >= 30:
            screen.blit(guard_list[0], (self.x,self.y))
            self.image = 0#Reset image value.Will then start increase again.

    def right(self):
        #As above, but using different costumes.
        if self.image >= 0 and self.image < 10:
            screen.blit(guard_list[3], (self.x,self.y))
        elif self.image >= 10 and self.image < 20:
            screen.blit(guard_list[4], (self.x,self.y))
        elif self.image >= 20 and self.image < 30:
            screen.blit(guard_list[5], (self.x,self.y))
        elif self.image >= 30:
            screen.blit(guard_list[3], (self.x,self.y))
            self.image = 0
        
           
    def move(self):
        self.x += self.x_speed
        self.image += 2 #Increase the value of image.
        if self.x > 450 or self.x < 0:#Change these for guards start and finish x values.
            self.x_speed = self.x_speed * -1

    def ready_to_fire_3(self):
        if guard_3.x == 0:
            guard_3.mov_ri = True
        elif guard_3.x ==450:
            guard_3.mov_ri = False

        if player.y == guard_3.y and player.x > guard_3.x and guard_3.mov_ri == True and player.show == True:
            bullet_3.can_see_player_right = True
        elif player.y == guard_3.y and player.x < guard_3.x and guard_3.mov_ri == False and player.show == True:
            bullet_3.can_see_player_left = True
        else:
             bullet_3.can_see_player_left = False
             bullet_3.can_see_player_right = False
            

    def ready_to_fire_2(self):
        if guard_2.x == 0:
            guard_2.mov_ri = True
        elif guard_2.x ==450:
            guard_2.mov_ri = False
            
        if player.y == guard_2.y and player.x > guard_2.x and guard_2.mov_ri == True and player.show == True:
            bullet_2.can_see_player_right = True
        elif player.y == guard_2.y and player.x < guard_2.x  and guard_2.mov_ri == False and player.show == True:
            bullet_2.can_see_player_left = True
        else:
             bullet_2.can_see_player_left = False
             bullet_2.can_see_player_right = False
            

    def ready_to_fire_1(self):
        if guard_1.x == 0:##############Fire right, but need to wait for this condition to be met!!!
            guard_1.mov_ri = True
        elif guard_1.x ==450:#########################################Fire left!!!
            guard_1.mov_ri = False

        if player.y == guard_1.y and player.x > guard_1.x and guard_1.mov_ri == True and player.show == True:
            bullet_1.can_see_player_right = True
        elif player.y == guard_1.y and player.x < guard_1.x  and guard_1.mov_ri == False and player.show == True:
            bullet_1.can_see_player_left = True
        else:
             bullet_1.can_see_player_left = False
             bullet_1.can_see_player_right = False
            
            

class Bullet():
    def __init__(self,x,y,can_see_player_left,can_see_player_right,guard):
        self.guard = guard
        self.x = x
        self.y = y
        fire_speed_right = 15
        self.fire_speed_right = fire_speed_right
        fire_speed_left = -15
        self.fire_speed_left = fire_speed_left
        self.can_see_player_left = can_see_player_left
        self.can_see_player_right = can_see_player_right

    def draw(self,screen):
        bullet = pygame.draw.rect(screen,black,[self.x + 24,self.y + 23,2,2])

    def update_pos(self):
        if self.can_see_player_left == False and self.can_see_player_right == False: 
            self.x = self.guard.x
            self.y = self.guard.y
        elif self.can_see_player_left == True:
            self.fire_left()
        elif self.can_see_player_right == True:
            self.fire_right()
       
    def fire_right(self):
        if self.x == 450:
            self.can_see_player_right = False
        elif self.x < 500:
            self.x += self.fire_speed_right
#########Here is the collision tset.####################
        if self.x + 5 >= player.x:
            if self.x -5 <= player.x:
                if self.y + 5 >= player.y:
                    if self.y -5 <= player.y:
                        player.x = 0
                        player.y = 450
                        
    def fire_left(self):
        if self.x == 0:
            self.can_see_player_left = False
        elif self.x > 0:
            self.x += self.fire_speed_left
############Here is one more collision test.##########
        if self.x + 5 >= player.x:
            if self.x -5 <= player.x:
                if self.y + 5 >= player.y:
                    if self.y -5 <= player.y:
                        player.x = 0
                        player.y = 450
                  
    def place(self):
        if bullet_1.x <= 0 or bullet_1.x >= 500:
            bullet_1.x = guard_1.x
            bullet_1.y = guard_1.y
        elif bullet_2.x <= 0 or bullet_2.x >= 500:
            bullet_2.x = guard_2.x
            bullet_2.y = guard_2.y
        elif bullet_3.x <= 0 or bullet_3.x >= 500:
            bullet_3.x = guard_3.x
            bullet_3.y = guard_3.y
            

class Doors():

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def draw(self,screen):
        pygame.draw.rect(screen,black,[self.x,self.y,50,50])

    def draw_two(self, screen):
        pygame.draw.rect(screen,red_orange,[self.x,self.y,50,50])

    def floors(self,screen):
        pygame.draw.rect(screen,grey,[self.x,self.y,500,10])
        

#Separate fuction for this message


#Pass in boolean values to set the guards costumes.
guard_1 = Guard(100,100,True)#These guards are set to True as their starting
#from x positions which are first increasing in value.
guard_2 = Guard(400,200,True)

guard_3 = Guard(450,300,False)#This guard is set to False as he starts at the
#edge of the screen so x is decreasing.

player = Player(0, 450,True)

#bullets!!!
bullet_1 = Bullet(guard_1.x,guard_1.y,False,False,guard_1)
bullet_2 = Bullet(guard_2.x,guard_2.y,False,False,guard_2)
bullet_3 = Bullet(guard_3.x,guard_3.y,False,False,guard_3)

##Doors!!
door_1 = Doors(450,100)
door_2 = Doors(0,200)
door_3 = Doors(450,200)
door_4 = Doors(450,450)
door_5 = Doors(0,100)
door_6 = Doors(450, 300)
door_7 = Doors(0,300)
door_8 = Doors(0,0)

floor_1 = Doors(0,50)
floor_2 = Doors(0,150)
floor_3 = Doors(0,250)
floor_4 = Doors(0,350)

#Secret weapon
secret_weapon = Doors(450,0)

#This will give the player smooth movement.
pygame.key.set_repeat(50,50)

game_over = False

#################Instructions pages######################################
pygame.display.set_caption("Instructions screen!")

font = pygame.font.Font(None, 36)

display_instructions = True

instruction_page = 1

bullet_message = 50

while display_instructions:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            instruction_page += 1
            if instruction_page == 3:
                display_instructions = False

    if instruction_page == 1:
        screen.fill(black)
        text = font.render("Use arrow keys to move", True, white)
        screen.blit(text,[50,150])
        text = font.render("Use space key to hide!", True, white)
        screen.blit(text,[50,170])
        text = font.render("Click to continue.", True, white)
        screen.blit(text,[50,190])


    elif instruction_page == 2:
        screen.fill(black)
        text = font.render("Your mission is to get the secret weapon.", True, white)
        screen.blit(text,[10,200])

    clock.tick(20)
    
    pygame.display.update()
        
##########################################################
pygame.display.set_caption("Stealth Mode!")

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.right()
            elif event.key == pygame.K_LEFT:
                player.left()
            elif event.key == pygame.K_SPACE:
                player.hide()
            elif event.key == pygame.K_UP:
                player.up()

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                player.show_player()

    if player.x >= 450 and player.y == 0:
        game_over = True
        
    screen.fill(greyish)
    #Bullets
    bullet_1.draw(screen)
    bullet_1.update_pos()
    bullet_2.draw(screen)
    bullet_2.update_pos()
    bullet_3.draw(screen)
    bullet_3.update_pos()
    bullet_1.place()
    bullet_2.place()
    bullet_3.place()
    #Draw doors
    door_1.draw(screen)
    door_2.draw(screen)
    door_3.draw(screen)
    door_4.draw(screen)
    door_5.draw(screen)
    door_6.draw(screen)
    door_7.draw(screen)
    door_8.draw(screen)
    #Player.
    player.draw(screen)
    #Draw floors.
    floor_1.floors(screen)
    floor_2.floors(screen)
    floor_3.floors(screen)
    floor_4.floors(screen)
    #Secret weapon!!
    secret_weapon.draw_two(screen)
    #Draw the guards on the screen and get them to move see Class.
    guard_1.draw(screen)
    guard_1.move()
    guard_1.ready_to_fire_1()
    guard_2.draw(screen)
    guard_2.move()
    guard_2.ready_to_fire_2()
    guard_3.draw(screen)
    guard_3.move()
    guard_3.ready_to_fire_3()
    
    bullet_message += 1
    if bullet_message < 20:
        text = font.render("You died", True, black)
        screen.blit(text,[140,200])
        text = font.render("Try again!", True, black)
        screen.blit(text,[140,220])
        
    
 
    if game_over:
        screen.fill(black)
        text = font.render("Mission completed", True, white)
        screen.blit(text,[140,200])
        text = font.render("You got the secret weapon!", True, white)
        screen.blit(text,[85,220])
        
    pygame.display.update() 
    clock.tick(20)

pygame.quit()
