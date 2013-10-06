import os
import csv
os.path

os.listdir('/home/gregory/Dropbox/GA/homework4')

train_data = csv.reader(open("train.csv", "rb"))

for row in train_data:
    print row


