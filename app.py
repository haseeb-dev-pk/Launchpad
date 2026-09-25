import os
from datetime import datetime, timezone

from flask import Flask, jsonify, render_template


app = Flask(__name__)
app.config["APP_VERSION"] = os.getenv("APP_VERSION", "1.0.0")


@app.get("/")
def home():
	return render_template(
		"index.html",
		app_version=app.config["APP_VERSION"],
		generated_at=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
	)


@app.get("/health")
def health():
	return jsonify({"status": "ok", "version": app.config["APP_VERSION"]})


@app.get("/ready")
def ready():
	return jsonify({"status": "ready"})


if __name__ == "__main__":
	app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")))
