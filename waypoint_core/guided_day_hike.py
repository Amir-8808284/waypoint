# Import the DayHike class.
# GuidedDayHike will inherit from DayHike.
from .day_hike import DayHike


# ============================================================
# GUIDED DAY HIKE CLASS
# ============================================================
# GuidedDayHike is a child class of DayHike.
#
# Inheritance chain:
#
# Trail
#   ↓
# DayHike
#   ↓
# GuidedDayHike
#
# GuidedDayHike inherits all normal DayHike behavior,
# but adds information about the guide.
class GuidedDayHike(DayHike):

    # --------------------------------------------------------
    # CONSTRUCTOR
    # --------------------------------------------------------
    # We receive all the normal trail information plus
    # one extra field: guide_name.
    def __init__(
        self,
        trail_id,
        name,
        distance,
        elevation_gain_m,
        difficulty,
        guide_name
    ):

        # Call the DayHike constructor.
        #
        # DayHike will then call Trail's constructor.
        #
        # This avoids rewriting all the parent initialization
        # code inside GuidedDayHike.
        super().__init__(
            trail_id,
            name,
            distance,
            elevation_gain_m,
            difficulty
        )

        # Store the extra information that belongs specifically
        # to GuidedDayHike.
        self.guide_name = guide_name

    # --------------------------------------------------------
    # SUMMARY
    # --------------------------------------------------------
    # Override the DayHike summary().
    #

    def summary(self):

        # Get the normal DayHike summary first.
        parent_summary = super().summary()

        # Add the guide information.
        return (
            f"{parent_summary} | "
            f"Guide: {self.guide_name}"
        )