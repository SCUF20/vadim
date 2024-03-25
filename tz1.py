import pygame


pygame.init()


screen = pygame.display.set_mode((600, 800))
pygame.display.set_caption("plat")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

player_x = 50
player_y = 450
player_width = 40
player_height = 60
player_vel = 5


gravity = 0.5
fall_speed = 0


is_jump = False
jump_count = 10


gravity = 10
fall_speed = 3






running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_vel
    if keys[pygame.K_RIGHT] and player_x < 600 - player_width:
        player_x += player_vel
    if player_y + player_height < 500:
        player_y += fall_speed
        fall_speed += gravity

    if not is_jump:
        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            player_y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 10




    pygame.draw.rect(screen, WHITE, (player_x, player_y, player_width, player_height))


    pygame.display.update()


pygame.quit()
