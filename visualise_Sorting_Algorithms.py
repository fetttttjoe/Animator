import time
import pygame
import numpy as np
from screeninfo import get_monitors
ARRAY_LENGTH = 10000
def Visualize():
    win.fill((0,0,0))
    # Draw lines
    for i in range(0,win_width):
        pygame.draw.line(win, (255, 255, 255), (i, win_height), (i, values[0][i]))
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
  
    values = GenValues(win_width, win_height)

    # Initialize pygame
    pygame.init()
    win = pygame.display.set_mode((win_width, win_height))
    pygame.display.set_caption('Visualize Bubble Sort')
    stop = False
    done = False
    
    while stop == False:
        pygame.time.delay(100)
    
        if (done == False):
            t0 = time.time()
            #iterations, swaps = BubbleSort(values)
            iterations, swaps = InsertionSort(values)
            t1 = time.time()
            done = True
            print(f'\nMade {swaps} swaps in {iterations} iterations\n')
            print(f"The whole Process took {t1-t0} seconds")
        # Make sure we can close the window with 'X'
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop = True



