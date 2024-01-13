def describe_city(city, country='south korea'):
    """Describe a city."""
    msg = f"{city.title()} is in {country.title()}."
    print(msg)

describe_city('seoul')
describe_city('new jersey', 'usa')
describe_city('busan')