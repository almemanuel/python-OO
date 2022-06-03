from person import Person

person1 = Person('John', 36, True)
person2 = Person('Chandler', 30, True)

person2.set_is_eating(True)
person1.eat('apple')
person2.eat('pizza')
