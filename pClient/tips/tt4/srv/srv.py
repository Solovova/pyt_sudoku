from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/get", methods=["GET"])
def starting_url_get():
    return jsonify({"data":{"name": "Rolando", "job": "test"}})

@app.route("/post", methods=["POST"])
def starting_url_post():
    json_data = request.json
    a_value = json_data["a_key"]
    job = "JSON value sent: " + a_value
    return jsonify({"name": "Rolando", "job": job})

# app.run(host="0.0.0.0", port=8080)
app.run()