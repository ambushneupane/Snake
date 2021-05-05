import pygame,random
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.body=[Vector2(5,10),Vector2(6,10),Vector2(7,10)] #[(200,400),(240,400),(280,400) adding 40 ]
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

class FRUIT:
    def __init__(self):
        self.x=random.randint(0,cell_number-1)
        self.y=random.randint(0,cell_number-1)
        self.pos= Vector2(self.x,self.y)

    def draw_fruit(self):
        fruit_rect= pygame.Rect(int(self.pos.x*cell_size),int(self.pos.y*cell_size),cell_size,cell_size)
        pygame.draw.rect(screen,(126,166,114),fruit_rect)



pygame.init()
cell_size=40
cell_number=20
# WIDTH,HEIGHT= 400,500
screen = pygame.display.set_mode((cell_number*cell_size,cell_number*cell_size))
pygame.display.set_caption("Snake Game")
clock= pygame.time.Clock()


fruit= FRUIT()
snake= SNAKE()

screen_update=pygame.USEREVENT
pygame.time.set_timer(screen_update,150)

running=True
while running:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            running= False
        if event.type== screen_update:
            snake.move_snake()


    screen.fill((175,215,70))
    fruit.draw_fruit()
    snake.draw_snake()
    pygame.display.update()
    clock.tick(60)

pygame.quit()