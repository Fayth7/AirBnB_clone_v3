#!/usr/bin/python3
'''
    flask routes
    routes:
        /status:    display "status":"OK"
        /stats:     dispaly total for all classes
'''
from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """Retrieve the number of objects by type."""
    return jsonify({'status': 'OK'})
