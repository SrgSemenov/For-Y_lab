from itertools import product


def calculation_and_output(data_lst):
    for elem in data_lst:
        result_int = 0
        result_str = ''
        elem.append(elem[0])

        for num in range(len(elem) - 1):
            point_1, point_2 = elem[num], elem[num + 1]
            x1, y1 = point_1[0], point_1[1]
            x2, y2 = point_2[0], point_2[1]
            current_path = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
            result_int += current_path

            if len(result_str) == 0:
                result_str = f'{point_1} -> {point_2}[{result_int}]'
            else:
                result_str += f' -> {point_2}[{result_int}]'

        result_str += f' = [{result_int}]'
        yield result_str, result_int
    return


points_lst = [(0, 2), (2, 5), (5, 2), (6, 6), (8, 3)]
points_len = len(points_lst)


if __name__ == '__main__':

    routes_lst = filter(lambda x: len(set(x)) == 5 and (x[0] == points_lst[0]), product(points_lst, repeat=points_len))

    routes_lst = (list(elem) for elem in routes_lst)

    min_path = min(calculation_and_output(data_lst=routes_lst), key=lambda x: x[1])

    print(min_path[0])
