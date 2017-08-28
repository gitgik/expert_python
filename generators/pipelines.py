"""
This file represents a generator pipeline.
You can start a series of generator functions together
into a pipe and pull items through it with a for loop.
"""
from watch import watch_file


def grep(pattern, lines):
    """A generator function to find a string in a given group of strings"""
    for line in lines:
        if pattern in line:
            yield line


# print all the log entries containing `python`
logfile = open("logs")
loglines = watch_file(logfile)
pylines = grep("python", loglines)

# pull results out of the processing pipeline
for line in pylines:
    print(line)
