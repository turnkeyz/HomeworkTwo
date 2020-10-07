##Kyler Telge 1825829
import csv

file = input()
wordsFreq = {}
with open(file, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        for word in row:
            if word not in wordsFreq.keys():
                wordsFreq[word] = 1
            else:
                wordsFreq[word] += 1
        for key in wordsFreq.keys():
            print(key + ' ' + str(wordsFreq[key]))