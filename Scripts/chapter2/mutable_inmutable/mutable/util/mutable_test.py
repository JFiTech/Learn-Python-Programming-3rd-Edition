class Person:
    def __init__(self, age):
        self.age = age
        
fab = Person(age=42)

print('fab.age', '\n', fab.age, '\n')
print('id(fab)', '\n', id(fab), '\n')
print('id(fab.age)', '\n', id(fab.age), '\n')

fab.age = 25
print('id(fab)', '\n', id(fab), '\n')
print('id(fab.age)', '\n', id(fab.age), '\n')
print('fab.age', '\n', fab.age, '\n')