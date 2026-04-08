
from flask import Blueprint, jsonify
import requests

user_routes = Blueprint("user_routes", __name__)

@user_routes.route("/")
def home():
    return "User Service Running"

@user_routes.route("/login")
def login():
    return jsonify({"message": "User Logged In"})

@user_routes.route("/send-payment")
def send_payment():
    response = requests.get("http://localhost:5002/pay")
    return jsonify({
        "user_service": "Payment Request Sent",
        "payment_service_response": response.json()
    })
