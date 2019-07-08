class CityNotFoundException(Exception):
    def __init__(self, city_id):
        Exception.__init__(self)
        self.message = 'City {0} was not found'.format(city_id)