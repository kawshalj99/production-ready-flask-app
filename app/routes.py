from flask import Blueprint
from app.database import get_connection


main = Blueprint("main", __name__)


@main.route("/")
def home():
    return {
        "message": "Welcome to the Production Ready Flask API!",
        "version": "1.0.0"
    }


@main.route("/users")
def users():

    connection = get_connection()

    cursor = connection.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM users"
    )

    result = cursor.fetchall()

    cursor.close()
    connection.close()

    return result