def is_interesting(number, awesome_phrases):
    if interesting(number, awesome_phrases):
        return 2
    if interesting(number + 1, awesome_phrases) \
            or interesting(number + 2, awesome_phrases):
        return 1
    return 0


def interesting(number, awesome_phrases):
    number_str = str(number)
    number_list = [int(i) for i in number_str]

    if number < 100:
        return False

    if number in awesome_phrases:
        return True

    if str(number) == number_str[::-1]:
        return True

    result = True
    for i in range(len(number_list) - 1):
        if number_list[i] != (number_list[i + 1] + 1) % 10:
            result = False
    if 0 in number_list[:-1]:
        result = False
    if result:
        return True

    result = True
    for i in range(len(number_list) - 1):
        if number_list[i + 1] != (number_list[i] + 1) % 10:
            result = False
    if 0 in number_list[:-1]:
        result = False
    if result:
        return True

    if len(set(number_list)) == 1:
        return True

    if set(number_list[1:]) == {0}:
        return True

    return False


if __name__ == '__main__':
    print(is_interesting(109, [31337]))
