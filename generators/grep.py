"""This file represents a coroutine
When you use yield by calling it directly (yield)
it becomes a coroutine.
Instead of just jenerating values,
Functions can consume values sent to them.

Usage:
>>>    g = grep("python")
>>>    g.next()
Looking for python
>>>    g.send("This is a good song")
>>>    g.send("This song has python in it!")
This song has python in it!
"""

def grep(pattern):
    print ("Looking for {}".format(pattern))
    while True:
        line = (yield)
        if pattern in line:
            print (line)

