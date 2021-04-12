import abc


class HumanState(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def current_state(self):
        pass


class Sleep(HumanState):

    def current_state(self):

        return "Sleeping."


class Work(HumanState):

    def current_state(self):

        return "Working."


class Exercise(HumanState):

    def current_state(self):

        return "Exercising."


class Human(HumanState):

    def __init__(self, state):

        self.state = state

    def set_state(self, state):
        
        self.state = state

    def current_state(self):

        return self.state.current_state()


if __name__ == '__main__':
    
    human = Human(Sleep())
    print(human.current_state())

    human.set_state(Work())
    print(human.current_state())

    human.set_state(Exercise())
    print(human.current_state())