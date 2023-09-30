#!/usr/bin/python3
"""app for registering blueprint and starting flask"""

import os
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views

app = Flask(__name__)

# Register the blueprint
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Closes the storage on teardown."""
    storage.close()

@app_views.route('/api/v1/stats', methods=['GET'])
def get_stats():
    """Retrieves the count of each object by type"""
    stats = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
    }
    return jsonify(stats)

@app.errorhandler(404)
def not_found(error):
    """Custom 404 error handler."""
    return jsonify({"error": "Not found"}), 404

    if __name__ == "__main__":
        host = os.getenv("HBNB_API_HOST", "0.0.0.0")
        port = int(os.getenv("HBNB_API_PORT", 5000))
        app.run(host=host, port=port, threaded=True)
