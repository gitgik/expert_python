'''
This file represents a generator function.
A generator function when called creates a generator object.
However, it does not start running the function.
The function only executes on next()

Example:

   >>> x = func(10)
   >>> x
   <generator object at 0x58490>
   >>> x.next()
   10
   >>> x.next()
   9
   >>>
'''

import time



def watch_file(thefile):
    """A function to read and watch the last line of a file"""

    # Go to the end of the file
    thefile.seek(0, 2)
    while True:
        line = thefile.readline()
        if not line:
            # sleep briefly
            time.sleep(0.1)
            continue
        yield line


# Practical example
logfile = open("logs")
for line in watch_file(logfile):
    print (line),
