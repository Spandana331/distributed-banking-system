
from flask import Blueprint, jsonify

transaction_routes = Blueprint("transaction_routes", __name__)

@transaction_routes.route("/")
def home():
    return "Transaction Service Running"

@transaction_routes.route("/history")
def history():
    return jsonify({"transaction": "Transaction Recorded"})
