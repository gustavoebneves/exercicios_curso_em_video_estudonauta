import pygame

pygame.init()
pygame.mixer.music.load('ex024.mp3')
pygame.mixer.music.play()
pygame.event.wait()
input()
