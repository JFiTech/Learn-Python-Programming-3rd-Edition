people = ['Nick', 'Rick', 'Roger', 'Syd']
ages = [23, 24, 23, 21]

# for person, age in zip(people, ages):
#     print(person, age)

# A more C way
for i, age in zip(people, ages):
    print(i, age)