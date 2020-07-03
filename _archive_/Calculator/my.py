class Calculator(object):
    def evaluate(self, string):
        return float(self.calculate(string.split(' '))[0])

    def calculate(self, elements):
        while '(' in elements:
            start = elements.index('(')
            o = 0
            c = 0
            for i in range(start, len(elements)):
                # print(elements, i, elements[i], 'o =', o, ' c =', c)
                if elements[i] == '(':
                    o += 1
                if elements[i] == ')':
                    c += 1
                if o == c and o != 0:
                    end = i
                    break
            # print('start')
            # print('start =', start, ' end =', end)
            # print(elements)
            # print(elements[:start])
            # print(elements[start + 1:end])
            # print(elements[end + 1:])
            # print('end')
            elements = elements[:start]\
                       + self.calculate(elements[start + 1:end])\
                       + elements[end + 1:]

        while '*' in elements or '/' in elements:
            try:
                x = elements.index('*')
            except ValueError:
                x = -1
            try:
                y = elements.index('/')
            except ValueError:
                y = -1
            if x > 0 and y > 0:
                ind = min(x, y)
            else:
                ind = max(x, y)
            if elements[ind] == '*':
                a = str(
                    float(elements.pop(ind - 1)) * float(elements.pop(ind)))
            else:
                a = str(
                    float(elements.pop(ind - 1)) / float(elements.pop(ind)))
            elements[ind-1] = a

        while '+' in elements or '-' in elements:
            try:
                x = elements.index('+')
            except ValueError:
                x = -1
            try:
                y = elements.index('-')
            except ValueError:
                y = -1
            if x > 0 and y > 0:
                ind = min(x, y)
            else:
                ind = max(x, y)
            if elements[ind] == '+':
                a = str(
                    float(elements.pop(ind - 1)) + float(elements.pop(ind)))
            else:
                a = str(
                    float(elements.pop(ind - 1)) - float(elements.pop(ind)))
            elements[ind-1] = a

        return elements


if __name__ == '__main__':
    calculator = Calculator()
    print(calculator.evaluate('( 1 + 2 ) + ( 3 + 4 )'))
