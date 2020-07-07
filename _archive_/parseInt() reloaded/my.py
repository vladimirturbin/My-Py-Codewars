def parse_int(string):
    numbers = string.replace('-', ' ').replace(' and ', ' ').split()

    return process(numbers)


def process(numbers):
    numerals = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        'ten': 10,
        'eleven': 11,
        'twelve': 12,
        'thirteen': 13,
        'fourteen': 14,
        'fifteen': 15,
        'sixteen': 16,
        'seventeen': 17,
        'eighteen': 18,
        'nineteen': 19,
        'twenty': 20,
        'thirty': 30,
        'forty': 40,
        'fifty': 50,
        'sixty': 60,
        'seventy': 70,
        'eighty': 80,
        'ninety': 90,
        'hundred': 100,
        'thousand': 1000,
        'million': 1000000,
    }
    multipliers = ['million', 'thousand', 'hundred']

    if not numbers:
        return 0

    for multiplier in multipliers:
        if multiplier in numbers:
            return process(numbers[:numbers.index(multiplier)])\
                   * numerals[multiplier]\
                   + process(numbers[numbers.index(multiplier)+1:])
    result = 0
    for word in numbers:
        print(word)
        result += numerals[word]
    
    return result


if __name__ == '__main__':
    print(parse_int('two hundred forty-six'))
