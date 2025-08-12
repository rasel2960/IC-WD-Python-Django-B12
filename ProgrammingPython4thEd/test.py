from person import Person
from manager import Manager

bob = Person('Bob Smith', 42, 10000, 'software')
sue = Person('Sue Jones', 45, 20000, 'hardware')
tom = Manager('Tom Doe', age=55, pay=30000)
db = [bob, sue, tom]

for people in db:
    people.giveRaise(.10)

for people in db:
    print(people.lastName(), '=>', people.pay)
