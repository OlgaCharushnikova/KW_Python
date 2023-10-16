import csv
import os
import datetime
def read_notes():
    with open("notes.csv", encoding='utf-8') as r_file:
        file_reader = csv.DictReader(r_file, delimiter = ";")
        for row in file_reader:
            for key, value in row.items():
                print("{0}: {1}".format(key,value))
            print('-----------------------------------')