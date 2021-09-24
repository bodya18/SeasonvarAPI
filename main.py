from logging import DEBUG
from middleware.config import HOST, PORT
from flask import Flask

app = Flask(__name__)

from controllers.serials import route

app.register_blueprint(route)

if __name__ == '__main__':
    app.run(HOST, PORT, True)