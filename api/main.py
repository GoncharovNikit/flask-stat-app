from flask import Flask
from flask_cors import CORS
import os, logging, psycopg2

logging.basicConfig(filename='logs/app.log', level=logging.ERROR)
app = Flask(__name__)
CORS(app) # TODO: configure CORS and csrf protection

def get_db_connection():
    return psycopg2.connect(
        host=os.environ.get('DB_HOST'),
        database=os.environ.get('DB_NAME'),
        user=os.environ.get('DB_USER'),
        password=os.environ.get('DB_PASSW')
    )

modules = next(os.walk('modules'))[1]
for module in modules:
    try:
        curr_module = __import__('modules.' + module + '.routes', fromlist='init_routes')
        curr_module.init_routes(app)
    except ImportError:
        app.logger.error('"%s" module doesn\'t have "routes.py"', module)