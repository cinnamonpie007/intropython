from data_create import input_user_data


def input_data():
    name, surname, phone, adress = input_user_data()
    var = int(input(f'\nВ каком формате записать данные? \n'
                    f'1 Вариант:\n'
                    f'{name}\n'
                    f'{surname}\n'
                    f'{phone}\n'
                    f'{adress}\n\n'
                    f'2 Вариант:\n'
                    f'{name};{surname};{phone};{adress}\n\n'
                    f'Ваш выбор: '))
    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as file:
            file.write( f'{name}\n'
                        f'{surname}\n'
                        f'{phone}\n'
                        f'{adress}\n\n')
    else:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name};{surname};{phone};{adress}\n\n')


def print_data():
    print('1 файл:')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
        print(''.join(data))
        
    print('2 файл:')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
        print(''.join(data))


def copy_data(source_file, destination_file, val):
    if source_file == 'data_first_variant.csv':
        with open(source_file, 'r', encoding='utf-8') as source:
            lines = source.readlines()
            for i, j in enumerate(lines):
                j = j.split()
                if val in j:
                    j1 = lines[i]
                    j2 = lines[i + 1]
                    j3 = lines[i + 2]
                    j4 = lines[i + 3]
                    with open(destination_file, 'a', encoding='utf-8') as destination:
                        destination.write(f'\n{j1}{j2}{j3}{j4}')
                    print("Данные успешно скопированы.")
                    break
    elif source_file == 'data_second_variant.csv':
        with open(source_file, 'r', encoding='utf-8') as source:
            lines = source.readlines()
            for i, j in enumerate(lines):
                if val in j:
                    with open(destination_file, 'a', encoding='utf-8') as destination:
                        destination.write(f'\n{j}')
                    print("Данные успешно скопированы.")
                    break