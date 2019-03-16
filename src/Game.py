import pygame

from src.Config import Config
from src.Snake import Snake
from src.Apple import Apple


class Game:
    def __init__(self, display):
        self.display = display
        self.score = 0

    def loop(self):
        # This is class that will help us to track amount of time or to manage framerate.
        clock = pygame.time.Clock()

        # Fonts.
        pygame.font.init()
        font = pygame.font.Font('./assets/Now-Regular.otf', 28)

        # Game name.
        title = font.render('Anaconda', True, Config['colors']['white'])
        # Gives the bounding box size around text.
        title_rect = title.get_rect(
            center=(
                Config['game']['width'] / 2,
                Config['game']['bumper_size'] / 2
            )
        )

        # Our snake.
        snake = Snake(self.display)
        dx = 0
        dy = 0
        self.score = 0

        # Apples.
        apple = Apple(self.display)

        while True:
            # This empties the event queue. Gives us our user input events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                # Checks if the key is one of any of the four potential keys.
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        dx = -Config['snake']['speed']
                        dy = 0
                    elif event.key == pygame.K_RIGHT:
                        dx = Config['snake']['speed']
                        dy = 0
                    elif event.key == pygame.K_UP:
                        dx = 0
                        dy = -Config['snake']['speed']
                    elif event.key == pygame.K_DOWN:
                        dx = 0
                        dy = Config['snake']['speed']

                print(event)

            # Fills the entire screen with the green color and than places black "background".
            self.display.fill(Config['colors']['green'])

            pygame.draw.rect(
                self.display,
                Config['colors']['black'],
                [
                    Config['game']['bumper_size'],
                    Config['game']['bumper_size'],
                    Config['game']['height'] - Config['game']['bumper_size'] * 2,
                    Config['game']['width'] - Config['game']['bumper_size'] * 2
                ]
            )

            # Moves our snake.
            snake.move(dx, dy)
            snake_rect = snake.draw()
            apple_rect = apple.draw()

            # Collisions with the wall.
            bumper_x = Config['game']['width'] - Config['game']['bumper_size']
            bumper_y = Config['game']['height'] - Config['game']['bumper_size']

            if (
                snake.x_pos < Config['game']['bumper_size'] or
                snake.y_pos < Config['game']['bumper_size'] or
                snake.x_pos + Config['snake']['width'] > bumper_x or
                snake.y_pos + Config['snake']['height'] > bumper_y
            ):
                self.loop()

            # Checks collisions with apple.
            if apple_rect.colliderect(snake_rect):
                apple.randomize()
                self.score += 1
                snake.eat()

            # Checks collisions with itself.
            if len(snake.body) > 1:
                for cell in snake.body:
                    if snake.x_pos == cell[0] and snake.y_pos == cell[1]:
                        self.loop()

            # Adds score.
            score_text = 'Score: {}'.format(self.score)
            score = font.render(score_text, True, Config['colors']['white'])

            score_rect = score.get_rect(
                center=(
                    Config['game']['width'] / 2,
                    Config['game']['height'] - Config['game']['bumper_size'] / 2
                )
            )

            self.display.blit(score, score_rect)
            self.display.blit(title, title_rect)

            pygame.display.update()

            # Tracks how many frames we have rendered. Uses pygame.time.delay, so it's very precise
            clock.tick_busy_loop(Config['game']['fps'])
