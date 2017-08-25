import time, csv


def links():
    first = open('in1.csv')
    csv_file1 = csv.reader(first, delimiter=",")


    second = open('in2.csv')
    csv_file2 = csv.reader(second, delimiter=",")

    list=[]
    for row in csv_file2:
        list.append(row)


    for row in csv_file1:
        match=False  
        for secrow in list:                             
            if row[0].replace(" ","") == secrow[0].replace(" ",""):
                print(row[0] + "," + row[1] + "," + secrow[1])
                match=True
        if not match:
            print(row[0] + "," + row[1] + ", blank no match") 
        time.sleep(1)
links()
