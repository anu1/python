def main():

    import random

    #Open a file named numbersmake.txt.
    outfile = open('numbersmake.txt', 'a+')

    #Produce the numbers
    for count in range(12):
        #Get a random number.
        num = random.randint(1, 100)

    #Write 12 random intergers in the range of 1-100 on one line
    #to the file.
    outfile.write(str(num) + ' ')

    #Close the file.
    outfile.close()
    print('Data written to numbersmake.txt')
    print()
print()    
#Call the main function
main()
