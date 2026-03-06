from flask import Flask, render_template, request, jsonify
from utils.json_processor import refine_json

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    data = request.json
    result = refine_json(data)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
