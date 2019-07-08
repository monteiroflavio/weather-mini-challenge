from flask import Flask
from api.weathers.routes import weather_api
from api.cities.routes import cities_api

app = Flask(__name__)
app.register_blueprint(weather_api)
app.register_blueprint(cities_api)

def run():
    app.run(debug=True)