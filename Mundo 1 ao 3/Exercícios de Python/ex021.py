import pygame
pygame.mixer.init()
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play()
print('\033[35mAproveite a música\033[m')
input('Pressione \033[1;97mENTER\033[m para sair...')
