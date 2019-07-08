class InvalidPaginationParameterException(Exception):
    def __init__(self, start, limit):
        Exception.__init__(self)
        self.message = 'One or both pagination parameters are invalid: Start = {0}, Limit = {1}'.format(start, limit)