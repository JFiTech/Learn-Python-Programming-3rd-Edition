people = ['Nick', 'Rick', 'Roger', 'Syd']
ages = [23, 24, 23, 21]
instruments = ['Drums', 'Keyboards', 'Bass', 'Guitar']

for data in zip(people, ages, instruments):
    person, age, instrument = data
    print(person, age, instrument)

# A more C way
# for data in zip(people, ages, instruments):
#     i, j, k = data
#     print(i, j, k)