# ============================================================
# ELEVATION MIXIN
# ============================================================
# A mixin is a small reusable class that adds one specific
# behavior to another class.
#
# ElevationMixin adds a method for calculating average
# elevation grade as a percentage.
class ElevationMixin:

    # --------------------------------------------------------
    # GRADE PERCENT
    # --------------------------------------------------------
    # Calculate average elevation grade using:
    #
    # elevation gain / horizontal distance * 100
    def grade_percent(self):

        # Convert the trail's distance to kilometres.
        distance_km = self.distance.convert("km")

        # Convert kilometres to metres because
        # elevation_gain_m is stored in metres.
        distance_m = distance_km.magnitude * 1000

        # Prevent division by zero.
        if distance_m == 0:
            return 0

        # Calculate grade percentage.
        grade = (
            self.elevation_gain_m
            / distance_m
        ) * 100

        return grade


# ============================================================
# RATING MIXIN
# ============================================================
# RatingMixin adds rating functionality to a trail class.
class RatingMixin:

    # --------------------------------------------------------
    # INITIALIZE RATINGS
    # --------------------------------------------------------
    # Creates an empty list that will store ratings.
    def initialize_ratings(self):
        self._ratings = []

    # --------------------------------------------------------
    # ADD RATING
    # --------------------------------------------------------
    # Add a star rating between 1 and 5.
    def add_rating(self, rating):

        # Only ratings from 1 through 5 are allowed.
        if rating < 1 or rating > 5:
            raise ValueError(
                "Rating must be between 1 and 5."
            )

        # Add the valid rating to the list.
        self._ratings.append(rating)

    # --------------------------------------------------------
    # AVERAGE RATING
    # --------------------------------------------------------
    # Calculate the average of all ratings.
    def average_rating(self):

        # Return 0 when there are no ratings yet.
        if not self._ratings:
            return 0

        # Calculate and return the average.
        return sum(self._ratings) / len(self._ratings)