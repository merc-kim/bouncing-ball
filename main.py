import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Bouncing Ball")
clock = pygame.time.Clock()

ball_x = 400
ball_y = 300
ball_radius = 20
speed_x = 4

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((20,20,30))

    ball_x = ball_x + speed_x
    pygame.draw.circle(screen, (255, 200, 50), (ball_x, ball_y), ball_radius)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()