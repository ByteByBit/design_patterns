import copy


class Prototype:

    _type = None
    _value = None

    def clone(self): pass

    def get_type(self):

        return self._type

    def get_value(self):

        return self._value


class TypeA(Prototype):

    def __init__(self, val):

        self._type = 'A'
        self._value = val

    def clone(self):

        return copy.copy(self) 


class TypeB(Prototype):

    def __init__(self, val):

        self._type = 'B'
        self._value = val

    def clone(self):

        return copy.copy(self) 


class Factory:

    __typeAValue1 = None
    __typeAValue2 = None
    __typeBValue1 = None
    __typeBValue2 = None

    @staticmethod
    def init():

        Factory.__typeAValue1  = TypeA(1)
        Factory.__typeAValue2  = TypeA(2)
        Factory.__typeBValue1  = TypeB(1)
        Factory.__typeBValue2  = TypeB(2)

    @staticmethod
    def get_type_a_val_1():

        return Factory.__typeAValue1.clone()

    @staticmethod
    def get_type_a_val_2():

        return Factory.__typeAValue2.clone()

    @staticmethod
    def get_type_b_val_1():

        return Factory.__typeBValue1.clone()

    @staticmethod
    def get_type_b_val_2():

        return Factory.__typeBValue2.clone()


if __name__ == '__main__':

    Factory.init()

    instance = Factory.get_type_a_val_1()
    print('Type: {}, Value: {}'.format(instance.get_type(), instance.get_value()))

    instance = Factory.get_type_a_val_2()
    print('Type: {}, Value: {}'.format(instance.get_type(), instance.get_value()))

    instance = Factory.get_type_b_val_1()
    print('Type: {}, Value: {}'.format(instance.get_type(), instance.get_value()))

    instance = Factory.get_type_b_val_2()
    print('Type: {}, Value: {}'.format(instance.get_type(), instance.get_value()))