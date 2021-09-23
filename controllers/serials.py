import json
from flask import Blueprint

route = Blueprint('route', __name__)

@route.route('/api/getRandomSerials/<int:count>', methods=["GET"])
def randomSerials(count):
    data = json.dumps({"data": count})
    print(data)
    data = {"data": count}
    print(data)
    return json.dumps({"data": count})

