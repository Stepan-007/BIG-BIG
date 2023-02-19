import os
import pygame
import requests

map_server = "http://static-maps.yandex.ru/1.x/"
map_params = {'ll': '135.125529,-27.306904',
              'spn': '40.9,25.9',
              'l': 'sat'}
response = requests.get(map_server, map_params)

if not response:
    pass

map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)

pygame.init()
screen = pygame.display.set_mode((600, 450))
screen.blit(pygame.image.load(map_file), (0, 0))
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()

os.remove(map_file)
