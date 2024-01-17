class Solution:
    def __init__(self):
        self.stack = []


    def evalRPN(self, tokens: List[str]) -> int:
        for elem in tokens:
            try:
                number = int(elem)
                self.stack.append(number)
            except ValueError:
                if elem == '+':
                    self.stack.append(self.add(self.stack.pop(), self.stack.pop()))
                elif elem == '-':
                    self.stack.append(self.sub(self.stack.pop(), self.stack.pop()))
                elif elem == '/':
                    self.stack.append(self.div(self.stack.pop(), self.stack.pop()))
                elif elem == '*':
                    self.stack.append(self.mul(self.stack.pop(), self.stack.pop()))

        return self.stack[-1]
        

        




    def add(self, num1: int, num2: int)-> int:
        print(num2, "+", num1, "=", num2 + num1)
        return num2 + num1
    def div(self, num1: int, num2: int)-> int:
        print (num2, "/", num1, "=", math.trunc(num2 / num1))
        return math.trunc(num2 / num1)
    def sub(self, num1: int, num2: int)-> int:
        print(num2, "-", num1, "=", num2 - num1)
        return num2 - num1
    def mul(self, num1: int, num2: int)-> int:
        print(num1, "*", num2, "=", num1 * num2)
        return num1 * num2
