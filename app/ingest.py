from flask import Blueprint, request, jsonify
from datetime import datetime
from app.db import telemetry_collection

ingest_bp = Blueprint("ingest", __name__)


@ingest_bp.route("/api/v1/analytics/batch", methods=["POST"])
def ingest_batch():
    try:
        payload = request.get_json(force=True)

        if not isinstance(payload, list):
            return jsonify({"error": "Payload must be a list"}), 400

        now = datetime.utcnow()
        docs = []

        for event in payload:
            # Parse timestamp if present in meta
            timestamp = now
            meta = event.get("meta", {})
            if "timestamp" in meta:
                try:
                    timestamp = datetime.fromisoformat(meta["timestamp"].replace("Z", "+00:00"))
                except ValueError:
                    pass  # Fallback to 'now' if parsing fails

            docs.append(
                {
                    "type": event.get("type"),
                    "data": event.get("data", {}),
                    "meta": meta,
                    "timestamp": timestamp,
                }
            )

        if docs:
            telemetry_collection.insert_many(docs, ordered=False)

        return jsonify({"status": "ok"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
