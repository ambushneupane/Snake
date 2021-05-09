import pygame,random,sys
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.body=[Vector2(5,10),Vector2(4,10),Vector2(3,10)] #[(200,400),(240,400),(280,400) adding 40 ]
        self.direction= Vector2(0,0)

        self.body_bl = pygame.image.load('Images/body_bl.png').convert_alpha()
        self.body_br = pygame.image.load('Images/body_br.png').convert_alpha()
        self.body_horizontal = pygame.image.load('Images/body_horizontal.png').convert_alpha()
        self.body_tl= pygame.image.load('Images/body_tl.png').convert_alpha()
        self.body_tr= pygame.image.load('Images/body_tr.png').convert_alpha()
        self.body_vertical = pygame.image.load('Images/body_vertical.png').convert_alpha()

        self.head_down = pygame.image.load('Images/head_down.png').convert_alpha()
        self.head_left= pygame.image.load('Images/head_left.png').convert_alpha()
        self.head_right = pygame.image.load('Images/head_right.png').convert_alpha()
        self.head_up= pygame.image.load('Images/head_up.png').convert_alpha()

        self.tail_down = pygame.image.load('Images/tail_down.png').convert_alpha()
        self.tail_left = pygame.image.load('Images/tail_left.png').convert_alpha()
        self.tail_right= pygame.image.load('Images/tail_right.png').convert_alpha()
        self.tail_up= pygame.image.load('Images/tail_up.png').convert_alpha()

        self.crunch_sound=pygame.mixer.Sound('Sound_crunch.wav')

    def draw_snake(self):
        self.upade_head_graphics()
        self.update_tail_graphics()


        for index,block in enumerate(self.body):
            X_POS = int(block.x * cell_size)
            Y_POS = int(block.y * cell_size)
            block_rect = pygame.Rect(X_POS,Y_POS,cell_size,cell_size)

            if index == 0:
                screen.blit(self.head,block_rect)
            elif index == len(self.body)-1:
                screen.blit(self.tail,block_rect)

            else:
                previous_block = self.body[index+1]- block
                next_block= self.body[index-1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical,block_rect)

                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal,block_rect)

                else:
                    if previous_block.x ==-1 and next_block.y == -1 or next_block.x ==-1 and previous_block.y ==-1:
                        screen.blit(self.body_tl,block_rect)
                    #
                    elif previous_block.x ==-1 and next_block.y == 1 or next_block.x ==-1 and previous_block.y ==1:
                        screen.blit(self.body_bl,block_rect)

                    elif previous_block.x ==1 and next_block.y ==-1 or next_block.x ==1 and previous_block.y ==-1:
                        screen.blit(self.body_tr,block_rect)

                    elif previous_block.x ==1 and next_block.y == 1 or next_block.x ==1 and previous_block.y ==1:
                        screen.blit(self.body_br,block_rect)






    def upade_head_graphics(self):

        head_relation = self.body[1] - self.body[0]

        if head_relation == Vector2(1,0):
            self.head=self.head_left
        elif head_relation == Vector2(-1,0):
            self.head= self.head_right
        elif head_relation == Vector2(0,1):
            self.head = self.head_up
        elif head_relation == Vector2(0,-1):
            self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation=self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1,0):
            self.tail =self.tail_left

        if tail_relation == Vector2(-1,0):
            self.tail = self.tail_right

        if tail_relation == Vector2(0,1):
            self.tail = self.tail_up

        if tail_relation == Vector2(0,-1):
            self.tail = self.tail_down



    def move_snake(self):
        body_copy= self.body[:-1]
        body_copy.insert(0,body_copy[0]+self.direction)
        self.body= body_copy[:]

    def add_block(self):
         body_copy= self.body[:]
         body_copy.insert(0, body_copy[0] + self.direction)
         self.body=body_copy[:]

    def play_sound(self):
        self.crunch_sound.play()

    def reset(self):

        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]  # [(200,400),(240,400),(280,400) adding 40 ]
        self.direction= Vector2(0,0)




class FRUIT:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        fruit_rect= pygame.Rect(int(self.pos.x*cell_size),int(self.pos.y*cell_size),cell_size,cell_size)
        # pygame.draw.rect(screen,(126,166,114),fruit_rect)
        screen.blit(fruit_img,fruit_rect)

    def randomize(self):
        self.x=random.randint(0,cell_number-1)
        self.y=random.randint(0,cell_number-1)
        self.pos= Vector2(self.x,self.y)

class MAIN:
    def __init__(self):
        self.snake= SNAKE()
        self.fruit= FRUIT()

    def update(self):
        self.snake.move_snake()

        self.collision()
        self.destruction()
    def draw_element(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()

    def collision(self):
        if self.fruit.pos == self.snake.body[0]: #head of the snake overlaps the fruit
            self.fruit.randomize()
            self.snake.add_block()
            self.snake.play_sound()

        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()

    def destruction(self):
        #Snake dies when it collides with the border of the screen
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()

        # Dies when its own head collides with it's body
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def draw_grass(self):
        grass_color=(167,209,61)
        for row in range(cell_number):
            if row % 2 == 0:
              for col in range(cell_number):
                  if col %2 ==0:
                    grass_rect= pygame.Rect(col*cell_size,row*cell_size,cell_size,cell_size)
                    pygame.draw.rect(screen,grass_color,grass_rect)

            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)


    def draw_score(self):
        score_text= str(len(self.snake.body)-3)
        score_surface= game_font.render(score_text,1,(56,74,12))
        score_x_pos= int(cell_size*cell_number -60)
        score_y_pos= int(cell_size*cell_number -40)
        score_rect= score_surface.get_rect(center=(score_x_pos,score_y_pos))
        apple_rect=fruit_img.get_rect(midright=(score_rect.left,score_rect.centery-5))
        bg_rect= pygame.Rect(apple_rect.left, apple_rect.top,apple_rect.width+score_rect.width+10,apple_rect.height)

        pygame.draw.rect(screen,(168,209,61),bg_rect)
        screen.blit(score_surface,score_rect)
        screen.blit(fruit_img,apple_rect)
        pygame.draw.rect(screen, (10, 2 , 3), bg_rect,2)

    def game_over(self):

        self.snake.reset()



pygame.init()
pygame.mixer.pre_init(44100,-16,2,512)
cell_size=35
cell_number=20
# WIDTH,HEIGHT= 400,500
screen = pygame.display.set_mode((cell_number*cell_size,cell_number*cell_size))
pygame.display.set_caption("Snake Game")
clock= pygame.time.Clock()

game_font= pygame.font.Font(None,50)


fruit_img= pygame.image.load('Images/apple.png').convert_alpha()
main_game= MAIN()
#timer
screen_update=pygame.USEREVENT
pygame.time.set_timer(screen_update,150)

running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False
        if event.type == screen_update:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            main_game.update()

           #Controlling Snake Moments
            if event.key== pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction =Vector2(0,-1)

            if event.key== pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction =Vector2(0,1)

            if event.key== pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                     main_game.snake.direction =Vector2(-1,0)

            if event.key== pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction =Vector2(1,0)



    screen.fill((175,215,70))
    main_game.draw_element()
    pygame.display.update()
    clock.tick(500)

pygame.quit()