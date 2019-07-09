import json
import requests
from datetime import datetime
from flask import jsonify, request
from api.weathers.exceptions.city_not_found import CityNotFoundException
from api.weathers.exceptions.owm_api_call import OwmApiCallException
from configs.config import OWM_API_KEY, OWM_API_URL, HUMIDITY_THRESHOLD

class WeatherBusiness:
    def get_forecast_summary_for(self, city_id):
        owm_response = requests.get(OWM_API_URL, params={
            'id': city_id,
            'appid': OWM_API_KEY,
            'units': 'metric'
        })
        if owm_response.ok:
            return summarize_forecasts(json.loads(owm_response.content))
        elif owm_response.status_code == 404 :
            raise CityNotFoundException(city_id)
        else:
            raise OwmApiCallException()
        
def summarize_forecasts(owm_response):
    summary = []
    for forecast in owm_response['list']:
        summary = summarize_forecast(forecast, summary)
    return {'hint': summary_message(summary), 'days': summary}

def summarize_forecast(forecast, summary):
    forecast_date = datetime.fromtimestamp(forecast['dt']).strftime('%Y-%m-%d')
    if forecast_date not in [d['date'] for d in summary]:
        summary.append({
            'date': forecast_date
            , 'humidity': forecast['main']['humidity']
            , 'wind': forecast['wind']['speed']
            , 'temperature': forecast['main']['temp']
            , 'cloudiness': forecast['clouds']['all']
            , 'pressure': forecast['main']['pressure']
            , 'message': mount_message(forecast['main']['humidity'])})
    else:
        daily_summary = next(day for day in summary if day['date'] == forecast_date)
        daily_summary['humidity'] = (daily_summary['humidity'] + forecast['main']['humidity']) / 2
        daily_summary['wind'] = (daily_summary['wind'] + forecast['wind']['speed']) / 2
        daily_summary['temperature'] = (daily_summary['temperature'] + forecast['main']['temp']) / 2
        daily_summary['cloudiness'] = (daily_summary['cloudiness'] + forecast['clouds']['all']) / 2
        daily_summary['pressure'] = (daily_summary['pressure'] + forecast['main']['pressure']) / 2
        daily_summary['message'] = mount_message(daily_summary['humidity'])
        [daily_summary for d in summary if d['date'] == forecast_date]
    return summary

def summary_message(daily_processed_response):
    print([d['humidity'] > int(HUMIDITY_THRESHOLD) for d in daily_processed_response])
    return 'You should take an umbrella these days: '+', '.join([d['date'] for d in daily_processed_response if d['humidity'] > int(HUMIDITY_THRESHOLD)])

def mount_message(humidity):
    if humidity >= 0 and humidity < 10:
        return 'No chance of rain'
    elif humidity >= 10 and humidity < 20:
        return 'Slight chance of isolated rains'
    elif humidity >= 20 and humidity < 30:
        return 'Small chance of rain'
    elif humidity >= 30 and humidity < 60:
        return 'Considerable chance of scattered rain'
    elif humidity >= 50 and humidity < 80:
        return 'Scattered rain'
    else:
        return 'Rainy (strong or weak)'