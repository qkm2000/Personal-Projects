import pygame
import random


# setting up window
WIDTH = 600
HEIGHT = 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")


# player constants
PLAYER_RADIUS = 20
PLAYER_VEL = 5

# table constants
TABLE_WIDTH = 300
TABLE_HEIGHT = 540

# net constants
NET_WIDTH = 350
NET_HEIGHT = 4


# circle item class
class circle:
    def __init__(self, radius, x, y):
        self.radius = radius
        self.x = x
        self.y = y


# function to update screen
def draw(player1, player2, table, net, ball):
    WIN.fill((0, 0, 0))
    pygame.draw.rect(WIN, "blue", table)
    pygame.draw.rect(WIN, "red", net)
    pygame.draw.circle(WIN, "white", (ball.x, ball.y), ball.radius)
    pygame.draw.circle(WIN, "gray", (player1.x, player1.y), player1.radius)
    pygame.draw.circle(WIN, "gray", (player2.x, player2.y), player2.radius)
    pygame.display.update()


# setting up the game board
def set_up():
    # player 1 is the top player
    player1 = circle(radius=PLAYER_RADIUS, x=WIDTH/2, y=40)

    # player 2 is the bottom player
    player2 = circle(radius=PLAYER_RADIUS, x=WIDTH/2, y=HEIGHT-40)

    # table
    table = pygame.Rect((WIDTH-TABLE_WIDTH)/2,
                        (HEIGHT-TABLE_HEIGHT)/2,
                        TABLE_WIDTH,
                        TABLE_HEIGHT)

    # net
    net = pygame.Rect((WIDTH-NET_WIDTH)/2,
                      (HEIGHT-NET_HEIGHT)/2,
                      NET_WIDTH,
                      NET_HEIGHT)

    # ball
    top = random.choice([True, False])
    if top:
        ball = circle(radius=10, x=WIDTH/2, y=200)
    else:
        ball = circle(radius=10, x=WIDTH/2, y=600)

    return player1, player2, table, net, ball


# movement stuff
def movement(keys, player1, player2):
    # player 1 movement
    if keys[pygame.K_LEFT] and player1.x-PLAYER_RADIUS-PLAYER_VEL>=0:
        player1.x -= PLAYER_VEL
    if keys[pygame.K_RIGHT] and player1.x+PLAYER_RADIUS+PLAYER_VEL<=WIDTH:
        player1.x += PLAYER_VEL
    if keys[pygame.K_UP] and player1.y-PLAYER_RADIUS-PLAYER_VEL>=0:
        player1.y -= PLAYER_VEL
    if keys[pygame.K_DOWN] and player1.y+PLAYER_RADIUS+PLAYER_VEL<=(HEIGHT-NET_HEIGHT)//2:
        player1.y += PLAYER_VEL

    # player 2 movement
    if keys[pygame.K_a] and player2.x-PLAYER_RADIUS-PLAYER_VEL>=0:
        player2.x -= PLAYER_VEL
    if keys[pygame.K_d] and player2.x+PLAYER_RADIUS+PLAYER_VEL<=WIDTH:
        player2.x += PLAYER_VEL
    if keys[pygame.K_w] and player2.y-PLAYER_RADIUS-PLAYER_VEL>=(HEIGHT-NET_HEIGHT)//2:
        player2.y -= PLAYER_VEL
    if keys[pygame.K_s] and player2.y+PLAYER_RADIUS+PLAYER_VEL<=HEIGHT:
        player2.y += PLAYER_VEL

    return player1, player2


def main():
    run = True

    # set up player
    player1, player2, table, net, ball = set_up()

    # setting 60fps
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        player1, player2 = movement(keys, player1,)

        draw(player1, player2, table, net, ball)

    pygame.quit()


if __name__ == "__main__":
    main()
