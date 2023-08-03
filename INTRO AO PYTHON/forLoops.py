# for loop = a loop that runs a specific number of times

# module time for the contdown to work with timers => in JS is setInterval() or setTimeout()
import time

# this example we can achieve in JS with setInterval()
# countdown from 10 to 0 with every second
for i in range(10, 0, -1):
    print(i)
    # for every 1 second
    time.sleep(1)
    if i == 1:
        print("Happy New Year!")
