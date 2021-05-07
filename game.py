import pygame,random,sys
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.body=[Vector2(5,10),Vector2(4,10),Vector2(3,10)] #[(200,400),(240,400),(280,400) adding 40 ]
        self.direction= Vector2(1,0)

    def draw_snake(self):
        for block in self.body:
            X_pos=int(block.x*cell_size)
            Y_pos= int(block.y*cell_size)
            block_rect= pygame.Rect(X_pos,Y_pos,cell_size,cell_size)
            pygame.draw.rect(screen,(0,5,2),block_rect)

    def move_snake(self):
        body_copy= self.body[:-1]
        body_copy.insert(0,body_copy[0]+self.direction)
        self.body= body_copy[:]

    def add_block(self):
         body_copy= self.body[:]
         body_copy.insert(0, body_copy[0] + self.direction)
         self.body=body_copy[:]

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
        self.fruit.draw_fruit()
        self.snake.draw_snake()
    def collision(self):
        if self.fruit.pos == self.snake.body[0]: #head of the snake overlaps the fruit
            self.fruit.randomize()
            self.snake.add_block()

    def destruction(self):
        #Snake dies when it collides with the border of the screen
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()

        # Dies when its own head collides with it's body
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        pygame.quit()
        sys.exit()


pygame.init()
cell_size=40
cell_number=20
# WIDTH,HEIGHT= 400,500
screen = pygame.display.set_mode((cell_number*cell_size,cell_number*cell_size))
pygame.display.set_caption("Snake Game")
clock= pygame.time.Clock()

fruit_img= pygame.image.load('apple.jpg').convert_alpha()




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
    clock.tick(60)

pygame.quit()