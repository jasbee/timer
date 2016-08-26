import time

x = input('Press s to start or q to quit: ')

while x != 's' and x != 'q':
    x = input('Please enter s to start or q to quit: ')
    print(' ')

if x is 's':
    start = time.clock()

    while x is not 'q':
        x = input('Press enter to print out the time or press q to quit: ')
        current = time.clock() - start

        minutes, seconds = divmod(current, 60)

        hours, minutes = divmod(minutes, 60)

        a = str(round(hours, 0))
        b = str(round(minutes, 0))
        c = str(round(seconds, 2))

        print(a + ':' + b + ':' + c)