people = ['Nick', 'Rick', 'Roger', 'Syd']
ages = [23, 24, 23, 21]

# for position, person in enumerate(people):
#     age = ages[position]
#     print(person, age)

# a more C way
for position, i in enumerate(people):
    age = ages[position]
    print(i, age)