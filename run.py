import os

basedir = os.path.abspath(os.path.dirname(__file__))

from app.app import app

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
