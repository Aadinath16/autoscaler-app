from flask import Flask, jsonify, render_template
import time
import math

app = Flask(__name__, template_folder="../frontend")

@app.route("/")
def home():
    return render_template("index.html")


# Normal endpoint
@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


# Endpoint to trigger CPU load -> HPA
@app.route("/cpu-load")
def cpu_load():
    result = 0
    for i in range(10**7):
        result += math.sqrt(i)

    return jsonify({
        "message": "CPU load executed",
        "result": result
    })


# Endpoint to trigger memory load -> VPA
@app.route("/memory-load")
def memory_load():
    data = []
    for i in range(10000000):
        data.append(i)

    return jsonify({
        "message": "Memory load executed",
        "items_created": len(data)
    })


# Endpoint to simulate long request
@app.route("/long-request")
def long_request():
    time.sleep(10)
    return jsonify({
        "message": "Long request completed"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)