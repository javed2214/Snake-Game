# Snake Game using Python

import pygame
import random
import os

pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

highscore = 0

# Screen Width and Height
screen_width = 800
screen_height = 500

font = pygame.font.SysFont(None, 45)

# Creating Window
gameWindow = pygame.display.set_mode((screen_width, screen_height))


# Game Title
pygame.display.set_caption("Snake Game")
pygame.display.update()

clock = pygame.time.Clock() 

def text_screen(text, color, x, y):
	screen_text = font.render(text, True, color)
	gameWindow.blit(screen_text, [x,y])


def plot_snake(gameWindow, color, snk_list, snake_size):
	for x,y in snk_list:
		pygame.draw.rect(gameWindow, black, [x, y, snake_size, snake_size]) 


def welcome():
	
	exit_game = False
	
	while not exit_game:
		
		# gameWindow.fill((233,190,187))
		
		bg = pygame.image.load("bg.jpg")
		gameWindow.blit(bg, (0, 0))

		text_screen("Welcome to Snake Game!!!", black, 152, 15)
		text_screen("Press Space Bar to Play", red, 182, 65)
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit_game = True

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					game_loop()

		pygame.display.update()
		clock.tick(30)

# Creating a Game Loop

def game_loop():

	# Game Specific Variables
	exit_game = False
	game_over = False
	snake_x = 45
	snake_y = 55
	velocity_x = 0
	velocity_y = 0
	snake_size = 13
	fps = 30
	init_velocity = 5

	food_x = random.randint(50, screen_width / 2)
	food_y = random.randint(50, screen_height / 2)
	score = 0

	snk_list = []
	snk_length = 1

	if(not os.path.exists("HighScore.txt")):
		with open("HighScore.txt", "w") as f:
			f.write("0")

	with open("HighScore.txt", "r") as f:
			highscore = f.read()

	while not exit_game:

		if game_over:

			with open("HighScore.txt", "w") as f:
				f.write(str(highscore))
			
			gameWindow.fill(white)
			text_screen("Game Over!!! Press Enter to Continue", red, 60, 200)
		
			for event in pygame.event.get():
				# print(event)
				if event.type == pygame.QUIT:
					exit_game = True

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN:
						welcome()

		else:

			for event in pygame.event.get():
				# print(event)
				if event.type == pygame.QUIT:
					exit_game = True

				if event.type == pygame.KEYDOWN:
					
					if event.key == pygame.K_RIGHT:
						velocity_x = init_velocity
						velocity_y = 0

					if event.key == pygame.K_LEFT:
						velocity_x = -init_velocity
						velocity_y = 0

					if event.key == pygame.K_UP:
						velocity_y = -init_velocity
						velocity_x = 0

					if event.key == pygame.K_DOWN:
						velocity_y = init_velocity
						velocity_x = 0

					if event.key == pygame.K_q:
						score += 5

			snake_x += velocity_x
			snake_y += velocity_y

			if abs(snake_x - food_x) < 6 and abs(snake_y - food_y) < 6:
				score += 10
				food_x = random.randint(50, screen_width / 2)
				food_y = random.randint(50, screen_height / 2)
				snk_length += 5

				if score > int(highscore):
					highscore = score

					with open("HighScore.txt", "w") as f:
						f.write(str(highscore))


			gameWindow.fill((233, 220, 229))
			text_screen("Score : "+ str(score) + "  High Score : " + str(highscore), red, 5, 5)
			pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
			
			head = []
			head.append(snake_x)
			head.append(snake_y)
			snk_list.append(head)

			if len(snk_list) > snk_length:
				del snk_list[0]

			if head in snk_list[:-1]:
				game_over = True

			if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
				game_over = True

			plot_snake(gameWindow, black, snk_list, snake_size)
		
		pygame.display.update()
		clock.tick(fps)

	# To Quit the Game
	pygame.quit()
	quit()


welcome()