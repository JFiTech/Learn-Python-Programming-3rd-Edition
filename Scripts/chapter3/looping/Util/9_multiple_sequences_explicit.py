people = ['Nick', 'Rick', 'Roger', 'Syd']
ages = [23, 24, 23, 21]
instruments = ['Drums', 'Keyboards', 'Bass', 'Guitar']

# for person, age, instrument in zip(people, ages, instruments):
#     print(person, age, instrument)

# A more C way
for i, j, k in zip(people, ages, instruments):
    print(i, j, k)