import pygame
import random

# Initialize pygame
pygame.init()

# Colors
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Screen size
dis_width, dis_height = 600, 400
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Multi-Food Snake')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 8

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Number of food items at a time
num_food = 100


def score_display(score):
    value = score_font.render(f"Score: {score}", True, yellow)
    dis.blit(value, [0, 0])


def draw_snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])


def random_food():
    return [
        round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0,
        round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    ]


def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    # Start with multiple food items
    food_positions = [random_food() for _ in range(num_food)]

    while not game_over:

        while game_close:
            dis.fill(blue)
            message("You Lost! C-Play Again or Q-Quit", red)
            score_display(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_d and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_w and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_s and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)

        # Draw foods
        for food in food_positions:
            pygame.draw.rect(
                dis, green, [food[0], food[1], snake_block, snake_block])

        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(snake_list)
        score_display(length_of_snake - 1)
        pygame.display.update()

        # Check for food eaten
        for food in food_positions[:]:
            if x1 == food[0] and y1 == food[1]:
                length_of_snake += 1
                food_positions.remove(food)

        # Refill up to num_food
        while len(food_positions) < num_food:
            food_positions.append(random_food())

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()
