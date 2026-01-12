# Projexa AI Analytics

Analytics ingestion pipeline for Projexa AI — collect, process, and visualize usage data and query events in real-time.

## Prerequisites

- Python 3.10 or higher
- pip
- (Optional) Docker and Docker Compose

## Quick start

1. Create and activate a virtual environment:

   - Windows: `python -m venv venv && venv\Scripts\activate`
   - macOS / Linux: `python -m venv venv && source venv/bin/activate`

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:

   ```bash
   python app/app.py
   ```

4. Open your browser at: http://localhost:5000

## Using Docker

To run with Docker Compose:

```bash
docker compose up --build
```

## Project layout

- `app/` - backend Flask application and static frontend (see `app.py`, `ingest.py`, `queries.py`, `db.py`)
- `requirements.txt` - Python dependencies
- `Dockerfile`, `docker-compose.yml` - containerization

## What it does

This service ingests analytics and telemetry events from Projexa AI and provides:

- **Batch event ingestion** — `/api/v1/analytics/batch` endpoint accepts JSON arrays of events
- **MongoDB time-series storage** — events stored in time-series collections with 30-day automatic retention
- **Recent events API** — `/api/v1/events/recent` returns the latest 200 events sorted by timestamp
- **Simple dashboard** — web UI to view recent telemetry and query events
- **Docker deployment** — containerized setup with MongoDB integration

## Contributing

1. Fork the repository and create a feature branch
2. Make focused changes — keep PRs small and single-purpose
3. Test locally before submitting: `python app/app.py`
4. Submit a pull request with a clear description of changes
