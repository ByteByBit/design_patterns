class Foam:

    height = None


class Strength:

    strength = None


class Cup:

    cup_type = None


class Sugar:

    amount = None


class Milk:

    amount = None
    temp = None


class Coffee:

    def __init__(self):

        self.__foam = None
        self.__strength = None
        self.__cup = None
        self.__sugar = None
        self.__milk = None

    def set_foam(self, foam):

        self.__foam = foam
    
    def set_strength(self, strength):

        self.__strength = strength
        
    def set_cup(self, cup):

        self.__cup = cup

    def set_sugar(self, sugar):

        self.__sugar = sugar

    def set_milk(self, milk):

        self.__milk = milk

    def __str__(self):

        return 'Foam: {}, Strength: {}, Cup: {}, Sugar: {}, ' \
            'Milk amount: {}, temperature: {}'.format(\
            self.__foam.height, self.__strength.strength,\
            self.__cup.cup_type, self.__sugar.amount, \
            self.__milk.amount, self.__milk.temp)


class Builder:

    def get_foam_height(self): pass

    def get_strength(self): pass

    def get_cup_type(self): pass

    def get_sugar_amount(self): pass

    def get_milk(self): pass


class LatteBuilder(Builder):

    #@override
    def get_foam_height(self):

        foam = Foam()
        foam.height = 4
        return foam
    
    #@override
    def get_strength(self):

        strength = Strength()
        strength.strength = 7
        return strength
    
    #@override
    def get_cup_type(self):

        cup = Cup()
        cup.cup_type = 2
        return cup
    
    #@override
    def get_sugar_amount(self):
        
        sugar = Sugar()
        sugar.amount = 1
        return sugar

    #@override
    def get_milk(self):

        milk = Milk()
        milk.amount = 1
        milk.temp = 60
        return milk


class Barista:
    __builder = None

    def set_builder(self, builder):
        self.__builder = builder

    def get_coffee(self):

        coffee = Coffee()

        foam = self.__builder.get_foam_height()
        coffee.set_foam(foam)

        strength = self.__builder.get_strength()
        coffee.set_strength(strength)

        cup = self.__builder.get_cup_type()
        coffee.set_cup(cup)

        sugar = self.__builder.get_sugar_amount()
        coffee.set_sugar(sugar)

        milk = self.__builder.get_milk()
        coffee.set_milk(milk)

        return coffee
        
        
if __name__ == "__main__":

    coffee_builder = LatteBuilder()

    barista = Barista()

    barista.set_builder(coffee_builder)

    latte = barista.get_coffee()

    print(latte)