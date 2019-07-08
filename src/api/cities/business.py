import json
from flask import Flask, request, jsonify, abort

class CityBusiness:
    cities = json.load(open('city.list.json', 'r'))
    def list(self):
        return jsonify(get_paginated_list(
            filter_city_result([city for city in self.cities if request.args.get('name', '').lower() in city["name"].lower()]),
            '/cities',
            start=request.args.get('start', 1),
            limit=request.args.get('limit', 20),
            name=request.args.get('name', '')
        ))

def filter_city_result(results):
    return [{key: result[key] for key in result if key not in ['country', 'coord']} for result in results]

def get_paginated_list(results, url, start, limit, name):
    start = int(start)
    limit = int(limit)
    count = len(results)
    if count < start or limit < 0:
        abort(404)
    obj = {}
    obj['start'] = start
    obj['limit'] = limit
    obj['count'] = count
    if start == 1:
        obj['previous'] = ''
    else:
        start_copy = max(1, start - limit)
        limit_copy = start - 1
        obj['previous'] = url + '?start=%d&limit=%d&name=%s' % (start_copy, limit_copy, name)
    if start + limit > count:
        obj['next'] = ''
    else:
        start_copy = start + limit
        obj['next'] = url + '?start=%d&limit=%d&name=%s' % (start_copy, limit, name)
    obj['results'] = results[(start - 1):(start - 1 + limit)]
    return obj