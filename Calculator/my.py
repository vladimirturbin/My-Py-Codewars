class Calculator(object):
    def evaluate(self, string):
        elements = string.split(' ')

        while '(' in elements:
            pass

        while '*' in elements:
            for i in range(len(elements)):
                if elements[i] == '*':
                    str(float(elements[i-1]) * float(elements[i+1]))
                    elements
        return elements


if __name__ == '__main__':
    calculator = Calculator()
    print(calculator.evaluate('1 + 1'))
