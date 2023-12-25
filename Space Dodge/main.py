import pygame
import random
import time


# setting up the window
WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")

# player constants
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_VEL = 5

# obstacle constants
STAR_WIDTH = 10
STAR_HEIGHT = 20
STAR_VEL = 3

# background
BG = pygame.transform.scale(pygame.image.load("Space Dodge/space.jpeg"), (WIDTH, HEIGHT))

# font setup
pygame.font.init()
FONT = pygame.font.SysFont("comicsans", 30)


# function to draw things
def draw(player, elapsed_time, stars):
    WIN.blit(BG, (0, 0))

    pygame.draw.rect(WIN, "red", player)

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))

    for star in stars:
        pygame.draw.rect(WIN, "white", star)

    pygame.display.update()


# main function
def main():
    run = True

    # setting up the player
    player = pygame.Rect((WIDTH+PLAYER_WIDTH)/2,
                         HEIGHT - PLAYER_HEIGHT - 10,
                         PLAYER_WIDTH,
                         PLAYER_HEIGHT)

    # setting 60FPS 
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    # obstacle stuff
    star_increment = 2000
    star_count = 0
    stars = []
    hit = False

    # main loop
    while run:
        # tracking the obstacles
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        # determining the number of obstacles
        if star_count > star_increment:
            for i in range(3):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x,
                                   -STAR_HEIGHT,
                                   STAR_WIDTH,
                                   STAR_HEIGHT)
                stars.append(star)

            # setting the time difference between obstacle spawns
            star_increment = max(200, star_increment-50)
            star_count = 0

        # if player closes the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        # key presses
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL > 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + PLAYER_WIDTH < WIDTH:
            player.x += PLAYER_VEL

        # moving obstacles
        for star in stars:
            star.y += STAR_VEL
            # checking for obstacle reaching end of screen
            if star.y >= HEIGHT:
                stars.remove(star)
            # checking for end of game if player collides with obstacle
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break

        # displaying text for end of game
        if hit:
            lost_text = FONT.render("YOU LOST", 1, "white")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2,
                                 HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break

        # updating screen
        draw(player, elapsed_time, stars)

    pygame.quit()


if __name__ == "__main__":
    main()
