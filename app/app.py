from flask import Flask
from flask_cors import CORS
from ingest import ingest_bp
from queries import query_bp
import db  # IMPORTANT: triggers collection creation

app = Flask(__name__, static_folder="frontend", static_url_path="/frontend")
CORS(app)

app.register_blueprint(ingest_bp)
app.register_blueprint(query_bp)


@app.route("/")
def index():
    return app.send_static_file("index.html")


if __name__ == "__main__":
    print("[Startup] Projexa Observability Backend")
    app.run(host="0.0.0.0", port=5000, debug=True)
