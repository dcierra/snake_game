import pygame
from time import sleep
from random import randint
from sys import exit

def game_over():
    game_over_font = pygame.font.SysFont('Times New Roman', 50)
    game_over_surface = game_over_font.render(f'Вы проиграли со счетом: {score}', True, red_color)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_size[0] // 2, window_size[1] // 4)
    window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    sleep(3)
    pygame.quit()
    exit()

def show_score():
    score_font = pygame.font.SysFont('Times New Roman', 25)
    score_surface = score_font.render('Счет: ' + str(score), True, white_color)
    score_rect = score_surface.get_rect()
    score_rect.midtop = (window_size[0] // 10, 15)
    window.blit(score_surface, score_rect)

if __name__ == '__main__':
    pygame.init()

    window_size = (800, 600)
    pygame.display.set_caption('Змейка')
    window = pygame.display.set_mode(window_size)
    background = pygame.image.load('images/bg_snake.jpg')

    black_color = pygame.Color(0, 0, 0)
    white_color = pygame.Color(255, 255, 255)
    red_color = pygame.Color(255, 0, 0)
    green_color = pygame.Color(0, 255, 0)

    speed = pygame.time.Clock()

    snake_cord = [window_size[0] // 2, window_size[1] // 2]
    snake_body = [[window_size[0] // 2, window_size[1] // 2]]

    food_cord = [randint(1, (window_size[0] // 10)) * 10, randint(1, (window_size[1] // 10)) * 10]

    direction_snake = 'UP'
    change_direction = direction_snake

    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_direction = 'UP'
                if event.key == pygame.K_DOWN:
                    change_direction = 'DOWN'
                if event.key == pygame.K_LEFT:
                    change_direction = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    change_direction = 'RIGHT'

        if change_direction == 'UP' and direction_snake != 'DOWN':
            direction_snake = 'UP'
        if change_direction == 'DOWN' and direction_snake != 'UP':
            direction_snake = 'DOWN'
        if change_direction == 'LEFT' and direction_snake != 'RIGHT':
            direction_snake = 'LEFT'
        if change_direction == 'RIGHT' and direction_snake != 'LEFT':
            direction_snake = 'RIGHT'

        if direction_snake == 'UP':
            snake_cord[1] -= 10
        if direction_snake == 'DOWN':
            snake_cord[1] += 10
        if direction_snake == 'LEFT':
            snake_cord[0] -= 10
        if direction_snake == 'RIGHT':
            snake_cord[0] += 10

        snake_body.insert(0, list(snake_cord))

        if snake_cord[0] == food_cord[0] and snake_cord[1] == food_cord[1]:
            score += 1
            food_cord = [randint(1, (window_size[0] // 10)) * 10, randint(1, (window_size[1] // 10)) * 10]
        else:
            snake_body.pop()

        window.blit(background, (0, 0))

        for cord in snake_body:
            pygame.draw.rect(window, green_color, pygame.Rect(cord[0], cord[1], 10, 10))

        if (snake_cord[0] < 0 or snake_cord[0] > window_size[0] - 10) or (snake_cord[1] < 0 or snake_cord[1] > window_size[1] - 10):
            game_over()

        for block in snake_body[1:]:
            if snake_cord[0] == block[0] and snake_cord[1] == block[1]:
                game_over()

        pygame.draw.rect(window, red_color, pygame.Rect(food_cord[0], food_cord[1], 10, 10))

        show_score()

        pygame.display.update()

        speed.tick(20)
