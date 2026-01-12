from pymongo import MongoClient
from pymongo.errors import CollectionInvalid

import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")

DB_NAME = "projexa"
COLLECTION_NAME = "telemetry_events"

client = MongoClient(MONGO_URI)
db = client[DB_NAME]


def ensure_timeseries_collection():
    collections = db.list_collection_names()

    if COLLECTION_NAME in collections:
        print("[MongoDB] Time-series collection exists")
        return

    try:
        db.create_collection(
            COLLECTION_NAME,
            timeseries={
                "timeField": "timestamp",
                "metaField": "meta",
                "granularity": "seconds",
            },
            expireAfterSeconds=60 * 60 * 24 * 30,  # 30 days retention
        )
        print("[MongoDB] Time-series collection created")

    except CollectionInvalid:
        print("[MongoDB] Collection already exists (race condition)")


ensure_timeseries_collection()

telemetry_collection = db[COLLECTION_NAME]
