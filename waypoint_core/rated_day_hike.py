# Import the DayHike class.
from .day_hike import DayHike


from .mixins import ElevationMixin, RatingMixin


# ============================================================
# RATED DAY HIKE
# ============================================================
# RatedDayHike combines:
#
# - ElevationMixin
# - RatingMixin
# - DayHike
#
# This demonstrates multiple inheritance.
#
# Python will search these classes in a specific order.
# That order is called the MRO:
# Method Resolution Order.
class RatedDayHike(
    ElevationMixin,
    RatingMixin,
    DayHike
):

    # --------------------------------------------------------
    # CONSTRUCTOR
    # --------------------------------------------------------
    def __init__(
        self,
        trail_id,
        name,
        distance,
        elevation_gain_m,
        difficulty
    ):

        # Reuse DayHike / Trail initialization.
        super().__init__(
            trail_id,
            name,
            distance,
            elevation_gain_m,
            difficulty
        )

        # RatingMixin provides this method.
        # It creates the empty ratings list.
        self.initialize_ratings()