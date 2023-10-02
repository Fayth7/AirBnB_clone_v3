#!/usr/bin/python3
'''
    flask routes
    routes:
        /status:    display "status":"OK"
        /stats:     dispaly total for all classes
'''

from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def return_status():
    """ Response for a successful fetch """
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def get_stats():
    """ Returns number of objects of each type """
    objects = {
            'amenities': Amenity,
            'cities': City,
            'places': Place,
            'reviews': Review,
            'states': State,
            'users': User
            }
    for key, value in objects.items():
        objects[key] = storage.count(value)
    return jsonify(objects)
