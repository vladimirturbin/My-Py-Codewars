def is_neighborhood(shapemap, x, y, symbol):
    limit_left = True if x == 0 else False
    limit_right = True if x == len(shapemap[y]) - 1 else False
    limit_top = True if y == 0 else False
    limit_bottom = True if y == len(shapemap) - 1 else False

    if not limit_top:
        if shapemap[y - 1][x] == symbol:
            return True
    if not limit_top and not limit_right:
        if shapemap[y - 1][x + 1] == symbol:
            return True
    if not limit_right:
        if shapemap[y][x + 1] == symbol:
            return True
    if not limit_right and not limit_bottom:
        if shapemap[y + 1][x + 1] == symbol:
            return True
    if not limit_bottom:
        if shapemap[y + 1][x] == symbol:
            return True
    if not limit_bottom and not limit_left:
        if shapemap[y + 1][x - 1] == symbol:
            return True
    if not limit_left:
        if shapemap[y][x - 1] == symbol:
            return True
    if not limit_left and not limit_top:
        if shapemap[y - 1][x - 1] == symbol:
            return True
    return False


def break_pieces(shape):
    shapemap = shape.split('\n')

    # Сразу заменим ведущие пробелы (не входящие внутрь ни одной из фигур) на*
    shapemap = [[char for char in string] for string in shapemap]
    for y in range(len(shapemap)):
        x = 0
        while x < len(shapemap[y]) and shapemap[y][x] == ' ':
            shapemap[y][x] = '*'
            x += 1

    # Так же как и пробелы в конце строк
    for y in range(len(shapemap)):
        deleted_symbols_counter = 0
        while shapemap[y][-1] == ' ':
            del shapemap[y][-1]
            deleted_symbols_counter += 1
        shapemap[y] += '*' * deleted_symbols_counter
    print('\n'.join([''.join(string) for string in shapemap]))

    # И заодно дополним астериксами все строки до одной длины х_х
    max_len = 0
    for current_string in shapemap:
        max_len = max(max_len, len(current_string))
    for curr_string in shapemap:
        curr_string += '*' * (max_len - len(curr_string))

    # А потом пробелы снизу, пробелы сверху х_х

    clean0 = False  # Рассказывает о том, что прошел полный цикл,
    # кусочков с пробелами не осталось и главный цикл
    # можно завершать (не хаходить в него больше).

    clean1 = True  # Для целей поиска нового чистого кусочка из одних пробелов
    # - рассказывает о том, что сейчас нужно его
    # искать (и ставить в него первый символ '!')

    clean2 = False  # Для контроля того, нужно ли ещё ставить символы '!'
    # в тот кусочек, который заполняем прямо сейчас

    result = []
    
    while not clean0:
        clean0 = True
        clean1 = True
        clean2 = False

        for y in range(len(shapemap) - 1):
            for x in range(len(shapemap[y]) - 1):
                if shapemap[y][x] == ' ':
                    shapemap[y][x] = '!'
                    clean1 = False
                    break
            if not clean1:
                clean0 = False
                break

        if clean0:
            break

        x_numbers = set()
        y_numbers = set()

        # for y in range(len(piece)):
        #     while piece[y][-1] == ' ':
        #         del piece[y][-1]
        # Здесь заполним целый кусочек, с которым сейчас работаем, символами !
        while not clean2:
            clean2 = True
            for y in range(len(shapemap) - 1):
                for x in range(len(shapemap[y]) - 1):
                    if shapemap[y][x] == ' ' and is_neighborhood(shapemap, x,
                                                                 y, '!'):
                        shapemap[y][x] = '!'
                        clean2 = False
        for y in range(len(shapemap) - 1):
            for x in range(len(shapemap[y]) - 1):
                if shapemap[y][x] == '!':
                    x_numbers.add(x)
                    y_numbers.add(y)
        if x_numbers and y_numbers:
            piece = [[' ' for x in range(max(x_numbers) - min(x_numbers) + 3)]
                     for y in range(max(y_numbers) - min(y_numbers) + 3)]

        borders = {'-', '|', '+'}

        if x_numbers and y_numbers:
            for y in range(min(y_numbers) - 1, max(y_numbers) + 2):
                for x in range(min(x_numbers) - 1, max(x_numbers) + 2):
                    if shapemap[y][x] in borders and is_neighborhood(shapemap,
                                                                     x, y,
                                                                     '!'):
                        piece[y - min(y_numbers) + 1][
                            x - min(x_numbers) + 1] = shapemap[y][x]
        if x_numbers and y_numbers:
            for y in range(len(piece)):
                for x in range(len(piece[0])):
                    if piece[y][x] == '+':
                        if is_neighborhood(piece, x, y, '|') != is_neighborhood(
                                piece, x, y, '-'):
                            if is_neighborhood(piece, x, y, '-'):
                                piece[y][x] = '-'
                            else:
                                piece[y][x] = '|'
            for y in range(len(piece)):
                deleted_symbols_counter = 0
                while piece[y][-1] == ' ':
                    del piece[y][-1]
                    deleted_symbols_counter += 1
                # piece[y] += '*' * deleted_symbols_counter
            result.append('\n'.join([''.join(string) for string in piece]))

            for y in range(min(y_numbers) - 1, max(y_numbers) + 2):
                for x in range(min(x_numbers) - 1, max(x_numbers) + 2):
                    if shapemap[y][x] == '!':
                        shapemap[y][x] = '&'

    result.sort()
    return result


if __name__ == "__main__":
    shape = '\n'.join(["+------------+",
                       "|            |",
                       "|            |",
                       "|            |",
                       "+------+-----+",
                       "|      |     |",
                       "|      |     |",
                       "+------+-----+"])
    # shape = '\n'.join(['+-------------------+--+',
    #                    '|                   |  |',
    #                    '|                   |  |',
    #                    '|  +----------------+  |',
    #                    '|  |                   |',
    #                    '|  |                   |',
    #                    '+--+-------------------+'])
    # shape = '\n'.join(['           +-+           ',
    #                    '           | |           ',
    #                    '         +-+-+-+         ',
    #                    '         |     |         ',
    #                    '      +--+-----+--+      ',
    #                    '      |           |      ',
    #                    '   +--+-----------+--+   ',
    #                    '   |                 |   ',
    #                    '   +-----------------+   '])
    shape = '\n'.join(['+-----------------+',
                       '|                 |',
                       '|   +-------------+',
                       '|   |',
                       '|   |',
                       '|   |',
                       '|   +-------------+',
                       '|                 |',
                       '|                 |',
                       '+-----------------+',])
    shape = '\n'.join(['               ',
                       '  +-----+      ',
                       '  |     |      ',
                       '  |     |      ',
                       '  +-----+-----+',
                       '        |     |',
                       '        |     |',
                       '        +-----+',])
    shape = '\n'.join(['               ',
                       '  +-----------+',
                       '  |           |',
                       '  |           |',
                       '  |  +-----+  |',
                       '  |  |     |  |',
                       '  |  |     |  |',
                       '  +--+     +--+', ])
    solution = break_pieces(shape)

    print('\n'.join(solution))
