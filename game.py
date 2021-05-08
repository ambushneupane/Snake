import pygame, random, sys
from pygame.math import Vector2


class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]  # [(200,400),(240,400),(280,400) adding 40 ]
        self.direction = Vector2(1, 0)

        self.body_bl = pygame.image.load('Images/body_bl.png').convert_alpha()
        self.body_br = pygame.image.load('Images/body_br.png').convert_alpha()
        self.body_horizontal = pygame.image.load('Images/body_horizontal.png').convert_alpha()
        self.body_tl = pygame.image.load('Images/body_tl.png').convert_alpha()
        self.body_tr = pygame.image.load('Images/body_tr.png').convert_alpha()
        self.body_vertical = pygame.image.load('Images/body_vertical.png').convert_alpha()

        self.head_down = pygame.image.load('Images/head_down.png').convert_alpha()
        self.head_left = pygame.image.load('Images/head_left.png').convert_alpha()
        self.head_right = pygame.image.load('Images/head_right.png').convert_alpha()
        self.head_up = pygame.image.load('Images/head_up.png').convert_alpha()

        self.tail_down = pygame.image.load('Images/tail_down.png').convert_alpha()
        self.tail_left = pygame.image.load('Images/tail_left.png').convert_alpha()
        self.tail_right = pygame.image.load('Images/tail_right.png').convert_alpha()
        self.tail_up = pygame.image.load('Images/tail_up.png').convert_alpha()

    def draw_snake(self):
        self.upade_head_graphics()
        self.update_tail_graphics()

        for index, block in enumerate(self.body):
            X_POS = int(block.x * cell_size)
            Y_POS = int(block.y * cell_size)
            block_rect = pygame.Rect(X_POS, Y_POS, cell_size, cell_size)

            if index == 0:
                screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)

            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                    screen.blit(self.body_horizontal, block_rect)

    def upade_head_graphics(self):

        head_relation = self.body[1] - self.body[0]

        if head_relation == Vector2(1, 0):
            self.head = self.head_left
        elif head_relation == Vector2(-1, 0):
            self.head = self.head_right
        elif head_relation == Vector2(0, 1):
            self.head = self.head_up
        elif head_relation == Vector2(0, -1):
            self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1, 0):
            self.tail = self.tail_left

        if tail_relation == Vector2(-1, 0):
            self.tail = self.tail_right

        if tail_relation == Vector2(0, 1):
            self.tail = self.tail_up

        if tail_relation == Vector2(0, -1):
            self.tail = self.tail_down

    def move_snake(self):
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]

    def add_block(self):
        body_copy = self.body[:]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]


class FRUIT:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        # pygame.draw.rect(screen,(126,166,114),fruit_rect)
        screen.blit(fruit_img, fruit_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)


class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def update(self):
        self.snake.move_snake()

        self.collision()
        self.destruction()

    def draw_element(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()

    def collision(self):
        self.score = 0
        if self.fruit.pos == self.snake.body[0]:  # head of the snake overlaps the fruit
            self.score += 1
            print(self.score)
            self.fruit.randomize()
            self.snake.add_block()

    def destruction(self):
        # Snake dies when it collides with the border of the screen
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
cell_size = 40
cell_number = 19
# WIDTH,HEIGHT= 400,500
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

fruit_img = pygame.image.load('Images/apple.png').convert_alpha()

main_game = MAIN()
# timer
screen_update = pygame.USEREVENT
pygame.time.set_timer(screen_update, 150)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == screen_update:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            main_game.update()

            # Controlling Snake Moments
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)

            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)

            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)

            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)

    screen.fill((175, 215, 70))
    main_game.draw_element()
    pygame.display.update()
    clock.tick(60)

pygame.quit()
