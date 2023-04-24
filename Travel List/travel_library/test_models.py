import unittest
from dataclasses import asdict
from models import Trip


class TestTrip(unittest.TestCase):
    def test_trip(self):
        """To checks if the Trip object is created with
           the correct attributes and defult values."""
        trip = Trip(_id="123",
                    attraction="Golden Gate Bridge",
                    city="San Francisco", country="USA")

        self.assertEqual(trip._id, "123")
        self.assertEqual(trip.attraction, "Golden Gate Bridge")
        self.assertEqual(trip.city, "San Francisco")
        self.assertEqual(trip.country, "USA")
        self.assertEqual(trip.rating, 0)
        self.assertEqual(len(trip.comments), 0)
        self.assertEqual(len(trip.tags), 0)
        self.assertIsNone(trip.description)
        self.assertIsNone(trip.video_link)

    def test_trip_as_dict(self):
        """To checks if the Trip object can be converted to a dictionary
        using the asdict function from the dataclasses module and if the
        resulting dictionary has the expected structure."""
        trip = Trip(_id="123",
                    attraction="Golden Gate Bridge",
                    city="San Francisco", country="USA")

        trip_dict = asdict(trip)
        expected_dict = {"_id": "123",
                         "attraction": "Golden Gate Bridge",
                         "city": "San Francisco",
                         "country": "USA",
                         "travel_days": [],
                         "best_season": [],
                         "rating": 0,
                         "comments": [],
                         "tags": [],
                         "description": None,
                         "video_link": None}
        self.assertEqual(trip_dict, expected_dict)


if __name__ == '__main__':
    unittest.main()
