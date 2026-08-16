# Import the abstract Trail parent class.
from .trail import Trail


# ============================================================
# DAY HIKE CLASS
# ============================================================
# DayHike is a concrete subclass of Trail.
# It represents a trail that can normally be completed in one day.
class DayHike(Trail):

    # --------------------------------------------------------
    # CONSTRUCTOR
    # --------------------------------------------------------
    # We reuse the parent Trail constructor with super().
    def __init__(
        self,
        trail_id,
        name,
        distance,
        elevation_gain_m,
        difficulty
    ):
        # Call the Trail constructor so we do not duplicate code.
        super().__init__(
            trail_id,
            name,
            distance,
            elevation_gain_m,
            difficulty
        )

    # --------------------------------------------------------
    # ESTIMATED TIME
    # --------------------------------------------------------
    # Estimate hiking time using a simple pace:
    # 4 kilometres per hour.
    def estimated_time(self):

        # Convert the distance to kilometres first.
        distance_km = self.distance.convert("km")

        # Divide distance by hiking speed.
        hours = distance_km.magnitude / 4

        return hours

    # --------------------------------------------------------
    # SUMMARY
    # --------------------------------------------------------
    # Return a readable summary of the DayHike object.
    def summary(self):
        return (
            f"Day Hike: {self.name} | "
            f"Distance: {self.distance} | "
            f"Difficulty: {self.difficulty}"
        )