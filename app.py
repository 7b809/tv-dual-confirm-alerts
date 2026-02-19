from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from datetime import datetime
import os
from dotenv import load_dotenv
from telegram import send_telegram_message
from message_formatter import format_signal_message
from datetime import datetime, timezone


load_dotenv()
app = Flask(__name__)

# ==========================
# ENV VARIABLES
# ==========================
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("MONGO_DB", "tva")

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db["alerts"]

# ==========================
# HOME DASHBOARD
# ==========================
@app.route("/", methods=["GET"])
def dashboard():
    alerts = list(collection.find().sort("timestamp", -1).limit(100))
    return render_template("index.html", alerts=alerts)

# ==========================
# WEBHOOK
# ==========================
@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    if not data:
        return jsonify({"status": "no data"}), 400

        # Save to Mongo
    data["created_at"] = datetime.now(timezone.utc)
    collection.insert_one(data)

    # Send Telegram
    message = format_signal_message(data)
    send_telegram_message(message)

    return jsonify({"status": "success"}), 200
# ==========================
# API - GET ALERTS JSON
# ==========================
@app.route("/api/alerts", methods=["GET"])
def get_alerts():

    # Get start of today (UTC)
    now = datetime.now(timezone.utc)
    start_of_today = datetime(now.year, now.month, now.day, tzinfo=timezone.utc)

    alerts = list(
        collection.find(
            {"created_at": {"$gte": start_of_today}},
            {"_id": 0}
        )
        .sort("timestamp", -1)
        .limit(200)
    )

    return jsonify(alerts)


if __name__ == "__main__":
    app.run(debug=False)
