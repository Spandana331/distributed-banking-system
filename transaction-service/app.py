
from flask import Flask
from routes import transaction_routes

app = Flask(__name__)
app.register_blueprint(transaction_routes)

if __name__ == "__main__":
    app.run(port=5003, debug=True)
