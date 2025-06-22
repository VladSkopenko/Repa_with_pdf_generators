# from countryinfo import CountryInfo
#
# country = CountryInfo('Vatican')
# languages = country.info().get('languages', [])
# print(languages)


from countryinfo import CountryInfo
import pycountry

no_lang_countries = []

for country in pycountry.countries:
    try:
        langs = CountryInfo(country.name).info().get('languages', [])
        if not langs:
            no_lang_countries.append(country.alpha_2)
    except:
        no_lang_countries.append(country.alpha_2)

print(no_lang_countries)