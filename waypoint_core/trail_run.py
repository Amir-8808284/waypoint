# Import the Trail parent class.
from .trail import Trail


# ============================================================
# TRAIL RUN CLASS
# ============================================================
# TrailRun represents a trail intended for running.
# It uses a faster pace than hiking or backpacking.
class TrailRun(Trail):

    # --------------------------------------------------------
    # CONSTRUCTOR
    # --------------------------------------------------------
    # Reuse the Trail constructor with super().
    def __init__(
        self,
        trail_id,
        name,
        distance,
        elevation_gain_m,
        difficulty
    ):
        # Call the parent Trail constructor.
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
    # A trail runner moves faster than a hiker.
    # We will use an average speed of 8 km per hour.
    def estimated_time(self):

        # Convert the distance to kilometres first.
        distance_km = self.distance.convert("km")

        # Calculate the estimated running time in hours.
        hours = distance_km.magnitude / 8

        return hours

    # --------------------------------------------------------
    # SUMMARY
    # --------------------------------------------------------
    # Return a readable description of the TrailRun.
    def summary(self):
        return (
            f"Trail Run: {self.name} | "
            f"Distance: {self.distance} | "
            f"Difficulty: {self.difficulty}"
        )