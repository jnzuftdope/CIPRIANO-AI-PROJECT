from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# -----------------------------------
# DATA
# -----------------------------------

queue_data = {
    "Business Office": 0,
    "Registrar's Office": 0
}


# -----------------------------------
# HOME
# -----------------------------------

@app.route("/")
def home():
    return render_template("index.html")


# -----------------------------------
# QUEUE API
# -----------------------------------

@app.route("/api/queue", methods=["GET"])
def get_queue():

    return jsonify({
        "business": queue_data["Business Office"],
        "registrar": queue_data["Registrar's Office"]
    })


@app.route("/api/queue", methods=["POST"])
def create_queue():

    data = request.get_json()

    office = data.get("office")

    if office not in queue_data:
        return jsonify({
            "success": False,
            "message": "Invalid office."
        }), 400

    queue_data[office] += 1

    prefix = "BO" if office == "Business Office" else "RO"

    queue_number = f"{prefix}-{queue_data[office]:03d}"

    return jsonify({
        "success": True,
        "queue_number": queue_number,
        "office": office
    })


# -----------------------------------
# SERVICE REQUEST
# -----------------------------------

@app.route("/api/request", methods=["POST"])
def service_request():

    data = request.get_json()

    name = data.get("name")
    service = data.get("service")
    office = data.get("office")

    if not name or not service or not office:
        return jsonify({
            "success": False,
            "message": "Please complete all fields."
        }), 400

    return jsonify({
        "success": True,
        "message": "Service request submitted successfully."
    })


# -----------------------------------
# RUN
# -----------------------------------

if __name__ == "__main__":
    app.run(debug=True)