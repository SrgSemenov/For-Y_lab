from termcolor import colored
import random
import time


def change_color(symbol):
    """Функция меняет цвет символа"""

    if symbol == 'X':
        return colored('X', 'yellow')
    else:
        return colored('O', 'cyan')


def sign_selection():
    """Функция предоставляет игроку выбор символа"""

    while True:
        user_input = int(input(
            f'Выберите игровую роль:\n'
            f'1 - {change_color("X")}\n'
            f'2 - {change_color("O")}\n'
            f'Ответ: '))

        if user_input == 1 or user_input == 2:
            if user_input == 1:
                player, computer = 'X', 'O'
                index = 0

            else:
                player, computer = 'O', 'X'
                index = 1

            print(f'Вы выбрали {change_color(player)}, игра началась.\n')
            time.sleep(1.5)

            gen_elements_field = {num: str(num) for num in range(1, 101)}
            gen_cells = [num for num in range(1, 101)]
            gen_names_symbols = [{'name': 'player', 'symbol': player},
                                 {'name': 'computer', 'symbol': computer}]

            return gen_elements_field, gen_cells, gen_names_symbols, index


def field_rendering(el_field):
    """ Функция выводит игровое поле в консоль """

    i_elem = 1

    for row in range(10):
        for col in range(10):

            if col == 0:
                if el_field[i_elem] == 'X' or el_field[i_elem] == 'O':
                    print(f' {change_color(el_field[i_elem])}', end='\t')
                else:
                    print(f' {el_field[i_elem]}', end='\t')

            else:
                if el_field[i_elem] == 'X' or el_field[i_elem] == 'O':
                    print(f'|{change_color(el_field[i_elem])}', end='\t')
                else:
                    print(f'|{el_field[i_elem]}', end='\t')
            i_elem += 1

        print()

        if row != 9:
            print('-' * 40)


def info():
    while True:
        print("""
        Обратные "Крестики-нолики":
    
        Игра имеет консольный интерфейс и разворачивается на поле размером 10 на 10 клеток.
        В начале игры требуется выбрать символ "X" или "O". По правилам игры первый ход делает игрок выбравший символ "X".
        Условие победы отличается от классической игры тем, что в данной версии для победы требуется избегать размещения 
        последовательности из 5 символов (по вертикали, горизонтали и диагонали). В противном случае - игрок проигрывает.
        В случае отсутствия свободных клеток - игрокам присваивается НИЧЬЯ.
    
        https://github.com/SrgSemenov/For-Y_lab
        """)

        if input('Для начала игры введите "старт": ').lower() == 'старт':
            break


def make_a_move(cell_data, el_field, symbol, player_name):
    """Функция определяет пуста ли ячейка в указанной позиции и ставит текущий символ игрока"""

    if player_name == 'player':
        while True:
            step = input('\nВаш ход! Для размещения символа на поле необжодимо ввести номер клетки.\n'
                         'Номер клетки: ')
            if step.isdigit() and (int(step) in range(1, 101)):
                step = int(step)
                if step in cell_data:
                    cell_data.remove(step)
                    el_field[step] = symbol
                    break
                else:
                    print(f'Клетка под номером "{step}" занята. Выберите другую.')
            else:
                print(f'Вы ввели не корректный символ "{step}". Ожидается целое число от 1 до 100.')

    else:
        print('\nХод компьютера.')
        time.sleep(1.5)
        step = random.choice(cell_data)
        cell_data.remove(step)
        el_field[step] = symbol


def check(el_field, cells):
    """Функция проверяет поле на наличие 5 одинаковых символов в ряд -
    (диагональ, обратная диагональ, горизонталь, вертикаль) и наличие пустых клеток"""

    for i_key in el_field:
        for symbol in ('X', 'O'):

            if len(cells) == 0:
                return 'Ничья'

            if (i_key % 10 < 7) and (i_key % 10 != 0) and (i_key // 10 < 6):
                if all(x == symbol for x in [el_field[i_key + num] for num in range(0, 44+1, 11)]):
                    return change_elem(symbol)

            if (i_key % 10 > 4 and i_key // 10 < 6) or (i_key % 10 == 0 and i_key // 10 < 7):
                if all(x == symbol for x in [el_field[i_key + num] for num in range(0, 36+1, 9)]):
                    return change_elem(symbol)

            if (i_key % 10 < 7) and (i_key % 10 != 0):
                if all(x == symbol for x in [el_field[i_key + num] for num in range(0, 4+1, 1)]):
                    return change_elem(symbol)

            if i_key < 61:
                if all(x == symbol for x in [el_field[i_key + num] for num in range(0, 40+1, 10)]):
                    return change_elem(symbol)


def restart_game():
    """Предложение игрокам начать игру заново"""

    while True:
        user = input('\nИгра окончена!'
                     '\nВведите "да" для перезапуска игры или "нет" для завершения: ')
        if user.lower() == 'да' or user.lower() == 'нет':
            if user.lower() == 'да':
                print('Перезапускаю игру.')
                time.sleep(1)
                return True
            else:
                return False


def change_elem(element):
    """Функция меняет значения на 'противоположные' """

    if element == 'X':
        element = 'O'
    elif element == 'O':
        element = 'X'
    elif element == 0:
        element = 1
    else:
        element = 0

    return element


def clear_screen():
    """Очищение игрового экрана добавлением пустых строк"""

    print('\n' * 100)


if __name__ == '__main__':
    info()
    elements_field, cells_lst, names_symbols, i = sign_selection()
    restart_flag = False

    while True:
        if restart_flag:
            info()

            elements_field, cells_lst, names_symbols, i = sign_selection()
            flag = False

        clear_screen()

        field_rendering(el_field=elements_field)

        make_a_move(cell_data=cells_lst,
                    el_field=elements_field,
                    symbol=names_symbols[i]['symbol'],
                    player_name=names_symbols[i]['name'])

        result_check = check(el_field=elements_field, cells=cells_lst)

        if result_check:
            field_rendering(elements_field)

            if result_check == 'Ничья':
                print(f'\nПустых клеток не осталось. {result_check}!')
            else:
                print(f'\nПобедил "{result_check}"!')

            restart_flag = restart_game()

            if restart_flag:
                pass
            else:
                break

        i = change_elem(i)

        clear_screen()
