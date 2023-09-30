from flask import Flask, jsonify, make_response
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)

# Register the blueprint
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Closes the storage on teardown."""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """Custom 404 error handler."""
    return make_response(jsonify({"error": "Not found"}), 404)

if __name__ == "__main__":
    host = getenv("HBNB_API_HOST", default="0.0.0.0")
    port = int(getenv("HBNB_API_PORT", default=5000))
    app.run(host=host, port=port, threaded=True)
