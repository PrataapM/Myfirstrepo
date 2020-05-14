import pygame
import random

x=pygame.init()

global Speed
game_music = pygame.mixer.music.load("game_music.mp3")
background_img = pygame.image.load("background_img2.png")
#appleimg = pygame.image.load("apple.jpg")
game_sound = pygame.mixer.Sound("game_sound.wav")
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
blue=(0,0,255)
screen_width = 1000
screen_height = 650
gameWindow=pygame.display.set_mode((screen_width,screen_height))
setCaption="Snake game"
pygame.display.set_caption(setCaption)
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None,25)


def text_screen(text,color,x,y):
    screen_text = font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])
    pass


def plot_snake(gameWindow,black1,snk_list, snake_size1):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow,black1,[x,y,snake_size1,snake_size1])


def gameloop():
    Game_exit = False
    Game_over = False
    pygame.mixer.music.play(-1)
    Speed = 5
    score = 0
    snake_x = 55
    snake_y = 45
    snake_size = 10
    food_size = 20
    velocity_x = 0
    velocity_y = 0
    fps = 30
    food_x = random.randint(0, screen_width)
    food_y = random.randint(0, screen_height)
    snake_length = 1
    snk_list = []
    with open("highscore_pygame.txt", "r") as f:
        highscore = f.read()

    while not Game_exit:
        if Game_over:
            gameWindow.fill(white)
            gameWindow.blit(background_img, [0, 0])
            with open("highscore_pygame.txt", "w") as f:
                f.write(str(highscore))
            gameWindow.fill(white)
            gameWindow.blit(background_img, [0, 0])
            text_screen("GAME OVER PLEASE ENTER TO CONTINUE",red,50,100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Game_exit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Game_exit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        print("You have pressed Right Key")
                        velocity_x = Speed
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        print("You have presses Left Key")
                        velocity_x = -Speed
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        print("You have pressed Up Key")
                        velocity_x = 0
                        velocity_y = -Speed
                    if event.key == pygame.K_DOWN:
                        print("You have pressed Down Key")
                        velocity_x = 0
                        velocity_y = Speed
            snake_x += velocity_x
            snake_y += velocity_y
            if abs(food_x - snake_x) < 10 and abs(food_y - snake_y) < 10:
                pygame.mixer.Sound.play(game_sound)
                score += 5
                food_x = random.randint(0, screen_width/2)
                food_y = random.randint(0, screen_height/2)
                snake_length += 5
                if score > int(highscore):
                    highscore = score
            gameWindow.fill(white)
            gameWindow.blit(background_img, [0, 0])
            text_screen("Score: " + str(score) + "  High Score:" + str(highscore), blue, 5, 5)
            pygame.draw.rect(gameWindow,black, [snake_x, snake_y, snake_size, snake_size])
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
            #gameWindow.blit(appleimg, [food_x, food_y])
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            print(snk_list)
            if len(snk_list) > snake_length:
                del snk_list[0]
            if head in snk_list[ :-1]:
                # pygame.mixer.music.stop()
                # game_over = pygame.mixer.Sound("Fail-sound-effect.mp3")
                # pygame.mixer.Sound.play(game_over)
                Game_over = True
            if (snake_x < 0) or (snake_y < 0) or (snake_x > screen_width) or (snake_y > screen_height):
                # pygame.mixer.music.stop()
                # game_over = pygame.mixer.Sound("Fail-sound-effect.mp3")
                # pygame.mixer.Sound.play(game_over)
                Game_over = True
            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
gameloop()

