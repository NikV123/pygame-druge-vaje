import random
import pygame

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Space Invaders")

raketa = pygame.image.load("rocket.png").convert_alpha()
raketa = pygame.transform.scale(raketa, (30, 60))
sr1 = pygame.image.load("enemy_rocket.png").convert_alpha()
sr1 = pygame.transform.scale(sr1, (50, 50))
sr2 = pygame.image.load("enemy_rocket2.png").convert_alpha()
sr2 = pygame.transform.scale(sr2, (50, 50))

raketa_x = 500 - 15
raketa_y = 800 - 60
sr1_x = 200
sr1_y = 0
sr1_speed = 3
sr2_x = 300
sr2_y = 0
sr2_speed = 2
bullet_x = -1
bullet_y = -1
bullet_speed = 8
score = 0

font = pygame.font.Font(None, 36)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if bullet_y < 0:
                bullet_x = mouse_pos[0] + 15
                bullet_y = raketa_y

    sr1_y += sr1_speed
    sr2_y += sr2_speed
    bullet_y += -bullet_speed
    mouse_position = pygame.mouse.get_pos()

    raketa_re = pygame.Rect(mouse_position[0], raketa_y, 30, 50)
    sr1_re = pygame.Rect(sr1_x, sr1_y, 50, 50)
    sr2_re = pygame.Rect(sr2_x, sr2_y, 50, 50)
    if raketa_re.colliderect(sr1_re) or raketa_re.colliderect(sr2_re):
        pygame.quit()
        exit()

    if bullet_x >= sr1_x and bullet_x <= sr1_x + 50:
        if bullet_y >= sr1_y and bullet_y <= sr1_y + 50:
            bullet_x = -1
            bullet_y = -1
            sr1_y = -60
            sr1_x = random.randint(30, 900 - 60)
            sr1_speed = random.randint(2, 8)
            score += 1

    if bullet_x >= sr2_x and bullet_x <= sr2_x + 50:
        if bullet_y >= sr2_y and bullet_y <= sr2_y + 50:
            bullet_x = -1
            bullet_y = -1
            sr2_y = -60
            sr2_x = random.randint(30, 900 - 60)
            sr2_speed = random.randint(2, 8)
            score += 1

    if sr1_y > 800:
        sr1_y = -60
        sr1_x = random.randint(30, 900 - 60)
        sr1_speed = random.randint(1, 8)

    if sr2_y > 800:
        sr2_y = -60
        sr2_x = random.randint(30, 900 - 60)
        sr2_speed = random.randint(1, 8)

    screen.fill("black")
    screen.blit(raketa, (mouse_position[0], raketa_y))
    screen.blit(sr1, (sr1_x, sr1_y))
    screen.blit(sr2, (sr2_x, sr2_y))
    pygame.draw.circle(screen, "red", (bullet_x, bullet_y), 3)

    score_text = font.render("Score: " + str(score), True, ("White"))
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(60)
