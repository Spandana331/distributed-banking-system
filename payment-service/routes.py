
from flask import Blueprint, jsonify
import requests

payment_routes = Blueprint("payment_routes", __name__)

@payment_routes.route("/")
def home():
    return "Payment Service Running"

@payment_routes.route("/pay")
def pay():
    response = requests.get("http://localhost:5003/history")
    return jsonify({
        "payment": "Payment Successful",
        "transaction_service_response": response.json()
    })
