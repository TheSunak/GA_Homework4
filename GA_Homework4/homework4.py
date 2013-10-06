import os
import csv
import collections
from collections import Counter


#os.path

#train_data = csv.reader(open("train.csv", "rb"))

#for row in train_data:
 #   print row


#Create an array of the words of interest

#search_words = [
# 'fuck',
# 'moron',
# 'retard',
# 'loser',
# 'stupid',
# 'sick',
# 'dick',
# 'ass',
# 'nigga',
# 'nigger',
# 'pussy',
# 'bitch',
# 'faggot',
# 'idiot',
# 'crap',
#]

# test_line = "Hey fuck fuck fuck head"

# word = test_line.split()

# print word

# cnt = Counter(word)

# print cnt["fuck"]

#Code from Stackoverflow:
# grades = collections.Counter()
# with open('train.csv') as input_file:
#     for row in csv.reader(input_file, delimiter=','):
#         grades[row[2]] += 1

# print 'Number of A grades: %s' % grades['A']
# print grades.most_common()

grades = collections.Counter()
with open('train2.csv') as input_file:
        for row in csv.reader(input_file, delimiter=','):
            print row[2]
            split_words = row[2].split()
            print split_words
            cnt = Counter(split_words)

            print cnt


            #print cnt["fuck"]





#build a For loop:

#Reads in each line of the train file, determines if any of the words on the search words array is there

#If it does, store the Row number into a results array... row number and Insults (1 or 0)

