from flask import Blueprint
from api.weathers.business import WeatherBusiness

weather_business = WeatherBusiness()

weather_api = Blueprint('weather_api', __name__)

@weather_api.route('/cities/<city_id>/weathers')
def test(city_id):
    return weather_business.businessTest(city_id)