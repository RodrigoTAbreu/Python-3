import pygame
print('='*25)
print('Reproduzindo musica')
print('='*25)
pygame.init()
pygame.mixer_music.load('sonic.ogg')
#pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()