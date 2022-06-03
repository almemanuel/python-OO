from datetime import datetime

class Person:
    # class variable
    year = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, name, age, is_talking = False):
        # instace variable
        self.name = name
        self.age = age
        self.is_talking = is_talking
        self.is_eating = False
        self.talk()


    def set_is_eating(self, is_eating):
        self.is_eating = is_eating


    def set_is_talking(self, is_talking):
        self.is_talking = is_talking


    def get_birth_year(self):
        return self.year - self.age


    def eat(self, food):
        if self.is_eating is False:
            self.is_eating = True
        print(f'{self.name} is eating a(n) {food}')


    def talk(self):
        if self.is_eating:
            print(f'{self.name} cant talking now.')
            return
        elif self.is_talking is False:
            self.is_talking = True
        print(f'{self.name} is talking')


    def __str__(self):
        return f'{self.name} has {self.age} yo.'