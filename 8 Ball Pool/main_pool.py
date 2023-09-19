import pygame
import pymunk
import pymunk.pygame_util
import math

pygame.init()
SCREEN_WIDTH = 1500 # main screen
SCREEN_HEIGHTT = 900 # main screen
SCREEN_HEIGHT = 678
pool_height = 1200
pool_width = 669
running = True
black = (243,246,228)
# Creting the game window
Screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHTT))
pygame.display.set_caption("My Poll Game")

# Pymunk space
space = pymunk.Space()
static_body = space.static_body
draw__options =pymunk.pygame_util.DrawOptions(Screen)

# CLOCK
clock = pygame.time.Clock()
FPS = 120

# game varriables
dia = 36
pocket_dia = 66
taking_shot = True
force = 0
max_force = 10000
force_direction = 1
powering_up = False
potted_balls = []
cue_ball_potted = False
lives = 3
game_running = True
level_selecting = True
tony = True
toy = False
# colours
bg = (50,50,50)
RED = (255 , 0 , 0)
WHITE = (255 , 255 ,255)
blue = (5,110,255)
font = pygame.font.SysFont("Lato" , 30 )
large_font = pygame.font.SysFont("Lato" , 60 )
# Load image
cue_image = pygame.image.load("cue.png").convert_alpha()
table_image = pygame.image.load("pool_b_3png.png").convert_alpha()
ball_images =[]
for i in range(1,17):
    ball_image = pygame.image.load(f"ball_{i}.png").convert_alpha()
    ball_images.append(ball_image)
# Creating our ball

def draw_text(text, font , text_col, x,y):
    img = font.render(text,True,text_col)
    Screen.blit(img , (x,y))
def creat_ball(radius,pos):
    body = pymunk.Body()
    body.position = pos
    shape = pymunk.Circle(body,radius)
    shape.mass = 5
    shape.elasticity = 0.8
    pivot =pymunk.PivotJoint(static_body,body,(0,0),(0,0))
    pivot.max_bias = 0
    pivot.max_force = 500

    space.add(body,shape,pivot)
    return shape
# Game baall settinng up
balls = []
rows = 5

# pollotting balls
for col in range(5):
    for row in range(rows):
        pos = (250 + (col* (dia+1)),267 + (row * (dia+1)) + (col * dia / 2) )
        new_ball = creat_ball(dia / 2,pos)
        balls.append(new_ball)
    rows -= 1
# cue ball positions
pos = (930,SCREEN_HEIGHT/ 3 + 113)
cue_ball = creat_ball(dia / 2,pos)
balls.append(cue_ball)

# Creating six pockets for pool game

pockets =  [
    (50, 60),
    (592, 48),
    (1134, 64),
    (55, 616),
    (592, 629),
    (1134, 616)
]

# creat pool table cushions
cushions = [
    [(85,56),(104,77),(565,77),(574,56)],
    [(636, 55), (639, 76), (1104, 76), (1130, 55)],
    [(80, 636), (98, 614), (568, 614), (574, 636)],
    [(632, 636), (640, 617), (1135, 636), (1109, 617)],
    [(40, 86), (60, 113), (60, 579), (43, 599)],
    [(1167, 90), (1145, 115), (1145, 574), (1167, 595)]
]
# Functions for crating colusitons
def creat_cushion(poly_dims):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = ((0,0))
    shape = pymunk.Poly(body, poly_dims)
    shape.elasticity=0.8
    space.add(body,shape)
for c in cushions:
    creat_cushion(c)

class Cue():
    def __init__(self,pos):
        self.original_image = cue_image
        self.angel = 0
        self.image = pygame.transform.rotate(self.original_image,self.angel)
        self.rect = self.image.get_rect()
        self.rect.center = pos
    def update(self, angel):
        self.angel = angel
    def draw(self, surface):
        self.image = pygame.transform.rotate(self.original_image,self.angel)
        surface.blit(self.image,
                     (self.rect.centerx - self.image.get_width() / 2,
                     self.rect.centery - self.image.get_height() / 2)
    )

cue = Cue(balls[-1].body.position)

# creatinng power bars to show how strrong the ball will hit
power_bar = pygame.Surface((10 , 20))
power_bar.fill(RED)

### aadding speiaal componends to my 8 ball pool
textfont = pygame.font.SysFont("PFR",40)
text_1 = textfont.render("S-EFFECTS",1,(25,45,56))                                        # adding texts




### styling giving new features to my pool game
style = True
pic_2 = pygame.image.load("first_page_7.png").convert_alpha()
pic_3 = pygame.image.load("first_page_8.png").convert_alpha()
pic_4 = pygame.image.load("first_page_11 - Copy.png").convert_alpha()
pic_5 = pygame.image.load("first_page_12 - Copy.png").convert_alpha()
pic_1 = "rfirst_page_3.png"
first_image = pygame.image.load(pic_1)
start_img = pygame.image.load("start.png").convert_alpha()
exit_img  = pygame.image.load("exit.png").convert_alpha()

