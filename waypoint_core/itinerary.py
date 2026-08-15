from .distance import Distance


class Itinerary:
    def __init__(self):
        self._trails = []

    def add_trail(self, trail):
        self._trails.append(trail)

    @property
    def trails(self):
        return list(self._trails)

    def total_distance(self):
        if not self._trails:
            return Distance(0, "km")

        total_km = 0

        for trail in self._trails:
            distance_km = trail.distance.convert("km")
            total_km += distance_km.magnitude

        return Distance(total_km, "km")