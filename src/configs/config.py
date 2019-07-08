import os
from dotenv import load_dotenv

load_dotenv()

OWM_API_KEY=os.getenv('OWM_API_KEY')
OWM_API_URL=os.getenv('OWM_API_URL')
HUMIDITY_THRESHOLD=os.getenv('HUMIDITY_THRESHOLD')