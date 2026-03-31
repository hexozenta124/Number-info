from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "success",
        "message": "API is running"
    })

@app.route("/lookup", methods=["GET"])
def lookup():
    number = request.args.get("number", "")

    if not number.isdigit() or len(number) != 10:
        return jsonify({
            "status": "error",
            "message": "Invalid number"
        }), 400

    return jsonify({
        "status": "success",
        "number": number,
        "country": "India",
        "carrier": "Demo Network",
        "location": "West Bengal",
        "valid": True
    })