pic_b_1 = pygame.image.load("buu.png").convert_alpha()
pic_b_2 = pygame.image.load("buuu.png").convert_alpha()
pic_b_3 = pygame.image.load("buuu.png").convert_alpha()
pic_b_4 = pygame.image.load("buuuu.png").convert_alpha()
pic_b_5 = pygame.image.load("buuuuu.png").convert_alpha()

pic_11223 = pygame.image.load("price.jpg").convert_alpha()
pic_110 = pygame.image.load("board_10.png").convert_alpha()
pic_111 = pygame.image.load("board_11.png").convert_alpha()
pic_210 = pygame.image.load("boooo.jpg").convert_alpha()   # adding level button
pic_290 = pygame.image.load("s_2.jpg").convert_alpha()
pic_295 = pygame.image.load("s_9.jpg").convert_alpha()

pic_1222  = pygame.image.load("images.png").convert_alpha()
pic_395 = pygame.image.load("s_221.jpg").convert_alpha()
copy_1 = pygame.image.load("copy.png").convert_alpha()

level_decideing = pygame.image.load("ba_7.png").convert_alpha()

add_1 = pygame.image.load("boooo_1.jpg").convert_alpha()
add_2 = pygame.image.load("boooo_3.jpg").convert_alpha()
add_3 = pygame.image.load("boooo_4.jpg").convert_alpha()

ok_button = pygame.image.load("okkk.png").convert_alpha()
ok_button_2 = pygame.image.load("okkk - Copy.png").convert_alpha()
ok_button_3 = pygame.image.load("okkk - Copy (2).png").convert_alpha()
ok_button_4 = pygame.image.load("okkk - Copy (3).png").convert_alpha()
###
### maaking buttons

