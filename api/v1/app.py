#!/usr/bin/python3
"""app for registering blueprint and starting flask"""

from flask import Flask, make_response, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"api/v1/*": {"origin": "*"}})
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Closes the storage on teardown."""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """Custom 404 error handler."""
    return jsonify({"error": "Not found"}), 404

    if __name__ == "__main__":
        port = int(os.getenv("HBNB_API_PORT", 5000))
        host = os.getenv("HBNB_API_HOST", "0.0.0.0")
        app.run(host=host, port=port, threaded=True)
