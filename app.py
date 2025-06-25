from flask import Flask, render_template, jsonify
from datetime import datetime

app = Flask(__name__)

# Dummy logic — you can replace this later with real CO2 calculations
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_occupancy")
def get_occupancy():
    result = {
        "timestamp": datetime.now().strftime("%H:%M"),
        "people": 4  # Simulated number
    }
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
