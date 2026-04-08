
from flask import Flask
from routes import user_routes

app = Flask(__name__)
app.register_blueprint(user_routes)

if __name__ == "__main__":
    app.run(port=5001, debug=True)
