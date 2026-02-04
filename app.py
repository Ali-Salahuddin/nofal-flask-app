import os
import time
import random
from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

# Track app start time for uptime calculation
START_TIME = time.time()

# Read environment variables
ENV_NAME = os.getenv("ENV_NAME", "development")
FAIL_LIVE = os.getenv("FAIL_LIVE", "false").lower() == "true"

# Main HTML page template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Zynex Solutions - DevOps Course</title>
</head>
<body>
    <h1>Zynex Solutions - DevOps Course</h1>
    <p>Welcome to the Fake Production Health-Check Service demo.</p>
    <h2>Available Endpoints:</h2>
    <ul>
        <li><a href="/health">/health</a> - Returns JSON with status, environment, and uptime.</li>
        <li><a href="/ready">/ready</a> - Returns readiness status (10% chance to be "not ready").</li>
        <li><a href="/live">/live</a> - Returns liveness status (can fail if FAIL_LIVE=true).</li>
    </ul>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route("/health")
def health():
    uptime_seconds = int(time.time() - START_TIME)
    response = {
        "status": "healthy",
        "environment": ENV_NAME,
        "uptime_seconds": uptime_seconds
    }
    return jsonify(response), 200

@app.route("/ready")
def ready():
    # 10% chance to return "not ready"
    if random.random() < 0.1:
        return jsonify({"status": "not ready"}), 503
    return jsonify({"status": "ready"}), 200

@app.route("/live")
def live():
    if FAIL_LIVE:
        return jsonify({"status": "dead"}), 500
    return jsonify({"status": "alive"}), 200
