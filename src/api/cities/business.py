import json
from flask import Flask, request, jsonify, abort
from utils.pagination_utils import PaginationUtils

pagination_utils = PaginationUtils()

class CityBusiness:
    cities = json.load(open('city.list.json', 'r'))
    def list(self):
        return pagination_utils.get_paginated_list(
            filter_city_result([city for city in self.cities if request.args.get('name', '').lower() in city["name"].lower()]),
            '/cities',
            start=request.args.get('start', 1),
            limit=request.args.get('limit', 20),
            name=request.args.get('name', '')
        )

def filter_city_result(results):
    return [{key: result[key] for key in result if key not in ['country', 'coord']} for result in results]