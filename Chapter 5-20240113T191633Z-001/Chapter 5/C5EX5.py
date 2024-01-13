pets = []

pet = {
    'animal': 'cat',
    'name': 'nogu',
    'owner': 'josh',
    'weight': 25,
    'eats': 'boxes',
}
pets.append(pet)

pet = {
    'animal': 'bird',
    'name': 'tweety',
    'owner': 'cameron',
    'weight': 5,
    'eats': 'worms',
}
pets.append(pet)

pet = {
    'animal': 'dog',
    'name': 'dotty',
    'owner': 'sheena',
    'weight': 34,
    'eats': 'socks',
}
pets.append(pet)

for pet in pets:
    print(f"\n Well, here's everything I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")