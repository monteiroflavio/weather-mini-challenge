from flask import Flask
from .weather.routes import weather

app = Flask(__name__)
app.register_blueprint(weather)