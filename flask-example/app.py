from flask import Flask, request, jsonify
from werkzeug import run_simple

from prefix_manager import manage_prefixes

app = Flask(__name__)


@app.route("/predict")
def predict():
    name = request.args.get("name", "")
    return jsonify({"predicted_first_letter": name[:1].lower()})


app = manage_prefixes(app)

if __name__ == "__main__":
    run_simple("0", 8000, use_reloader=True, application=app)
