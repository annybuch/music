## Python basic: Como colocar um arquivo de música mp3 para tocar no python
> coloque o seu arquivo mp3 no mesmo local do seu arquivo .py
> 
> Importe o pygame:

import pygame

>inicializar os comandos do mixer:
>
pygame.mixer.init()  

>inicializar todos os comandos do pygame:
>
pygame.init()   

>Carregar um arquivo de música mp3:
>
pygame.mixer.music.load('justin.mp3')  

>Inicializar a reprodução música:
>
pygame.mixer_music.play()   

>esperar por um unico evento da fila acabar (a música), para encerrar a reprodução:
>
pygame.event.wait()
