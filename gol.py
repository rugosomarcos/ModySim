import pygame
import numpy as np
import time

pygame.init()
#Tamaño de la ventana
width, height = 1000, 1000

screen = pygame.display.set_mode((height, width))

bg= 25,25,25
screen.fill(bg)
numcellx,numcelly = 25,25

dimCWidth = width / numcellx
dimCHeight = height / numcelly

#Estado de las celdas, vivas o muertas
gameState = np.zeros((numcellx, numcelly))

#Inicialización uno abajo de otro
gameState[3, 4] = 1
gameState[3, 5] = 1
gameState[3, 6] = 1
gameState[10, 11] = 1
gameState[10, 12] = 1
gameState[10, 13] = 1

#Bucle para mantener la pantalla del juego
while True:

    nuevoEstadoJuego = np.copy(gameState)

    screen.fill(bg)
    time.sleep(0.3)
    for y in range(0, numcellx):
        for x in range(0, numcelly):

            #Calculamos el numero de vecinos cercanos

            n_neigh = gameState[ (x - 1) % numcellx, (y - 1) % numcelly] + \
                      gameState[(x) % numcellx, (y - 1)      % numcelly] + \
                      gameState[(x + 1) % numcellx, (y - 1)  % numcelly] + \
                      gameState[(x - 1) % numcellx, (y)      % numcelly] + \
                      gameState[(x + 1) % numcellx, (y)      % numcelly] + \
                      gameState[(x - 1) % numcellx, (y + 1)  % numcelly] + \
                      gameState[(x) % numcellx, (y + 1)      % numcelly] + \
                      gameState[(x + 1) % numcellx, (y + 1)  % numcelly]                        \

            #Condicion 1 : Una celula muerta con exactamente 3 vecinas,revive
            if gameState[x, y] == 0 and n_neigh == 3:
                nuevoEstadoJuego[x, y] = 1

            #Condicion 2 : Una celula viva con menos de 2 o mas de 3 vecinas vivas se muere
            elif gameState[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                nuevoEstadoJuego[x, y] = 0

            #Crear poligono de cada celda

            poly = [((x)* dimCWidth, y * dimCHeight),
            ((x + 1) * dimCWidth, y * dimCHeight),
            ((x+1) * dimCWidth, (y + 1) * dimCHeight),
            ((x) * dimCWidth, (y + 1) * dimCHeight)]

            if nuevoEstadoJuego[x, y] == 0:
                pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
            else:
                 pygame.draw.polygon(screen, (255, 255, 255), poly, 0)

    #Nuevo estado del juego

    gameState = np.copy(nuevoEstadoJuego)
    pygame.display.flip()



