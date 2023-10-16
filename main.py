from Loggers import read_notes, add_note, del_note, edit_note, filter_of_date, print_note

def main():
    print('Для работы с программой выберите нужное действие:')
    print('1 - вывести все заметки\n'
            '2 - создать новую заметку\n'
            '3 - редактировать заметку\n'
            '4 - удалить заметку\n'
            '5 - сделать выборку по дате\n'
            '6 - вывести заметку\n'
            '7 - завершение работы\n')
    while True:
        comand  = int(input('Введите цифру, соответствующую команде:'))
        if comand not in (1, 2, 3, 4, 5, 6, 7):
            print('Такой команды не существует!')
            print(' ')
            main()
        elif comand == 1:
            read_notes()
        elif comand == 2:
            add_note()
        elif comand == 3:
            edit_note()
        elif comand == 4:
            del_note()
        elif comand == 5:
            filter_of_date()
        elif comand == 6:
            print_note()
        elif comand == 7:
            return
        
if __name__ == '__main__':
      main()