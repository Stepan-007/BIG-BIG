import os
import pygame
import requests

spn = [40.9, 25.9]
map_server = "http://static-maps.yandex.ru/1.x/"
map_params = {'ll': '135.125529,-27.306904',
              'spn': '40.9,25.9',
              'l': 'sat'}
response = requests.get(map_server, map_params)

map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)

pygame.init()
screen = pygame.display.set_mode((600, 450))
screen.blit(pygame.image.load(map_file), (0, 0))
pygame.display.flip()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.K_PAGEUP:
            if spn[0] < 80 or spn[1] < 80:
                spn = [i + 10 for i in spn]
            map_server = "http://static-maps.yandex.ru/1.x/"
            map_params = {'ll': '135.125529,-27.306904',
                          'spn': f"{spn[0]},{spn[1]}",
                          'l': 'sat'}
            response = requests.get(map_server, map_params)
            map_file = "map.png"
            with open(map_file, "wb") as file:
                file.write(response.content)
            screen.blit(pygame.image.load(map_file), (0, 0))
            pygame.display.flip()
        if event.type == pygame.K_PAGEDOWN:
            if spn[0] > 30 or spn[1] > 30:
                spn = [i - 10 for i in spn]
            map_server = "http://static-maps.yandex.ru/1.x/"
            map_params = {'ll': '135.125529,-27.306904',
                          'spn': f"{spn[0]},{spn[1]}",
                          'l': 'sat'}

            response = requests.get(map_server, map_params)
            map_file = "map.png"
            with open(map_file, "wb") as file:
                file.write(response.content)
            screen.blit(pygame.image.load(map_file), (0, 0))
            pygame.display.flip()
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()