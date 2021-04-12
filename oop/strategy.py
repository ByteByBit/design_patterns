import types


class Strategy:

    def __init__(self, f = None):

        self.name = 'Main type strategy.'
        if not f == None:
            self.execute = types.MethodType(f, self)

    def execute(self):

        print(self.name)


def execute_A(self):

    print(self.name + ' execute_A')


def execute_B(self):

    print(self.name + ' execute_B')


if __name__ == '__main__':
    
    strategy_main = Strategy()
    strategy_A = Strategy(execute_A)
    strategy_A.name = 'A type strategy.'
    strategy_B = Strategy(execute_B)
    strategy_B.name = 'B type strategy.'

    strategy_main.execute()
    strategy_A.execute()
    strategy_B.execute()