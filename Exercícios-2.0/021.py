import pygame
print('='*25)
print('Reproduzindo musica')
print('='*25)
pygame.init()
pygame.mixer.music.load('sonic.mp3')
pygame.mixer.music.play()
pygame.event.wait()
