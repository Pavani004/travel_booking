from flask import Blueprint, request, jsonify
from app.models import FlightBooking
from app import db

booking_bp = Blueprint('booking_bp', __name__)

@booking_bp.route("/book-flight", methods=["POST"])
def book_flight():
    data = request.json
    booking = FlightBooking(
        user=data["user"],
        flight_number=data["flight_number"],
        date=data["date"]
    )
    db.session.add(booking)
    db.session.commit()
    return jsonify({"message": "Flight booked successfully!"})
