from flask import Flask, jsonify, render_template
from datetime import datetime, UTC
import os

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "DevSecOps Demo Application",
        "timestamp": datetime.now(UTC).isoformat()
    })


@app.route("/api/status")
def api_status():
    return jsonify({
        "application": "DevSecOps Demo",
        "version": "1.0.0",
        "environment": os.getenv("APP_ENV", "development"),
        "status": "running",
        "security": "protected"
    })


@app.route("/api/info")
def api_info():
    return jsonify({
        "name": "DevSecOps Demo Application",
        "technology": "Python Flask",
        "ci_cd": "GitHub Actions",
        "deployment": "AWS EC2",
        "security": [
            "Static Analysis",
            "SonarQube",
            "Snyk",
            "DAST"
        ]
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8080,
        debug=False
    )