"""
crow7
2021年07月04日
"""


def city(city_name, country_name, population):
    name = str(city_name).title() + ',' + \
           str(country_name).title() + '-' + str(population)
    return name