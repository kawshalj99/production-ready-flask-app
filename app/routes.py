from flask import Blueprint

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return {
        "message": "Welcome to the Production Ready Flask API!",
        "version": "1.0.0"
        
        
    }