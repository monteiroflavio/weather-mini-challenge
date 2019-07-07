from flask import Flask
from api.weather.routes import weather_api

app = Flask(__name__)
app.register_blueprint(weather_api)


def run():
    app.run(debug=True)