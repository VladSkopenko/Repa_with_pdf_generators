from countryinfo import CountryInfo

country = CountryInfo("United Kingdom")
languages = country.info().get("languages", [])
print(languages)
