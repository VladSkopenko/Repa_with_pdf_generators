from countryinfo import CountryInfo

country = CountryInfo('Belarus')
languages = country.info().get('languages', [])
print(languages)