from flask import Blueprint

weather = Blueprint('weather', __name__)

@weather.route('/weathers')
def test():
    return {'message': 'test'}