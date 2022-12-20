# This is a 'beginner' project with a lot of room for growth. I'm curious where I can go with it.
# imports
import pygame
import random
import math
import time

# constant vars in all caps. im not going to change the FPS because I'm not developing a nice GUI
FPS = 90
HEIGHT = 1000
WIDTH = 2000
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
CLICK_CAP = 15

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (200, 175, 75)
PINK = (200, 100, 100)
YELLOW = (100, 100, 0)

# Target
RADIUS_OUTER = 40
RADIUS_MID = 25
RADIUS_INNER = 10

# Scoreboard - apparently need the .init for the text manipulation only
SCOREBOARD_HEIGHT = 50
SCOREBOARD = pygame.Rect(0, 0, WIDTH, SCOREBOARD_HEIGHT)
pygame.init()
FONT1 = pygame.font.SysFont('arial', 32, True, False)


def display(target_pos, clicks, inner_score, mid_score, outer_score, timer):
    # fill the background and title first, then other drawn code overtop
    WINDOW.fill(BLACK)
    pygame.display.set_caption('Coding without a tutorial or guide!')

    # target drawing code. All circles are full but this shouldn't matter due to overlaps. OL might be handy if lazy
    outer_circle = pygame.draw.circle(WINDOW, WHITE, target_pos, RADIUS_OUTER)
    mid_circle = pygame.draw.circle(WINDOW, ORANGE, target_pos, RADIUS_MID)
    inner_circle = pygame.draw.circle(WINDOW, PINK, target_pos, RADIUS_INNER)

    # Scoreboard code drawn overtop
    pygame.draw.rect(WINDOW, YELLOW, SCOREBOARD)

    # Clicks counted
    click_img = FONT1.render('You have clicked x' + str(clicks), True, BLACK)
    WINDOW.blit(click_img, (10, 10))

    #Outer circle score
    out_score_img = FONT1.render('Outer ring clicked x' + str(outer_score), False, WHITE)
    WINDOW.blit(out_score_img, (350, 10))

    #Mid circle score
    mid_score_img = FONT1.render('Middle ring clicked x' + str(mid_score), False, ORANGE)
    WINDOW.blit(mid_score_img, (650, 10))

    #Inner circle score
    inner_score_img = FONT1.render('Inner ring clicked x' + str(inner_score), False, PINK)
    WINDOW.blit(inner_score_img, (1000, 10))

    #Timer
    timer_img = FONT1.render('Elapsed '+ str(CLICK_CAP) + ' click time is ' + str(round(timer, 2)) + ' seconds', False, BLACK)
    WINDOW.blit(timer_img, (1350, 10))

    # make the window display things
    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()
    target_pos = (WIDTH / 2, HEIGHT / 2)
    inner_score = 0
    mid_score = 0
    outer_score = 0
    clicks = 0
    timer = 0


    while run:
        # need to make it iterable -> get() , such that it will run and keep the window up until it is closed
        clock.tick(FPS)
        # timer
        if clicks > 0 and clicks < CLICK_CAP:
            timer = time.time() - started
        elif clicks == CLICK_CAP:
            timer = timer

        #events like quiting or clicking
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                return

            #now for the clicking
            elif event.type == pygame.MOUSEBUTTONDOWN and clicks < CLICK_CAP:
                click_pos = pygame.mouse.get_pos()

                if math.dist(click_pos, target_pos) <= RADIUS_INNER:
                    inner_score = inner_score + 1
                elif math.dist(click_pos, target_pos) <= RADIUS_MID:
                    mid_score = mid_score + 1
                elif math.dist(click_pos, target_pos) <= RADIUS_OUTER:
                    outer_score = outer_score + 1

                # tracks clicks
                clicks = clicks + 1

                if clicks == 1:
                    started = time.time()

                # Moves target with every click. Offsets due to click range & largest radius & scoreboard zone
                target_pos = (random.randint(RADIUS_OUTER, WIDTH - RADIUS_OUTER),
                              random.randint(RADIUS_OUTER + SCOREBOARD_HEIGHT, HEIGHT - RADIUS_OUTER))


        # include all the main file things here
        display(target_pos, clicks, inner_score, mid_score, outer_score, timer)
    pygame.QUIT


# keeping this towards the bottom so it runs good
if __name__ == '__main__':
    main()