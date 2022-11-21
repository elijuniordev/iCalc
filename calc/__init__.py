from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = '75f14ae2c81256f8078da27b2b0bf9fd'

from calc import routes