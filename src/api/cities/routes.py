from flask import Blueprint
from api.cities.business import CityBusiness

cities_api = Blueprint('cities_api', __name__)
city_business = CityBusiness()

@cities_api.route('/cities')
def list():
    return city_business.list()