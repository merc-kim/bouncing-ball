import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Bouncing Ball")
clock = pygame.time.Clock()

ball_x = 400
ball_y = 300
ball_radius = 20
ball_color = (255, 200, 50)
speed_x = 7
speed_y = 2

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((20,20,30))

    ball_x = ball_x + speed_x
    ball_y = ball_y + speed_y

    if ball_x + ball_radius >= 800 or ball_x - ball_radius <= 0:
        speed_x = -speed_x
        ball_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    if ball_y + ball_radius >= 600 or ball_y - ball_radius <=0:
        speed_y = -speed_y
        ball_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()