from flask import Blueprint, jsonify
from utils.exceptions.pagination_exception import InvalidPaginationParameterException
from api.cities.business import CityBusiness

cities_api = Blueprint('cities_api', __name__)
city_business = CityBusiness()

@cities_api.route('/cities')
def list():
    return jsonify(city_business.list())

@cities_api.errorhandler(InvalidPaginationParameterException)
def handle_invalid_pagination_parameter(error):
    return jsonify({'error': error.message}), 400