from flask import Blueprint, jsonify
from api.weathers.business import WeatherBusiness
from api.weathers.exceptions.city_not_found import CityNotFoundException
from api.weathers.exceptions.owm_api_call import OwmApiCallException

weather_business = WeatherBusiness()

weather_api = Blueprint('weather_api', __name__)

@weather_api.route('/cities/<city_id>/weathers')
def test(city_id):
    return jsonify(weather_business.get_forecast_summary_for(city_id))

@weather_api.errorhandler(CityNotFoundException)
def handle_city_not_found(error):
    return jsonify({'error': error.message}), 404

@weather_api.errorhandler(OwmApiCallException)
def handle_owm_api_call_error(error):
    return jsonify({'error': error.message}), 500