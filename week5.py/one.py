class Country:
    
    def __init__(self, name, capital, population, area):
        self.name = name
        self.capital = capital
        self.population = population
        self.area = area  # in km²
    
    def get_info(self):
        return f"{self.name} | Capital: {self.capital} | Population: {self.population:,} | Area: {self.area:,} km²"
    
    def population_density(self):
        density = self.population / self.area
        return f"Population density: {density:.1f} people/km²"


class Kenya(Country):
    
    def __init__(self):
        # Initialize with Kenya's specific data
        super().__init__("Kenya", "Nairobi", 55000000, 580367)
        self.official_languages = ["Swahili", "English"]
        self.currency = "Kenyan Shilling"
        self.independence_year = 1963
    
    def greet(self):
        return "Karibu Kenya! 🇰🇪"
    
    def get_info(self):  # Method overriding (polymorphism)
        base_info = super().get_info()
        return f"{base_info} | Languages: {', '.join(self.official_languages)}"


class KenyaCounty(Kenya):
    
    def __init__(self, county_name, county_population, main_town):
        super().__init__()  # Initialize parent class
        self.county_name = county_name
        self.county_population = county_population
        self.main_town = main_town
    
    def get_county_info(self):
    
        return f"{self.county_name} County | Main town: {self.main_town} | Population: {self.county_population:,}"


# Demonstration
if __name__ == "__main__":
    print("🇰🇪 KENYA COUNTRY INFORMATION 🇰🇪")
    
    # Create Kenya object
    kenya = Kenya()
    print(kenya.greet())
    print(kenya.get_info())
    print(kenya.population_density())
    
    print("\n COUNTY INFORMATION")
    
    # Create county objects (inheritance)
    nairobi_county = KenyaCounty("Nairobi", 500000, "Nairobi City")
    mombasa_county = KenyaCounty("Mombasa", 200000, "Mombasa Town")
    kisumu_county = KenyaCounty("Kisumu", 150000, "Kisumu City")
    
    counties = [nairobi_county, mombasa_county, kisumu_county]
    
    for county in counties:
        print(county.get_county_info())
        # Inherited method from grandparent class
        print(f"Country: {county.name}")  
