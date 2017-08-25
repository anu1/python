import csv

def links():

    # open both files
    with open('in1.csv') as in1, open('in2.csv') as in2:

        # using DictReader instead to be able more easily access information by num
        csv_in1 = csv.DictReader(in1)
        csv_in2 = csv.DictReader(in2)

        # create dictionaries out of the two CSV files using dictionary comprehensions
        in1_dict = {row['Num']:row['status'] for row in csv_in1}
        in2_dict = {row['Num']:row['code'] for row in csv_in2}   
    print(in1_dict)
    print(in2_dict)
    # print header, each column has width of 8 characters
    print("{} | {} | {}".format("Num", "Status", "Code"))

    # print the information
    for num, status in in1_dict.items():

        # call to in2_dict.get() - will get values out of the in2 dictionary,
        # specifying a default return value of an empty string if num is not found in it to avoid an exception
       print("{} | {} | {}".format(num, status, in2_dict.get(num, '')))

links()
