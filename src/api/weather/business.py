from api.config import OWM_API_KEY, OWM_API_URL

def businessTest():
    print(OWM_API_KEY, OWM_API_URL)
    return {'message': 'test'}