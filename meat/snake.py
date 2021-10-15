import pygame
from pygame.locals import *
import time
import random
import imp
import sys
import subprocess
branch = subprocess.Popen("git branch", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
branch = branch.decode()
branch = branch.split('\n')
ok = False
for b in branch:
    if '* meat' in b:
        ok = True
if not ok:
    print('seems that you aren\'t on a right branch')
    sys.exit(0)

SIZE = 40
BACKGROUND_COLOR = (0, 0, 0)
NOVIDEO = False

class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.x = 120
        self.y = 120

    def draw(self):
        if not NOVIDEO:
            pygame.draw.circle(self.parent_screen, pygame.Color('White'), (self.x+20, self.y+20), 20)

    def move(self):
        self.x = random.randint(1,24)*SIZE
        self.y = random.randint(1,19)*SIZE

class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        #self.image = pygame.image.load("resources/block.jpg").convert()
        self.direction = 'down'
        self.length = 1
        self.x = [40]
        self.y = [40]

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def walk(self):
        # update body
        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        # update head
        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE

        self.draw()

    def draw(self):
        if not NOVIDEO:
            for i in range(self.length):
                pygame.draw.rect(self.parent_screen, pygame.Color('Yellow'), pygame.Rect(self.x[i], self.y[i], SIZE, SIZE))

    def increase_length(self):
        self.length += 1
        self.x.append(-40)
        self.y.append(-40)

class API:
    def __init__(self, snake, apple):
        self.snake = snake
        self.apple = apple
    def get_snake_pos(self):
        return (self.snake.x[0], self.snake.y[0]);
    def get_snake_len(self):
        return self.snake.length
    def get_snake_dir(self):
        return self.snake.direction
    def get_apple_pos(self):
        return (self.apple.x, self.apple.y)

class Game:
    def __init__(self, argv):
        pygame.init()
        if not NOVIDEO:
            pygame.display.set_caption("Codebasics Snake And Apple Game")
            self.surface = pygame.display.set_mode((1000, 800))
        else:
            self.surface = None
        self.snake = Snake(self.surface)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()
        self.clock = pygame.time.Clock()
        self.Human_control = True
        if 'snake_hacker' in argv:
            try:
                loadtmp = imp.load_source('', f'./snake_hacker.py')
                self.player_ai = loadtmp.TeamAI(API(self.snake, self.apple))
                self.Human_control = False
            except:
                print(f'snake_hacker.py cannot load')
                raise f'snake_hacker.py cannot load'
        print('Human_control',self.Human_control)


    def reset(self):
        self.snake = Snake(self.surface)
        self.apple = Apple(self.surface)


    def is_collision(self, x1, y1, x2, y2):
        if abs(x1-x2)<SIZE and abs(y1-y2)<SIZE:
            return True
        return False

    def render_background(self):
        if NOVIDEO:
            return
        pygame.draw.rect(self.surface, pygame.Color('Black'), pygame.Rect(0, 0, 1000, 800))
        
        
    def play(self):
        self.render_background()
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        if not NOVIDEO:
            pygame.display.flip()

        # snake eating apple scenario
        for i in range(self.snake.length):
            if self.is_collision(self.snake.x[i], self.snake.y[i], self.apple.x, self.apple.y):
                self.snake.increase_length()
                self.apple.move()

        # snake colliding with itself
        for i in range(3, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                raise "Collision Occurred"

        # snake colliding with the boundries of the window
        if self.snake.x[0]-SIZE<0 or self.snake.x[0]+SIZE > 1000 or self.snake.y[0]-SIZE<0 or self.snake.y[0]+SIZE > 800:
            raise "Hit the boundry error"

    def display_score(self):
        if not NOVIDEO:
            font = pygame.font.SysFont('arial',30)
            score = font.render(f"Score: {self.snake.length}",True,(200,200,200))
            self.surface.blit(score,(850,10))

    def show_game_over(self):
        self.render_background()
        if not NOVIDEO:
            font = pygame.font.SysFont('arial', 30)
            line1 = font.render(f"Game is over! Your score is {self.snake.length}", True, (255, 255, 255))
            print(f"Game is over! Your score is {self.snake.length}")
            if self.snake.length >= 20:
                f = open('fat_snake', 'w')
                f.write('W0w_7He_Py+h0n_1$_$trooooonG!')
                f.close()
            self.surface.blit(line1, (200, 300))
            line2 = font.render("To play again press Enter. To exit press Escape!", True, (255, 255, 255))
            print("To play again press Enter. To exit press Escape!")
            self.surface.blit(line2, (200, 350))
            pygame.display.flip()
        print(f"Game is over! Your score is {self.snake.length}")
        if self.snake.length >= 20:
            f = open('fat_snake', 'w')
            f.write('W0w_7He_Py+h0n_1$_$trooooonG!')
            f.close()

    def run(self):
        running = True
        pause = False
        if self.Human_control:
            while running:
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            running = False
                            pygame.display.quit()
                            pygame.quit()

                        if event.key == K_RETURN:
                            pause = False

                        if not pause:
                            if event.key == K_LEFT and self.snake.direction!='right':
                                self.snake.move_left()

                            if event.key == K_RIGHT and self.snake.direction!='left':
                                self.snake.move_right()

                            if event.key == K_UP and self.snake.direction!='down':
                                self.snake.move_up()

                            if event.key == K_DOWN and self.snake.direction!='up':
                                self.snake.move_down()

                    elif event.type == QUIT:
                        running = False
                        pygame.display.quit()
                        pygame.quit()
                try:

                    if not pause:
                        self.play()

                except Exception as e:
                    #print(e)
                    self.show_game_over()
                    pause = True
                    self.reset()

                self.clock.tick(30)
        else:
            while running:
                movement = self.player_ai.decide()
                #print(movement)
                if movement == 'esc':
                    running = False
                    if not NOVIDEO:
                        pygame.display.quit()
                    pygame.quit()

                if movement == 'return':
                    pause = False

                if not pause:
                    if movement == 'left' and self.snake.direction!='right':
                        self.snake.move_left()

                    if movement == 'right' and self.snake.direction!='left':
                        self.snake.move_right()

                    if movement == 'up' and self.snake.direction!='down':
                        self.snake.move_up()

                    if movement == 'down' and self.snake.direction!='up':
                        self.snake.move_down()

                try:
                    if not pause:
                        self.play()

                except Exception as e:
                    self.show_game_over()
                    running = False
                    self.reset()

                self.clock.tick(30)
            else:
                if not NOVIDEO:
                    pygame.display.quit()
                pygame.quit()

if __name__ == '__main__':
    if '-n' in sys.argv:
        NOVIDEO = True
    game = Game(sys.argv)
    game.run()
