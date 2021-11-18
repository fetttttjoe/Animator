import time
import pygame
import numpy as np
from screeninfo import get_monitors
ARRAY_LENGTH = 10000
def Visualize():
    screen.fill((0,0,0))
    # Draw lines make sure they fit into display
    for i in range(0,win_width):
        pygame.draw.line(screen, (255, 255, 255), (i, win_height), (i, values[0][i]))
    pygame.display.update()
def InsertionSort(values):
    swaps = 0
    iterations = 0
    for i in range(1, len(values[0])):
        key_item = values[0][i]

        j = i - 1
        while j >= 0 and values[0][j] > key_item:
            swaps += 1
            values[0][j + 1] = values[0][j]
            j -= 1
        Visualize()
        iterations += 1 
        values[0][j + 1] = key_item
    return iterations, swaps
def BubbleSort(values):
    iterations = 0
    swaps = 0
    IsSwapped = True
    while(IsSwapped):
        IsSwapped = False

        for i in range(len(values[0]) - iterations - 1):
            if (values[0][i] > values[0][i + 1]):
                values[0][i], values[0][i + 1] = values[0][i + 1], values[0][i] 
                IsSwapped = True
                swaps +=1
        Visualize()
        iterations += 1
    return iterations, swaps
def DispayText(screen, x, y, text, size):
    pygame.font.init()
    font = pygame.font.SysFont('Comic Sans MS', size) #trololo
    textsurface = font.render(f'{text}', True, 'RED')
    screen.blit(textsurface, (x, y))
def GenValues(win_width, win_height):
  return np.random.rand(1, win_width)*win_height 
if __name__ == '__main__':
    for monitor in get_monitors():
        monitor=str(monitor).split(',')
    #make sure we get the correct monitor size
    monitor = monitor[2].split('='), monitor[3].split('=')
    
    # Set parameters
    win_width   = int(int(monitor[0][1])/2) 
    win_height  = int(int(monitor[1][1])/2)
  

    # Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((win_width, win_height))
    pygame.display.set_caption('Visualize Bubble Sort')
    stop = False
    done = False
   
    while stop == False:
        pygame.time.delay(100)
    
        if (done == False):
   
            
            values = GenValues(win_width, win_height)
            DispayText(screen, int(win_width/3), int(win_height/2), "Insertion Sort", 50)
            pygame.display.update()
            time.sleep(3)
            print(f"The Dataset has a size of: {len(values[0])}\n") 
            t0 = time.time()
            iterationsI, swapsI = InsertionSort(values)
            t1 = time.time()  
            screen.fill((0,0,0))
            DispayText(screen, int(win_width/3), int(win_height/2), "Bubble Sort", 50)
            pygame.display.update()
            time.sleep(3) 
            values = GenValues(win_width, win_height)
            screen.fill((0,0,0))
            t2 = time.time()
            iterationsB, swapsB = BubbleSort(values)
            t3 = time.time()
            done = True
            print(f'\nInsertionSort made {swapsI} swaps in {iterationsI} iterations\n')
            print(f"The whole Process took {t1-t0} seconds")
            print(f'BubbleSort made {swapsB} swaps in {iterationsB} iterations\n')
            print(f"The whole Process took {t3-t2} seconds")
        # Make sure we can close the window with 'X'
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop = True



