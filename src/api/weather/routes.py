from flask import Blueprint
from api.weather.business import businessTest

weather_api = Blueprint('weather_api', __name__)

@weather_api.route('/weathers')
def test():
    return businessTest()