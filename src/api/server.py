from flask import Flask, jsonify
from api.cities.routes import cities_api
from api.weathers.routes import weather_api

app = Flask(__name__)
app.register_blueprint(weather_api)
app.register_blueprint(cities_api)

@app.errorhandler(Exception) # cuz sometimes
def handle_generic_exception(error):
    return jsonify({'error': 'Some error occurred while processing your request'}), 500

def run():
    app.run(debug=True)