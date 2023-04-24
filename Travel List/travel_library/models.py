from dataclasses import dataclass, field


@dataclass
class Trip:
    """
    A dataclass representing a trip, containing information
    about the destination, travel details, and user feedback.

    Attributes:
        _id (str): The unique ID for the trip.
        attraction (str): The name of the attraction.
        city (str): The name of the city.
        country (str): The name of the country.
        travel_days(list[str]): A list of recommended travel days for the trip.
        Defaults to an empty list.
        best_season (list[str]): A list of the best seasons to visit the attraction.
        Defaults to an empty list.
        rating(int): The average user rating for the trip,ranging from 0 to 5.
        comments (list[dict]): A list of user comments, where each comment is a
        dictionary containing comment and timestamp. Defaults to empty list.
        tags (list[str]): A list of tags that describe the attraction.
        Defaults to an empty list.
        description (str, optional): A detailed description of the attraction.
        video_link (str, optional): A URL to a video showcasing the attraction.
    """
    _id: str
    attraction: str
    city: str
    country: str
    travel_days: list[str] = field(default_factory=list)
    best_season: list[str] = field(default_factory=list)
    rating: int = 0
    comments: list[dict] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)
    description: str = None
    video_link: str = None
