# Import the Trail parent class.
from .trail import Trail


# ============================================================
# BACKPACKING ROUTE CLASS
# ============================================================
# BackpackingRoute represents a longer trail that may take
# more than one day and usually has a slower average pace.
class BackpackingRoute(Trail):

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
    # Backpacking is usually slower than a normal day hike.
    # We will use an average speed of 3 km per hour.
    def estimated_time(self):

        # Convert the distance to kilometres.
        distance_km = self.distance.convert("km")

        # Calculate total estimated hours.
        hours = distance_km.magnitude / 3

        return hours

    # --------------------------------------------------------
    # SUMMARY
    # --------------------------------------------------------
    # Return a readable description of the route.
    def summary(self):
        return (
            f"Backpacking Route: {self.name} | "
            f"Distance: {self.distance} | "
            f"Difficulty: {self.difficulty}"
        )