class Button():
    def __init__(self,x,y,image,scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image , (int(width * scale) , int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

    def draw(self):
        action =  False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        Screen.blit(self.image, (self.rect.x , self.rect.y))

        return action

## creating classic buttons
start_button = Button(200 ,550 , start_img , 1.05)
exit_button = Button(700 ,540 ,exit_img , 1.22)
new_button = Button(1220,90,pic_b_1,1.3)
new_button_2 = Button(1220,230,pic_b_2,1.3)
new_button_3 = Button(1220,370,pic_b_3,1.3)
new_button_4 = Button(1220,510,pic_b_4,1.3)
new_button_5 = Button(1220,650,pic_b_5,1.3)

le_button  = Button(500,500,pic_210,1.3)
addd_1 = Button(70,350,add_1,0.8)
addd_2 = Button(630,350,add_2,0.8)
addd_3 = Button(355,350,add_3,0.8)


oko = Button(400,640,ok_button,0.8)
oko_2 = Button(400,640,ok_button_2,0.8)
oko_3 = Button(400,600,ok_button_3,0.8)
oko_4 = Button(400,600,ok_button_4,0.8)
done = Button(500,250,pic_1222,1.2)
goat = True
cow = True
dear = True
cat = True
while running:

    clock.tick(FPS)
    space.step(1 / FPS)
    Screen.fill(bg)

    # Drawing pool table

    Screen.blit(table_image,(0,6))

    # cheaking  balls are in pockeet or not
    for i, ball in enumerate(balls):
        for pocket in pockets:
            ball_x_dist = abs(ball.body.position[0] - pocket[0])
            ball_y_dist = abs(ball.body.position[1] - pocket[1])
            ball_dist = math.sqrt((ball_x_dist ** 2) + (ball_y_dist ** 2 ))
            if ball_dist <= pocket_dia / 2:
                if i == len(balls) - 1:
                    lives -= 1
                    cue_ball_potted = True
                    ball.body.position  = (-100,-100)
                    ball.body.velocity=(0.0,0.0)
                else:
                    space.remove(ball.body)
                    balls.remove(ball)
                    potted_balls.append(ball_images[i])
                    ball_images.pop(i)

    #print(potted_balls)
    #drawing ball images
    for i, ball in enumerate(balls):
        Screen.blit(ball_images[i],(ball.body.position[0] - ball.radius , ball.body.position[1] -ball.radius))

    # checking collusion between ball and stick
    taking_shot = True
    for ball in balls:
        if int(ball.body.velocity[0]) != 0  or int(ball.body.velocity[1]) != 0 :
            taking_shot = False

    if taking_shot == True and game_running == running:
        if cue_ball_potted == True:
            balls[-1].body.position = (888 , SCREEN_HEIGHTT/3)
            cue_ball_potted = False
        mouse_pos = pygame.mouse.get_pos()
        cue.rect.center = balls[-1].body.position
        x_dist = balls[-1].body.position[0] - mouse_pos[0]
        y_dist = -(balls[-1].body.position[1] - mouse_pos[1])
        cue_angel = math.degrees(math.atan2(y_dist , x_dist))
        cue.update(cue_angel)
        cue.draw(Screen)

    if powering_up == True and game_running == True:
        force += 100 * force_direction
        if force >= max_force or force <= 0:
            force_direction *= -1
        for b in range(math.ceil(force / 2000)):
            Screen.blit(power_bar , (balls[-1].body.position[0] + (b * 15) - 30, balls[-1].body.position[0] + 30))
    elif powering_up == False and taking_shot == True:
        x_impulse = math.cos(math.radians(cue_angel))
        y_impulse = math.sin(math.radians(cue_angel))
        balls[-1].body.apply_impulse_at_local_point((force * -x_impulse, force * y_impulse), (0, 0))
        force = 0
        force_direction = 1
    draw_text("LIVES : " + str(lives), font ,WHITE , 1100 , 700 )
    # drawing the potted balls
    for i, ball in enumerate(potted_balls):
        Screen.blit(ball, (10 + (i * 50) ,700 + 30 ))

    if lives <= 0 :
        draw_text("GAME OVER , GREAT JOB YOU HAVE PLAYED WELL" , large_font, WHITE ,SCREEN_WIDTH/4 - 230,SCREEN_HEIGHTT/3 )
        game_running = False

    if len(balls) == 1:
        draw_text("Victory is yours , Great job ,  " , large_font, WHITE ,SCREEN_WIDTH/4 - 130,SCREEN_HEIGHTT/3 )
        game_running = False
    pygame.draw.line(Screen,WHITE,(925 ,74),(925,613))
    pygame.draw.line(Screen, blue, (0,690),(1200,690))
    pygame.draw.line(Screen, blue, (0, 730), (1200, 730))
    pygame.draw.line(Screen, blue, (1200, 690), (1200, 770))
    pygame.draw.line(Screen, WHITE, (0, 770), (1200, 770))

    draw_text("To check your diffexulty level please check here -----------------------------------------------------------------------", font, WHITE, 30, 700)

    # Drawing a box to add inovative features to a game
    pygame.draw.rect(Screen,black,[1210,20 ,280,750])
    pygame.draw.line(Screen,blue,(1210,50),(1490,50))
    Screen.blit(text_1,(1270,22))# adding the previous text
    Screen.blit(pic_290,(0,200))
    Screen.blit(pic_395,(50,300))

    if style == True :
        Screen.blit(first_image, (0, 0))
        Screen.blit(pic_2, (100 , 100 ))
        Screen.blit(pic_3, (400 , 100 ))
        Screen.blit(pic_4, (700, 100))
        Screen.blit(pic_5, (1100, 100))
        draw_text("Created by - Eren Yeager",large_font,WHITE,100,200)
        if start_button.draw():
            style = False
        elif exit_button.draw():
            pygame.quit()


    if style == False:
        pic_395 = copy_1
        if goat == True and cat == True:
            draw_text("Welcome to 8 ball pool,i hope you enjoy this game , The rules are pretty simple", font, WHITE, 110,400 )
            draw_text(
                "play this game and give your best  to creat the heighest score ",
                font, WHITE, 110, 450)
            draw_text(
                " Two players cant play this game at a same timme , its not a multiplayer game ",
                font, WHITE, 110, 500)

            draw_text(
                "                                       For further information please go to next page   ",
                font, WHITE, 110, 550)
        if dear == True:
            if oko.draw():
                goat = False
        if goat == False and cow == True:
            draw_text("                Rules of this game                  ,",large_font,WHITE,110,400)
            draw_text("1. you can choose your diffeculty Level according to your exprience",font,WHITE,110,450)
            draw_text("2. You have to put all the balls to clear the game , ball colour does'not matter here",font,WHITE,110,500)
            draw_text("3. you get the lives by depending upon what duffecullty level you choose like ",font,WHITE,110,550)
            draw_text("if choose easy then you will get 5 lives but if you choose hard you will get one",font,WHITE,110,600)
            cat = False

        if goat == False and cat == False:
           # print("iron man")
            if done.draw():
                copy_1 =  pic_11223
                cat = False
                cow = False
                goat = True
                dear = False
    if style == False :

        if new_button.draw():
           table_image = pic_110
        elif new_button_2.draw():
           table_image = pic_111
        elif new_button_4.draw():
            print("c")
        elif new_button_5.draw():
            pass
        if new_button_3.draw() and tony == True:
           pic_290 = level_decideing
           toy = True
        if tony == False:
            pic_290 = pic_295



        draw_text("Red ground", large_font, WHITE, 1235, 125)
        draw_text("GRN ground", large_font, WHITE, 1235, 265)
        draw_text("LEVEL", large_font, WHITE, 1270, 405)
        draw_text("RDJ", large_font, WHITE, 1270, 545)
        draw_text("Settings", large_font, WHITE, 1250, 680)

        ## Drawing Levels



    if style == False and toy == True:

        if addd_1.draw():
            lives = 5
        elif addd_2.draw():
            lives = 1
        elif addd_3.draw():
            lives = 2
        draw_text("Easy", large_font, WHITE, 100, 355)
        draw_text("Medium", large_font, WHITE, 356, 355)
        draw_text("Hard", large_font, WHITE, 659, 355)



    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
               style = False
        if style == False:
            if event.type == pygame.MOUSEBUTTONDOWN and taking_shot == True:
                powering_up = True
            if event.type == pygame.MOUSEBUTTONUP and taking_shot == True:
                powering_up = False

    pygame.display.update()
pygame.quit()



#   A6kCFus@VMAWm2h