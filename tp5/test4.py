import csv
with open('test22.csv','r') as file5:
    csv_reader=csv.reader(file5)
    for line in csv_reader:
        print(line)
