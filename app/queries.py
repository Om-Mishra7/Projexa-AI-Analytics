from flask import Blueprint, jsonify
from app.db import telemetry_collection

query_bp = Blueprint("query", __name__)


@query_bp.route("/api/v1/events/recent", methods=["GET"])
def get_recent_events():
    cursor = telemetry_collection.find({}, limit=200).sort("timestamp", -1)

    results = []
    for doc in cursor:
        doc["_id"] = str(doc["_id"])
        results.append(doc)

    return jsonify(results)
