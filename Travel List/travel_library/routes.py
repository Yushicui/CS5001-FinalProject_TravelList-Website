import uuid
from datetime import datetime
from flask import (Blueprint, current_app, render_template,
                   redirect, request, url_for, abort, flash)
from dataclasses import asdict
from travel_library.forms import TravelForm, ExtendedTravelForm
from travel_library.models import Trip


# Create a 'pages' Blueprint for organizing routes and views of the website.
pages = Blueprint("pages", __name__, template_folder="templates",
                  static_folder="static")


@pages.route("/")
def index():
    """
    The index view function renders the main page of the application,
    which displays a list of trips.

    return: Rendered 'index.html' template with the trip data.
    """
    # Retrieve data from the database with trip ID
    trip_data = current_app.db.trips.find({})
    # Create a list of Trip objects from the retrieved data
    trips = [Trip(**trip) for trip in trip_data]
    return render_template("index.html", title="TravelList", trip_data=trips)


@pages.route("/add", methods=["GET", "POST"])
def add_trip():
    """
    This function handles the addition of new trips to the database.

    return: Rendered 'new_trip.html' template or a redirect to the index page.
    """
    form = TravelForm()

    if form.validate_on_submit():  # check and validate the entries in the form
        trip = Trip(_id=uuid.uuid4().hex,
                    attraction=form.attraction.data,
                    city=form.city.data,
                    country=form.country.data)
        # Insert the new Trip object into the database as dictionary
        current_app.db.trips.insert_one(asdict(trip))
        return redirect(url_for(".index"))
    return render_template("new_trip.html",
                           title="TravelList - Add Trip",
                           form=form)


@pages.route("/edit/<string:_id>", methods=["GET", "POST"])
def edit_trip(_id: str):
    """
    This function handles the editing of existing trips in the database.

    Arg:  _id: The trip ID to be edited.

    return: Rendered 'trip_form.html' template
            or redirect to the trip's page.
    """
    # Retrieve trip data from the database with trip ID
    trip_data = current_app.db.trips.find_one({"_id": _id})
    trip = Trip(**trip_data)
    form = ExtendedTravelForm(obj=trip)

    if form.validate_on_submit():
        trip.travel_days = form.travel_days.data
        trip.best_season = form.best_season.data
        trip.tags = form.tags.data
        trip.description = form.description.data
        trip.video_link = form.video_link.data
        # Save the updated Trip object to the database
        current_app.db.trips.update_one({"_id": _id}, {"$set": asdict(trip)})
        return redirect(url_for(".trip", _id=trip._id))
    # Render the trip_form.html with pre-filled trip details in the form
    return render_template("trip_form.html", trip=trip, form=form)


@pages.route("/delete/<string:_id>", methods=["GET", "POST"])
def delete_trip(_id: str):
    """
    The delete_trip view function handles the deletion of existing
    trips in the database.

    Arg:  _id: The trip ID to be deleted.

    return: Rendered 'delete_trip.html' template or redirect to index page.
    """
    trip_data = current_app.db.trips.find_one({"_id": _id})
    if not trip_data:
        flash("Trip not found.", "error")
        return redirect(url_for(".index"))
    if request.method == "POST":
        # Delete the trip from the database
        current_app.db.trips.delete_one({"_id": _id})
        return redirect(url_for(".index"))
    return render_template("delete_trip.html", trip=Trip(**trip_data))


@pages.route("/search", methods=["GET", "POST"])
def search():
    """
    Route for searching trips based on attraction, city, or country.

    If the request method is POST, search for a trip based on the
    user's query and redirect to the trip's page if found.
    If no trip is found, redirect to the add_trip page.
    """
    if request.method == "POST":
        query = request.form.get("query")
        # Find a trip in the database that match the attraction,city or country
        # $regex is a MongoDB query operator to perform a search
        # "i" option is to make the search "case-insensitive"
        trip = current_app.db.trips.find_one({
            "$or": [
                {"attraction": {"$regex": query, "$options": "i"}},
                {"city": {"$regex": query, "$options": "i"}},
                {"country": {"$regex": query, "$options": "i"}},]})
        if trip:
            return redirect(url_for(".trip", _id=trip["_id"]))
        else:
            return redirect(url_for(".add_trip"))


@pages.route("/trip/<string:_id>", methods=["GET", "POST"])
def trip(_id: str):
    """
    Route for displaying a trip's details and handling comments.

    If the request method is POST, add the user's comment to the trip
    and update the database. If the request method is GET, render the
    trip_info.html template with the trip's details.
    """
    trip_data = current_app.db.trips.find_one({"_id": _id})
    if not trip_data:
        abort(404)
    trip = Trip(**trip_data)
    if request.method == "POST":
        comment = request.form.get("comment")
        if comment:
            new_comment = {
                "content": comment,
                "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
            }
            trip.comments.append(new_comment)
            # Update the database with the new trip data
            current_app.db.trips.update_one({"_id": _id},
                                            {"$set": asdict(trip)})
            return redirect(url_for(".trip", _id=_id))
    return render_template("trip_info.html", trip=trip)


@pages.route("/trip/<string:_id>/delete_comment/<int:comment_index>",
             methods=["POST"])
def delete_comment(_id: str, comment_index: int):
    """
    Route for deleting a comment from a trip.

    This function receives the trip's _id and the index of the comment to be
    deleted. If the comment index is within the range of the trip's comments,
    it removes the comment and updates the database.
    """
    trip_data = current_app.db.trips.find_one({"_id": _id})
    trip = Trip(**trip_data)
    if 0 <= comment_index < len(trip.comments):
        del trip.comments[comment_index]
        # Update the database
        current_app.db.trips.update_one({"_id": _id},
                                        {"$set": asdict(trip)})
        return redirect(url_for(".trip", _id=_id))
    return abort(404)


@pages.get("/trips/<string:_id>/rate")
def rate_trip(_id: str):
    """
    Route for updating the rating of a trip.

    This function receives the trip's _id and a rating value.
    It updates the trip's rating in the database and
    redirects the user back to the trip's page.
    """
    rating = int(request.args.get("rating"))
    # Update rating in database
    current_app.db.trips.update_one({"_id": _id}, {"$set": {"rating": rating}})
    return redirect(url_for(".trip", _id=_id))
