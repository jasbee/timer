import time
import msvcrt

x = input('Press s to start, p to pause, or r to reset: ')

if x is 's':
    start = time.clock()
    x1 = 's'

    while True:
        if x is 'p':
            x = msvcrt.getwch()
            x1 = 'p'
        elif x is 'r':
            start = time.clock()
            print('         ', end='\r')
            print('0:0:0.00', end='\r')
            x = msvcrt.getwch()
        elif x is 's':
            if msvcrt.kbhit():
                x = msvcrt.getwch()
            else:
                current = time.clock() - start
                minutes = current / 60
                seconds = current % 60
                hours = minutes / 60
                minutes = minutes % 60
                a = str(int(hours))
                b = str(int(minutes))
                c = str(round(seconds, 2))
                print(a + ':' + b + ':' + c, end='\r')
                x1 = 's'
        else:
            x = x1
