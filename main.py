import pygame
import random as rm
import pygame.mixer

midnight_blue = pygame.Color(25, 25, 112)
mint_cream = pygame.Color(245, 255, 250)
crimson_red = pygame.Color(220, 20, 60)
lawn_green = pygame.Color(124, 252, 0)
orange_red = pygame.Color(255, 69, 0)
black = pygame.Color(0,0,0)

pygame.init()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 420
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
font_path = "Grand9KPixel.ttf"
pygame.display.set_caption('Snake Game')
background_image = pygame.image.load("background.png")
bg = pygame.image.load("background.jpg")
back = pygame.image.load("back.png")
click_sound = pygame.mixer.Sound("click.wav")
eat_sound = pygame.mixer.Sound("eat.wav")
pygame.mixer.music.load("moosic.wav")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)
running = True
position_of_snake = [100, 50]
body_of_snake = [ [100, 50], [90, 50], [80, 50], [70, 50] ]
position_of_fruit = [ rm.randrange(1, (SCREEN_WIDTH//10)) * 10, rm.randrange(1, (SCREEN_HEIGHT//10)) * 10 ]
spawning_of_fruit = True
initial_direction = 'RIGHT'
snake_direction = initial_direction
player_score = 0
speed_of_snake = 15
obstacles = []
spawning_of_obstacles = True

def setdiff():
  while True:
    screen.blit(bg, (0, 0))
    draw_text("Set Difficulty ", 24, mint_cream, SCREEN_WIDTH//2, SCREEN_HEIGHT//4-20)
    draw_text("Enter 1 for Easy", 18, mint_cream, SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
    draw_text("Press 2 for Normal", 18, mint_cream, SCREEN_WIDTH//2, SCREEN_HEIGHT*2//3-30)
    draw_text("Press 3 for Expert", 18, mint_cream, SCREEN_WIDTH//2, SCREEN_HEIGHT*3//4-20)
    pygame.display.update()
    global speed_of_snake
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_1:
          speed_of_snake = 10
          return
        elif event.key == pygame.K_2:
          speed_of_snake = 15
          return
        elif event.key == pygame.K_3:
          speed_of_snake = 45
          return


def display_home_screen():
  click_sound.play()
  while True:
    screen.blit(background_image, (0, 0))
    draw_text("Press SPACE to Start", 18, mint_cream, SCREEN_WIDTH//2, (SCREEN_HEIGHT//2)+30)
    draw_text("Press 1 to Select Difficulty", 18, mint_cream, SCREEN_WIDTH//2, (SCREEN_HEIGHT*2//3))
    draw_text("Press ESC to Quit", 18, mint_cream, SCREEN_WIDTH//2, (SCREEN_HEIGHT*3//4)+5)
    pygame.display.update()
    reset_game()
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
          return
        elif event.key == pygame.K_ESCAPE:
          pygame.quit()
          quit()
        elif event.key == pygame.K_1:
          setdiff()
          return

def reset_game():
  global obstacles, spawning_of_obstacles, running, position_of_snake, body_of_snake, position_of_fruit, spawning_of_fruit, initial_direction, snake_direction, player_score, speed_of_snake
  running = True
  position_of_snake = [100, 50]
  body_of_snake = [ [100, 50], [90, 50], [80, 50], [70, 50] ]
  position_of_fruit = [ rm.randrange(1, (SCREEN_WIDTH//10)) * 10, rm.randrange(1, (SCREEN_HEIGHT//10)) * 10 ]
  spawning_of_fruit = True
  initial_direction = 'RIGHT'
  snake_direction = initial_direction
  player_score = 0
  speed_of_snake = 15
  obstacles = []
  spawning_of_obstacles = True
  return

def draw_text(text, size, color, x, y):
  font = pygame.font.Font(font_path, size)
  text_surface = font.render(text, True, color)
  text_rect = text_surface.get_rect()
  text_rect.center = (x, y)
  screen.blit(text_surface, text_rect)

def game_over():
  click_sound.play()
  while True:
    screen.blit(background_image, (0, 0))
    draw_text("Game Over", 32, crimson_red, SCREEN_WIDTH//2, SCREEN_HEIGHT//4)
    draw_text("Your Score: " + str(player_score), 16, mint_cream, SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
    draw_text("Press SPACE to Play Again", 16, mint_cream, SCREEN_WIDTH//2, SCREEN_HEIGHT*3//4)
    draw_text("Press ESC to Go to Home Screen", 16, mint_cream, SCREEN_WIDTH//2, SCREEN_HEIGHT*3//4 + 40)
    pygame.display.update()
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
          reset_game()
          return
        elif event.key == pygame.K_ESCAPE:
          display_home_screen()
          return

def display_score():
    score_font = pygame.font.Font(font_path, 16)
    score_surface = score_font.render('Your Score : ' + str(player_score), True, mint_cream)
    score_rect = score_surface.get_rect()
    score_rect.topleft = (10, 10)
    screen.blit(score_surface, score_rect)

def main_game():
    click_sound.play()
    global position_of_snake, body_of_snake, position_of_fruit, player_score, spawning_of_fruit, snake_direction, initial_direction, obstacles, spawning_of_obstacle
    while running:
      screen.blit(back, (0, 0))
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          quit()
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_w:
            snake_direction = 'UP'
          if event.key == pygame.K_s:
            snake_direction = 'DOWN'
          if event.key == pygame.K_a:
            snake_direction = 'LEFT'
          if event.key == pygame.K_d:
            snake_direction = 'RIGHT'

      if snake_direction == 'UP' and initial_direction != 'DOWN':
        initial_direction = 'UP'
      if snake_direction == 'DOWN' and initial_direction != 'UP':
        initial_direction = 'DOWN'
      if snake_direction == 'LEFT' and initial_direction != 'RIGHT':
        initial_direction = 'LEFT'
      if snake_direction == 'RIGHT' and initial_direction != 'LEFT':
        initial_direction = 'RIGHT'
  
      if position_of_snake[0] == position_of_fruit[0] and position_of_snake[1] == position_of_fruit[1]:
        player_score += 1
        eat_sound.play()
        # Insert new head position when the snake eats a fruit
        body_of_snake.insert(0, list(position_of_snake))
        spawning_of_fruit = False
        position_of_fruit = [rm.randrange(1, (SCREEN_WIDTH // 10)) * 10, rm.randrange(1, (SCREEN_HEIGHT // 10)) * 10]
      else:
        # Remove the last segment of the snake's body if it doesn't eat a fruit
        body_of_snake.pop()

      for obstacle in obstacles:
        if position_of_snake[0] == obstacle[0] and position_of_snake[1] == obstacle[1]:
          game_over()

        # Update snake's position based on direction
      if initial_direction == 'UP':
        position_of_snake[1] -= 10
      if initial_direction == 'DOWN':
        position_of_snake[1] += 10
      if initial_direction == 'LEFT':
        position_of_snake[0] -= 10
      if initial_direction == 'RIGHT':
        position_of_snake[0] += 10

        # Insert new head position
      body_of_snake.insert(0, list(position_of_snake))

        # Check if the snake eats the fruit
      if position_of_snake[0] == position_of_fruit[0] and position_of_snake[1] == position_of_fruit[1]:
        player_score += 1
        spawning_of_fruit = False

        # Check if the snake hits the boundary
      if position_of_snake[0] < 0 or position_of_snake[0] > SCREEN_WIDTH - 10:
        game_over()
      if position_of_snake[1] < 0 or position_of_snake[1] > SCREEN_HEIGHT - 10:
        game_over()

        # Check if the snake hits itself
      for block in body_of_snake[1:]:
        if position_of_snake[0] == block[0] and position_of_snake[1] == block[1]:
          game_over()

        # Update score and display
      display_score()

        # Obstacle spawning logic
      num_obstacles_to_spawn = int(player_score * 1.5)
      if len(obstacles) < num_obstacles_to_spawn:
        obstacle_x = rm.randrange(1, (SCREEN_WIDTH // 10)) * 10
        obstacle_y = rm.randrange(1, (SCREEN_HEIGHT // 10)) * 10
        obstacle_position = [obstacle_x, obstacle_y]
        obstacles.append(obstacle_position)
        spawning_of_obstacle = True

        # Draw obstacles
      for obstacle in obstacles:
        pygame.draw.rect(screen, crimson_red, pygame.Rect(obstacle[0], obstacle[1], 10, 10))

        # Update obstacles spawning status
      spawning_of_obstacle = False

      for position in body_of_snake:
        pygame.draw.rect(screen, lawn_green, pygame.Rect(position[0], position[1], 10, 10))

      # Draw fruits
      pygame.draw.rect(screen, 'purple', pygame.Rect(position_of_fruit[0], position_of_fruit[1], 10, 10))

      # Draw obstacles
      for obstacle in obstacles:
        pygame.draw.rect(screen, 'red', pygame.Rect(obstacle[0], obstacle[1], 10, 10))

      spawning_of_obstacle = False

      pygame.display.update()
      clock.tick(speed_of_snake)


def main():
    click_sound.play()
    while True:
      display_home_screen()
      main_game()

if __name__ == "__main__":
    main()

# known bugs 
# player score updates by 2
# restarting resets difficulty