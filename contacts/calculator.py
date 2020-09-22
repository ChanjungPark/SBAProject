class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sum(self):
        return self.num1 + self.num2 


if __name__ == '__main__':
    calc = Calculator(6, 2)  # num1 = 6, num2 = 2
    sumResult = calc.sum()
    print(f'덧셈결과 {sumResult}')

    # 덧셈결과 : 8
    # 뺄셈결과 : 4
    # 곱셈결과 : 12
    # 나눗셈결과 : 3