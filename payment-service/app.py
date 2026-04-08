
from flask import Flask
from routes import payment_routes

app = Flask(__name__)
app.register_blueprint(payment_routes)

if __name__ == "__main__":
    app.run(port=5002, debug=True)
