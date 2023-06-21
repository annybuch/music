# Como colocar um arquivo de música mp3 no python:
import pygame
pygame.mixer.init()  # inicializar os comandos do mixer.
pygame.init()   # inicializar todos os comandos do pygame.
pygame.mixer.music.load('justin.mp3')   # Carregar um arquivo de música mp3.
pygame.mixer_music.play()    # Inicializar a reprodução música
pygame.event.wait()  # esperar por um unico evendo (a musica) da fila, para encerrar a reprodução.