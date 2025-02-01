class City:
    def __init__(self, city_name, region_name, country_name, population, zip_code, area_code):
        self.city_name = city_name
        self.region_name = region_name
        self.country_name = country_name
        self.population = population
        self.zip_code = zip_code
        self.area_code = area_code

    def full_address(self):
        print(f"{self.city_name}, {self.region_name}, {self.country_name}, {self.zip_code}, {self.area_code}")

Copake = City(city_name="Copake", region_name="New York", country_name="USA", population=3000, zip_code=12516, area_code=518)
Copake.full_address()

