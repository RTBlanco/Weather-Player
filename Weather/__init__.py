from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'TEST'

from Weather import routes
