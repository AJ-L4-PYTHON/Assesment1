rivers = {
    'amazon': 'south america',
    'nile': 'south africa',
    'ganges': 'india and bangladesh',
    'mississippi': 'north america',
    'thames': 'southern england',
    }

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\n rivers that are included in this data:")
for river in rivers.keys():
    print(f"- {river.title()}")

print("\n countries that are included in this data:")
for country in rivers.values():
    print(f"- {country.title()}")