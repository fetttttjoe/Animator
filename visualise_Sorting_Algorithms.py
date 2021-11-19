import time
import pygame
from random import randint, randrange
from screeninfo import get_monitors
iterationsM = 0
swapsM = 0
iterationsQ = 0
swapsQ = 0
def Visualize(values, color = (255,255,255)):
    screen.fill((0,0,0))
    # Draw lines make sure they fit into display
    for i in range(0,len(values)):
        #print('i: ', i, '\n')
        pygame.draw.line(screen, color, (i, win_height), (i, values[i]))  # Using win_height because max is incredibly slow
    pygame.display.update()
def InsertionSort(values):
    swaps = 0
    iterations = 0
    for i in range(1, len(values)):
        key_item = values[i]

        j = i - 1
        while j >= 0 and values[j] > key_item:
            swaps += 1
            values[j + 1] = values[j]
            j -= 1
        Visualize(values)
        iterations += 1 
        values[j + 1] = key_item
    return iterations, swaps
def BubbleSort(values):
    iterations = 0
    swaps = 0
    IsSwapped = True
    while(IsSwapped):
        IsSwapped = False

        for i in range(len(values) - iterations - 1):
            if (values[i] > values[i + 1]):
                values[i], values[i + 1] = values[i + 1], values[i] 
                IsSwapped = True
                swaps +=1
        Visualize(values)
        iterations += 1
    return iterations, swaps
def Merge(left, right):
    global iterationsM
    global swapsM
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left
    result = []
    index_left  = 0
    index_right = 0
    while len(result) < len(left) + len(right):
        
        
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left  += 1
            swapsM += 1
        else:
            result.append(right[index_right])
            index_right += 1
            swapsM += 1
        if index_right == len(right):
            result += left[index_left:]
            break
        if index_left  == len(left):
            result += right[index_right:]
            break;
    iterationsM += 1
    #use random color to make it more visible what happens #shitsolution
    Visualize(result, (randrange(1,256),randrange(1,256),randrange(1,256)))
    return result
def MergeSort(values):
    
    if len(values) < 2:
        return values
    midpoint = len(values) // 2
    return Merge(
                    left    = MergeSort(values[ :midpoint]),
                    right   = MergeSort(values[midpoint: ]))
def QuickSort(values):
    global iterationsQ
    global swapsQ
    if len(values) < 2:
        return values
    low  = []
    same = []
    high = []
    # choose random pivot element from array values
    pivot = values[randint(0, len(values) - 1)]
    for item in values:
        iterationsQ += 1
        if item < pivot:
            low.append(item)
            swapsQ += 1
        elif item == pivot:
            same.append(item)
            swapsQ += 1
        elif item > pivot:
            high.append(item)
            swapsQ += 1
    temp = QuickSort(low) + same + QuickSort(high)
    Visualize(temp, (randrange(1,256),randrange(1,256),randrange(1,256)))
    return temp
def DisplayText(screen, x, y, text, size):
    pygame.font.init()
    font = pygame.font.SysFont('Comic Sans MS', size) #trololo
    textsurface = font.render(f'{text}', True, 'RED')
    screen.blit(textsurface, (x, y))
    pygame.display.update()
def GenValues(win_width, win_height):
  #return np.random.rand(1, win_width)*win_height 
  return [randint(0, win_height) for i in range(win_width)]
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
            DisplayText(screen, int(win_width/3), int(win_height/2), "Insertion Sort", 50)
            time.sleep(3)
            print(f"The Dataset has a size of: {len(values)}\n") 
            t0 = time.time()
            iterationsI, swapsI = InsertionSort(values)
            t1 = time.time()  
            time.sleep(2)
            screen.fill((0,0,0))
            DisplayText(screen, int(win_width/3), int(win_height/2), "Bubble Sort", 50)
            time.sleep(3) 
            values = GenValues(win_width, win_height)
            screen.fill((0,0,0))
            t2 = time.time()
            iterationsB, swapsB = BubbleSort(values)
            t3 = time.time()
            time.sleep(2)
            screen.fill((0,0,0))
            DisplayText(screen, int(win_width/3), int(win_height/2), "Merge Sort", 50)
            time.sleep(3)
            values = GenValues(win_width, win_height)
            t4 = time.time()            
            MergeSort(values)
            t5 = time.time()
            time.sleep(3)
            screen.fill((0,0,0))
            DisplayText(screen, int(win_width/3), int(win_height/2), "Quick Sort", 50)
            time.sleep(3)
            t6 = time.time()
            QuickSort(values)
            t7 = time.time()
            done = True
            print(f'\nInsertionSort made {swapsI} swaps in {iterationsI} iterations')
            print(f"The whole Process took {t1-t0} seconds\n")
            print(f'BubbleSort made {swapsB} swaps in {iterationsB} iterations')
            print(f"The whole Process took {t3-t2} seconds\n")
            print(f"Merge Sort made {swapsM} swaps in {iterationsM} iterations")
            print(f"The Process took {t5-t4} seconds\n")
            print(f"Quick Sort made {swapsQ} swaps in {iterationsQ} iterations")
            print(f"The Process took {t7-t6} seconds\n")
        # Make sure we can close the window with 'X'
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop = True
