import csv
import os
import datetime
def read_notes():
    with open("notes.csv", encoding='utf-8') as f:
        file= csv.DictReader(f, delimiter = ";")
        for row in file:
            for key, value in row.items():
                print("{0}: {1}".format(key,value))
            print('-----------------------------------')


def add_note():
    with open("notes.csv", mode="a", encoding='utf-8') as f:
        new_entry = ["Id", "Название","Тело", "Дата"]
        file = csv.DictWriter(f, delimiter = ";", 
                                    lineterminator="\r", fieldnames=new_entry)
        new_Id = input('Введите Id: ')
        for row in file:
            if row["Id"] == new_Id:
                    print('Такой Id уже существует, введите новый Id: ')
                    new_Id = input('Введите Id: ')
        new_title = input('Введите название: ')
        new_body = input('Введите тело заметки: ')
        new_date = datetime.datetime.now().strftime("%Y-%m-%d")
        file.writeheader()
        file.writerow({"Id": new_Id, "Название": new_title, "Тело": new_body, "Дата" : new_date})    