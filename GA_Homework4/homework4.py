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

search_words = [
'fuck',
'fucking',
'moron',
'morons',
'retard',
'loser',
'stupid',
'sick',
'dick',
'ass',
'nigga',
'nigger',
'pussy',
'bitch',
'faggot',
'idiot',
'crap',
'damn',
'fool',
'fag',
'gay',
'fat',
'ugly',
'hate',
'wtf',
'racist',
'smack',
'pervert',
'perverted',
]

punc=('.')

dirty_comments = 0
total_rows = 0
insult = 0

grades = collections.Counter()
with open('train.csv') as input_file:
        with open('output.csv', 'w') as csvoutput:
            writer = csv.writer(csvoutput)
            for row in csv.reader(input_file, delimiter=','):
                
                row = map(str.lower,row)
                
                print row

                insult = 0

                total_rows = total_rows + 1    
                split_words = row[2].replace(punc,"").split()
                

                #print split_words
                cnt = Counter(split_words)

                #print cnt

                #Run the split words and check against our dirty words:
                for word in search_words:
                    #print word
                    if cnt[word] > 0:
                        dirty_comments = dirty_comments + 1
                        insult = 1
                        break

                if insult == 1:
                    writer.writerow(row+['Insult'])
                else:
                     writer.writerow(row+['Not an Insult'])

        print "number of rows"
        print total_rows

        print "number of insults"
        print dirty_comments

         


            #cnt holds the results of each check.    
            #print cnt["fuck"]





#build a For loop:

#Reads in each line of the train file, determines if any of the words on the search words array is there

#If it does, store the Row number into a results array... row number and Insults (1 or 0)

