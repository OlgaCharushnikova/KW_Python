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



def del_note():
    del_Id = input('Введите Id: ')
    with open("notes.csv", encoding='utf-8') as f:
        file = csv.DictReader(f, delimiter = ";")
        for row in file:
            if row["Id"] != del_Id and row["Id"] != 'Id':
                with open("new_notes.csv", mode="a", encoding='utf-8') as ff:
                    new_entry = ["Id", "Название","Тело", "Дата"]
                    ffile = csv.DictWriter(ff, delimiter = ";", 
                                                lineterminator="\r", fieldnames=new_entry)
                    ffile.writeheader()
                    ffile.writerow({"Id": row["Id"], "Название": row["Название"], "Тело": row["Тело"], "Дата" : row["Дата"]})
    os.remove("notes.csv")
    os.rename("new_notes.csv", "notes.csv")  


def edit_note():
    del_Id = input('Введите Id: ')
    with open("notes.csv", encoding='utf-8') as f:
        file = csv.DictReader(f, delimiter = ";")
        new_title = input('Введите новое название: ')
        new_body = input('Введите новое тело заметки: ')
        new_date = datetime.datetime.now().strftime("%Y-%m-%d")
        with open("new_notes.csv", mode="w", encoding='utf-8') as ff:
                new_entry = ["Id", "Название","Тело", "Дата"]
                ffile = csv.DictWriter(ff, delimiter = ";", 
                                            lineterminator="\r", fieldnames=new_entry)
                file.writeheader()
                file.writerow({"Id": del_Id, "Название": new_title, "Тело": new_body, "Дата" : new_date})
        for row in file:        
            if row["Id"] != del_Id and row["Id"] != 'Id':
                with open("new_notes.csv", mode="a", encoding='utf-8') as w_file:
                    new_entry = ["Id", "Название","Тело", "Дата"]
                    file_writer = csv.DictWriter(w_file, delimiter = ";", 
                                            lineterminator="\r", fieldnames=new_entry)
                    file_writer.writeheader()
                    file_writer.writerow({"Id": row["Id"], "Название": row["Название"], "Тело": row["Тело"], "Дата" : row["Дата"]})
    os.remove("notes.csv")
    os.rename("new_notes.csv", "notes.csv")