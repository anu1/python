#!/bin/python

# print("Welcome to Python")

# include all the libraries
import os

# function to tail the last n lines of the given file, n=10 by default
def tail(path, n=10):
    # return the last n lines of path
    #
    # path --> /var/log/messages
    # newline --> \n
    #
    # size: empty --> several hundreds of GB
    myfile = path
    lcount = 0
    
    # to move the file pointer to the last position 
    # checking the file pointer options (online)
    # fp.seek(offset, from_what)
    # where fp is the file pointer you're working with; offset means how many positions you will move; from_what defines your point of reference:

    # 0: means your reference point is the beginning of the file
    # 1: means your reference point is the current file position
    # 2: means your reference point is the end of the file
    
    with open(myfile, "r") as fp:
        fp.seek(0,2) # to go to the end of the file
        filesize = fp.tell() # to get the total file size 
        
        approx_size_in_bytes = n * 1024  # assuming 80 chars for  a single line
        fp.seek(max( filesize  - approx_size_in_bytes , 0 ), 0) # moved the file pointer to file size - n * 80 bytes
        
        lines = fp.readlines() # read the lines from the current position.

        # now need to pick only n lines from the list lines.

    return lines[-n:] # testing
# lines[0:n] 
#    lines[:1]
 
def main():
    p = "thumbtack.py"
    for line in tail(p, 10):
        print(line, end='')
    
if __name__ == "__main__":
        main()
