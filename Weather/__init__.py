from flask import Flask

app = Flask(__name__)

from Weather import routes
