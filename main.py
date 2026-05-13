from math import hypot
from random import randint
import pygame
pygame.init()



window = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

my_player = [0, 0, 20]
class Food:
    def __init__(self, color, x, y, radius):
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius
    def check_collision(self, player_x, player_y, player_radius):
        dx = player_x - self.x
        dy = player_y - self.y
        return hypot(dx, dy) < self.radius + player_radius

foods = []
for i in range(150):
    foods.append(
        Food((randint(0, 255), randint(0, 255), randint(0, 255)),
             randint(0, 600),
             randint(0, 600),
             5))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


    window.fill((123, 123, 123))
    scale = max(0.3, min(50/my_player[2], 1.5))
    pygame.draw.circle(window, (0, 255, 0), (300, 300), my_player[2]*scale)
    for food in foods[:]:
        if food.check_collision(my_player[0], my_player[1], my_player[2]):
            my_player[2] += int(food.radius* 0.2)
            foods.remove(food)
        else:
            sx = int((food.x - my_player[0])*scale  +300)
            sy = int((food.y - my_player[1]) * scale + 300)
            pygame.draw.circle(window, food.color, (sx, sy), int(food.radius*scale))

    pygame.display.flip()
    clock.tick(60)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        my_player[1] -= 10
    if keys[pygame.K_d]:
        my_player[0] += 10