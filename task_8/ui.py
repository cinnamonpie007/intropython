from logger import input_data, print_data, copy_data, remove_val


def interface():
    print('Добрый день! Это бот-помощник. \n'
          'Что вы хотите сделать? \n'
          '1 - Записать данные \n'
          '2 - Вывести данные\n'
          '3 - Скопировать данные')
    command = int(input('Ваш выбор: '))

    while command < 1 or command > 4:
        command = int(input('Ошибка! Ваш выбор: '))

    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        source_file = ''
        destination_file = ''
        print('1 - data_first_variant.csv\n'
              '2 - data_second_variant.csv\n')
        file_in = int(input("Введите имя файла, из которого нужно скопировать данные: "))
        while file_in < 1 or file_in > 2:
            file_in = int(input('Ошибка! Ваш выбор: '))
        if file_in == 1:
            source_file = 'data_first_variant.csv'
        elif file_in == 2:
            source_file = 'data_second_variant.csv'
        file_to = int(input("Введите имя файла, в который нужно скопировать данные: "))
        while file_to < 1 or file_to > 2:
            file_to = int(input('Ошибка! Ваш выбор: '))
        if file_to == 1:
            destination_file = 'data_first_variant.csv'
        elif file_to == 2:
            destination_file = 'data_second_variant.csv'
        val = input("Введите значение для копирования: ")
        copy_data(source_file, destination_file, val)


interface()
