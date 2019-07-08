class OwmApiCallException(Exception):
    def __init__(self):
        Exception.__init__(self)
        self.message = 'Could\'t request OWM api with success'