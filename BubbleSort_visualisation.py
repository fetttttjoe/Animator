import pygame
import numpy
from screeninfo import get_monitors
def Visualize():
    win.fill((0,0,0))
    # Draw lines
    for i in range(0,win_width):
        pygame.draw.line(win, (255, 255, 255), (i, win_height), (i, values[0][i]))
    pygame.display.update()
def BubbleSort():
    iterations = 0
    swaps = 0
    IsSwapped = True
    while(IsSwapped):
        IsSwapped = False
        for i in range(len(values[0]) - iterations - 1):
            if (values[0][i] > values[0][i+1]):
                values[0][i], values[0][i+1] = values[0][i+1], values[0][i] 
                IsSwapped = True
                swaps +=1
        Visualize()
        iterations += 1
    return iterations, swaps


if __name__ == '__main__':
    for monitor in get_monitors():
        monitor=str(monitor).split(',')
    monitor = monitor[2].split('='), monitor[3].split('=')
    print(monitor)
    # Set parameters
    win_width   = int(int(monitor[0][1])/2) 
    win_height  = int(int(monitor[1][1])/2)
    values = numpy.random.rand(1,win_width)*win_height 
    
    # Initialize pygame
    pygame.init()
    win = pygame.display.set_mode((win_width, win_height))
    pygame.display.set_caption('Visualize Bubble Sort')
    stop = False
    done = False
    
    while stop == False:
        pygame.time.delay(100)
    
        if (done == False):
            iterations, swaps = BubbleSort()
            done = True
            print(f'\nNumber of swaps made: {swaps} in {iterations} iterations')
        # Make sure we can close the window with 'X'
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop = True
