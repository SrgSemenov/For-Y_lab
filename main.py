import random
from termcolor import colored
import time


def sign_selection():
    """Функция предоставляет игроку выбор символа"""

    while True:
        user_input = int(input(
            f'Выберите игровую роль:\n'
            f'1 - {colored("X", "yellow")}\n'
            f'2 - {colored("O", "cyan")}\n'
            f'Ответ: '))

        if user_input == 1 or user_input == 2:
            if user_input == 1:
                player, computer = 'X', 'O'
                index = 0

            else:
                player, computer = 'O', 'X'
                index = 1

            print(f'Вы выбрали {player}, игра началась.\n')
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
                if el_field[i_elem] == 'X':
                    print(f' {colored(el_field[i_elem], "yellow")}', end='\t')
                elif el_field[i_elem] == 'O':
                    print(f' {colored(el_field[i_elem], "cyan")}', end='\t')
                else:
                    print(f' {el_field[i_elem]}', end='\t')

            else:
                if el_field[i_elem] == 'X':
                    print(f'|{colored(el_field[i_elem], "yellow")}', end='\t')
                elif el_field[i_elem] == 'O':
                    print(f'|{colored(el_field[i_elem], "cyan")}', end='\t')
                else:
                    print(f'|{el_field[i_elem]}', end='\t')
            i_elem += 1

        print()

        if row != 9:
            print('-' * 40)


def make_a_move(cell_data, el_field, symbol, player_name):
    """Функция определяет пуста ли ячейка в указанной позиции и ставит текущий символ игрока"""

    if player_name == 'player':
        while True:
            step = int(input('\nВаш ход! \nВведите номер клетки: '))
            if (step in range(1, 101)) and (step in cell_data):
                cell_data.remove(step)
                el_field[step] = symbol
                break
            print('Некорректный номер клетки или клетка уже занята.')
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
                if (el_field[i_key] == symbol) \
                        and (el_field[i_key + 11] == symbol) \
                        and (el_field[i_key + 22] == symbol) \
                        and (el_field[i_key + 33] == symbol) \
                        and (el_field[i_key + 44] == symbol):
                    return change_elem(symbol)

            if (i_key % 10 > 4 and i_key // 10 < 6) or (i_key % 10 == 0 and i_key // 10 < 7):
                if (el_field[i_key] == symbol) \
                        and (el_field[i_key + 9] == symbol) \
                        and (el_field[i_key + 18] == symbol) \
                        and (el_field[i_key + 27] == symbol) \
                        and (el_field[i_key + 36] == symbol):
                    return change_elem(symbol)

            if (i_key % 10 < 7) and (i_key % 10 != 0):
                if (el_field[i_key] == symbol) \
                        and (el_field[i_key + 1] == symbol) \
                        and (el_field[i_key + 2] == symbol) \
                        and (el_field[i_key + 3] == symbol) \
                        and (el_field[i_key + 4] == symbol):
                    return change_elem(symbol)

            if i_key < 61:
                if (el_field[i_key] == symbol) \
                        and (el_field[i_key + 10] == symbol) \
                        and (el_field[i_key + 20] == symbol) \
                        and (el_field[i_key + 30] == symbol) \
                        and (el_field[i_key + 40] == symbol):
                    return change_elem(symbol)


def restart_game():
    """Предложение игрокам начать игру заново"""

    while True:
        user = input('\nВведите "да" для перезапуска игры или "нет" для завершения: ')
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

    elements_field, cells_lst, names_symbols, i = sign_selection()
    restart_flag = False

    while True:
        if restart_flag:
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
