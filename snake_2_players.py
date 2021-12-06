import pygame
from time import sleep
from random import randint
from sys import exit

def game_over():
    game_over_font = pygame.font.SysFont('Times New Roman', 40)

    if score_player_1 >= score_player_2:
        game_over_surface = game_over_font.render(f'Победил игрок 1 со счетом: {score_player_1}', True, red_color)
    else:
        game_over_surface = game_over_font.render(f'Победил игрок 2 со счетом: {score_player_2}', True, red_color)

    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_size[0] // 2, window_size[1] // 4)
    window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    sleep(3)
    pygame.quit()
    exit()

def show_score():
    score_font = pygame.font.SysFont('Times New Roman', 15)

    score_player_1_surface = score_font.render('Счет первого игрока: ' + str(score_player_1), True, white_color)
    score_player_1_rect = score_player_1_surface.get_rect()
    score_player_1_rect.midtop = (window_size[0] // 10, 15)
    score_player_2_surface = score_font.render('Счет второго игрока: ' + str(score_player_2), True, white_color)
    score_player_2_rect = score_player_2_surface.get_rect()
    score_player_2_rect.midtop = (window_size[0] - 80, 15)

    window.blit(score_player_1_surface, score_player_1_rect)
    window.blit(score_player_2_surface, score_player_2_rect)

if __name__ == '__main__':
    pygame.init()

    #Определение главного окна
    window_size = (800, 600)
    pygame.display.set_caption('Змейка')
    window = pygame.display.set_mode(window_size)

    #Определение фона
    background = pygame.image.load('images/bg_snake.jpg')

    #Определение цветов
    black_color = pygame.Color(0, 0, 0)
    white_color = pygame.Color(255, 255, 255)
    red_color = pygame.Color(255, 0, 0)
    green_color = pygame.Color(0, 255, 0)

    #Скорость игры
    speed = pygame.time.Clock()

    #Координаты появления игрока
    snake_cord_player_1 = [window_size[0] // 2, window_size[1] // 2]
    snake_cord_player_2 = [window_size[0] // 2 - 100, window_size[1] // 2 - 100]

    #Создание тела игрока
    snake_body_player_1 = [[window_size[0] // 2, window_size[1] // 2]]
    snake_body_player_2 = [[window_size[0] // 2 - 100, window_size[1] // 2 - 100]]

    #Координаты появления еды
    food_cord = [randint(1, (window_size[0] // 10) - 1) * 10, randint(1, (window_size[1] // 10) - 1) * 10]

    #Траектория движения по умолчанию
    direction_snake_player_1 = 'UP'
    change_direction_player_1 = direction_snake_player_1
    direction_snake_player_2 = 'UP'
    change_direction_player_2 = direction_snake_player_2

    #Счет
    score_player_1 = 0
    score_player_2 = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over()
            #Определение траектории движения по нажатой клавише
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_direction_player_1 = 'UP'
                if event.key == pygame.K_DOWN:
                    change_direction_player_1 = 'DOWN'
                if event.key == pygame.K_LEFT:
                    change_direction_player_1 = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    change_direction_player_1 = 'RIGHT'
                if event.key == ord('w'):
                    change_direction_player_2 = 'UP'
                if event.key == ord('s'):
                    change_direction_player_2 = 'DOWN'
                if event.key == ord('a'):
                    change_direction_player_2 = 'LEFT'
                if event.key == ord('d'):
                    change_direction_player_2 = 'RIGHT'

        #Проверка, что направление движения правильное
        if change_direction_player_1 == 'UP' and direction_snake_player_1 != 'DOWN':
            direction_snake_player_1 = 'UP'
        if change_direction_player_1 == 'DOWN' and direction_snake_player_1 != 'UP':
            direction_snake_player_1 = 'DOWN'
        if change_direction_player_1 == 'LEFT' and direction_snake_player_1 != 'RIGHT':
            direction_snake_player_1 = 'LEFT'
        if change_direction_player_1 == 'RIGHT' and direction_snake_player_1 != 'LEFT':
            direction_snake_player_1 = 'RIGHT'
        if change_direction_player_2 == 'UP' and direction_snake_player_2 != 'DOWN':
            direction_snake_player_2 = 'UP'
        if change_direction_player_2 == 'DOWN' and direction_snake_player_2 != 'UP':
            direction_snake_player_2 = 'DOWN'
        if change_direction_player_2 == 'LEFT' and direction_snake_player_2 != 'RIGHT':
            direction_snake_player_2 = 'LEFT'
        if change_direction_player_2 == 'RIGHT' and direction_snake_player_2 != 'LEFT':
            direction_snake_player_2 = 'RIGHT'

        #Изменение движения
        if direction_snake_player_1 == 'UP':
            snake_cord_player_1[1] -= 10
        if direction_snake_player_1 == 'DOWN':
            snake_cord_player_1[1] += 10
        if direction_snake_player_1 == 'LEFT':
            snake_cord_player_1[0] -= 10
        if direction_snake_player_1 == 'RIGHT':
            snake_cord_player_1[0] += 10
        if direction_snake_player_2 == 'UP':
            snake_cord_player_2[1] -= 10
        if direction_snake_player_2 == 'DOWN':
            snake_cord_player_2[1] += 10
        if direction_snake_player_2 == 'LEFT':
            snake_cord_player_2[0] -= 10
        if direction_snake_player_2 == 'RIGHT':
            snake_cord_player_2[0] += 10

        # Проверка на то, съедена ли еда, если да, то тело и счетчик очков увеличивается
        snake_body_player_1.insert(0, list(snake_cord_player_1))
        snake_body_player_2.insert(0, list(snake_cord_player_2))
        if snake_cord_player_1[0] == food_cord[0] and snake_cord_player_1[1] == food_cord[1]:
            score_player_1 += 1
            food_cord = [randint(1, (window_size[0] // 10) - 1) * 10, randint(1, (window_size[1] // 10) - 1) * 10]
        else:
            snake_body_player_1.pop()
        if snake_cord_player_2[0] == food_cord[0] and snake_cord_player_2[1] == food_cord[1]:
            score_player_2 += 1
            food_cord = [randint(1, (window_size[0] // 10) - 1) * 10, randint(1, (window_size[1] // 10) - 1) * 10]
        else:
            snake_body_player_2.pop()

        window.blit(background, (0, 0))

        #Отрисовка игроков
        for cord in snake_body_player_1:
            pygame.draw.rect(window, green_color, pygame.Rect(cord[0], cord[1], 10, 10))
        for cord in snake_body_player_2:
            pygame.draw.rect(window, white_color, pygame.Rect(cord[0], cord[1], 10, 10))

        #Проверка чтобы игрок не выходил за поле
        if (snake_cord_player_1[0] < 0 or snake_cord_player_1[0] > window_size[0] - 10) or (snake_cord_player_1[1] < 0 or snake_cord_player_1[1] > window_size[1] - 10):
            game_over()
        if (snake_cord_player_2[0] < 0 or snake_cord_player_2[0] > window_size[0] - 10) or (snake_cord_player_2[1] < 0 or snake_cord_player_2[1] > window_size[1] - 10):
            game_over()

        #Если игрок заденет другого игрока
        for block in snake_body_player_1:
            if snake_cord_player_2[0] == block[0] and snake_cord_player_2[1] == block[1]:
                game_over()

        #Если игрок заденет свое тело
        for block in snake_body_player_1[1:]:
            if snake_cord_player_1[0] == block[0] and snake_cord_player_1[1] == block[1]:
                game_over()
        for block in snake_body_player_2[1:]:
            if snake_cord_player_2[0] == block[0] and snake_cord_player_2[1] == block[1]:
                game_over()

        #Отрисовка еда
        pygame.draw.rect(window, red_color, pygame.Rect(food_cord[0], food_cord[1], 10, 10))

        show_score()

        pygame.display.update()

        speed.tick(20)
