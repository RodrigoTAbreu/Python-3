import pygame
print('='*25)
print('Reproduzindo musica')
print('='*25)
pygame.init()
pygame.mixer.music.load('sonic.ogg')
pygame.mixer.music.play()
pygame.event.wait()
