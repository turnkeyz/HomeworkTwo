##Kyler Telge 1825829
import csv

date = input()
with open('inputDates.txt', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        for i in row:
            if csvreader[i].find('%m' <= 0):
                break
            else:
                print('%m/%d/%y%', date)

