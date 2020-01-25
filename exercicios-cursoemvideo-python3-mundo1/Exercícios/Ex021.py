'''Enunciado: Faça um programa em Python que abra e reproduza o aúdio de um arquivo MP3.'''

import pygame

pygame.init()
pygame.mixer.music.load('Ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
