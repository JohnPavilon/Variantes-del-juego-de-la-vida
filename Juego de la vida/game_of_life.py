import pygame
import numpy as np
import time

#Asignamos color a los diferentes elementos en pantalla
col_about_to_die = (200, 200, 225)
col_alive = (255, 255, 215)
col_background = (10, 10, 40)
col_grid = (30, 30, 60)

#Ponemos el número de celdas en el eje X e Y
celX, celY = 50, 50

#Ponemos las dimensiones de la ventana
dimx, dimy = 700, 700

#Creamos las dimensiones de las celdas
dimCW = int(dimx / celX)
dimCH = int(dimy / celY)

#Ejecuta el juego de la vida
def main():
    
    #Iniciamos la ventana
    pygame.init()
    #Asignamos los valores de la ventana
    surface = pygame.display.set_mode((dimx, dimy))
    #Nombramos la ventana
    pygame.display.set_caption("El juego de la vida")
    #Coloreamos la superficie de la pantalla
    surface.fill(col_background)
    
    #Creamos un arreglo
    gameState =  np.zeros((celX, celY))
    
    #Sirve para la pausa
    pause = True
    step = False

    #Iniciamos un bucle
    while True:
        
        #Creamos una copia del estado del juego para poder actualizar las celdas en simultaneo
        copyState = np.copy(gameState)
        #Recolorea la pantalla para evitar que se superpongan estados anteriores
        surface.fill(col_background)
        
        #Ejecuta la función para salir del juego
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
            #Registra el click del mouse
            click = pygame.mouse.get_pressed()
            keystate = pygame.key.get_pressed()
            
            #Registra la posición del cursor y cambia el estado de la celda
            if click[0] > 0:
                posX, posY = pygame.mouse.get_pos()
                minX, minY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))
                copyState[minX,minY] = 1
            
            if click[2] > 0:
                posX, posY = pygame.mouse.get_pos()
                minX, minY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))
                copyState[minX,minY] = 0
                    
            elif event.type == pygame.KEYDOWN:
            
                #Cambia el estado del juego
                if keystate[pygame.K_SPACE]:
                    pause = not pause
                    
                if keystate[pygame.K_RETURN]:
                    step = True
                    pause = False
                
                if keystate[pygame.K_BACKSPACE]:
                    copyState = np.zeros((celX, celY))
                    gameState = np.zeros((celX, celY))
            
                    
        #Hay un delay entre pantallas para mejorar su visualización
        time.sleep(0.1)
        
        #Recorre el arreglo
        for y in range(0, celX):
            for x in range(0, celY):
                
                #Permite pausar el juego actual
                if not pause: 
                    #Suma el total de vecinos vivos
                    neighbor = gameState[(x-1) % celX, (y-1) % celY]+\
                        gameState[(x) % celX, (y-1) % celY]+\
                        gameState[(x+1) % celX, (y-1) % celY]+\
                        gameState[(x-1) % celX, (y) % celY]+\
                        gameState[(x+1) % celX, (y) % celY]+\
                        gameState[(x-1) % celX, (y+1) % celY]+\
                        gameState[(x) % celX, (y+1) % celY]+\
                        gameState[(x+1) % celX, (y+1) % celY]
                        
                    #Si una célula esta muerta y tiene 3 vecinos vivos, resucita
                    if gameState[x,y] == 0 and neighbor == 3:
                        copyState[x,y]=1
                    
                    #Si una célula esta viva y tiene menos de 2 o más de 3 vecinos vivos, muere
                    elif gameState[x,y] == 1 and (neighbor < 2 or neighbor > 3):
                        copyState[x,y]=0
                
                #Asigna la manera en como se generará la rendija
                cells = [((x) * dimCW, (y) * dimCH),
                        ((x+1) * dimCW, (y) * dimCH),
                        ((x+1) * dimCW, (y+1) * dimCH),
                        ((x) * dimCW, (y+1) * dimCH)]
                
                #Pinta en pantalla la celda correspondiente
                if copyState[x,y] == 0:
                    pygame.draw.polygon(surface, col_grid, cells,1)
                else:
                    pygame.draw.polygon(surface, col_alive, cells,0)
        
        #Actualizamos el estado de juego
        gameState = np.copy(copyState)
        
        if np.array_equal(np.zeros((celX, celY)), gameState):
            pause = True

        if step == True: 
            pause = not pause
            step = not step

        #Actualiza la pantalla
        pygame.display.flip()
        
#Ejecuta main
main()