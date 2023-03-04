from flask import Flask
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app) # confiture CORS and csrf protection

modules = next(os.walk(app.root_path + '/modules'))[1]
for module in modules:
    curr_module = __import__('modules.' + module + '.routes', fromlist='init_routes')
    curr_module.init_routes(app)