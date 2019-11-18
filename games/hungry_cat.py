import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)

mouse_width = 80
cat_width = 140
cat_height = 160

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Hungry Cats')
clock = pygame.time.Clock()

mouseImg = pygame.transform.scale(pygame.image.load(
    "mouse.png"), (mouse_width, mouse_width))
catImg = pygame.transform.scale(pygame.image.load(
    "cat.png"), (cat_width, cat_height))


def cats_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render(f"Poäng:    {str(count)}", True, black)
    gameDisplay.blit(text, (10, 10))


def cats(cat_x, cat_y):
    gameDisplay.blit(catImg, (cat_x, cat_y))


def mouse(mouse_x, mouse_y):
    gameDisplay.blit(mouseImg, (mouse_x, mouse_y))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()


def crash():
    message_display('R.I.P.')


def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    cat_start_x = random.randrange(0, display_width - cat_width)
    cat_start_y = -600
    cat_speed = 4

    thingCount = 1

    dodged = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        gameDisplay.fill(white)

        cats(cat_start_x, cat_start_y)

        cat_start_y += cat_speed
        mouse(x, y)
        cats_dodged(dodged)

        if x > display_width - mouse_width or x < 0:
            crash()

        if cat_start_y > display_height:
            cat_start_y = 0 - cat_height
            cat_start_x = random.randrange(0, display_width)
            dodged += 1
            cat_speed += 1

        if y < cat_start_y + cat_height:
            if x > cat_start_x and x < cat_start_x + cat_width or x + mouse_width > cat_start_x and x + mouse_width < cat_start_x + cat_width:
                crash()

        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()
