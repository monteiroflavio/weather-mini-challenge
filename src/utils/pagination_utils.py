from utils.exceptions.pagination_exception import InvalidPaginationParameterException

class PaginationUtils:
    def get_paginated_list(self, results, url, start, limit, name):
        start = int(start)
        limit = int(limit)
        count = len(results)
        if count < start or limit < 0:
            raise InvalidPaginationParameterException(start, limit)
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