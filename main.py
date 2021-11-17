from middleware.config import HOST, PORT
from flask import Flask, send_file  

app = Flask(__name__)

from controllers.serials import serials_route
from controllers.seasons import seasons_route
from controllers.series import series_route

app.register_blueprint(seasons_route)
app.register_blueprint(serials_route)
app.register_blueprint(series_route)

@app.route('/', methods=["GET"])
def Main():
    return send_file('README.md')

if __name__ == '__main__':
    app.run(HOST, PORT, True)