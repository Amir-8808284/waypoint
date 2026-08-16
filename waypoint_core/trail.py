# Import ABC so Trail can become an Abstract Base Class.
# Import abstractmethod so subclasses are forced to implement
# required methods such as estimated_time() and summary().
from abc import ABC, abstractmethod

# Import our Distance class from distance.py.
from .distance import Distance


# ============================================================
# TRAIL ABSTRACT BASE CLASS
# ============================================================
# Trail represents the common information and behavior
# shared by all trail types.
#
# Because Trail inherits from ABC, it can contain abstract
# methods that subclasses must implement.
class Trail(ABC):

    # Class variable containing the default distance unit.
    # This value belongs to the Trail class rather than
    # to one particular Trail object.
    DEFAULT_UNIT = "km"

    # Set containing all valid trail difficulty values.
    ALLOWED_DIFFICULTIES = {
        "easy",
        "moderate",
        "hard",
        "expert"
    }

    # --------------------------------------------------------
    # CONSTRUCTOR
    # --------------------------------------------------------
    # Runs whenever a Trail subclass object is created.
    #
    # Parameters:
    # trail_id         -> unique identifier for the trail
    # name             -> trail name
    # distance         -> Distance object
    # elevation_gain_m -> elevation gain in metres
    # difficulty       -> easy, moderate, hard, or expert
    def __init__(
        self,
        trail_id,
        name,
        distance,
        elevation_gain_m,
        difficulty
    ):
        # Store the trail ID.
        self.id = trail_id

        # Store the trail name.
        self.name = name

        # Store the Distance object.
        self.distance = distance

        # Store elevation gain in metres.
        self.elevation_gain_m = elevation_gain_m

        # Do not directly assign difficulty.
        # Use set_difficulty() so the value is validated first.
        self.set_difficulty(difficulty)

    # --------------------------------------------------------
    # DIFFICULTY PROPERTY
    # --------------------------------------------------------
    # @property allows us to access difficulty like:
    #
    # trail.difficulty
    #
    # while the actual value is stored in _difficulty.
    @property
    def difficulty(self):
        return self._difficulty

    # --------------------------------------------------------
    # SET DIFFICULTY
    # --------------------------------------------------------
    # Validates the supplied difficulty before storing it.
    def set_difficulty(self, difficulty):

        # Call our static validation method.
        if not self.validate_difficulty(difficulty):

            # Stop execution if difficulty is invalid.
            raise ValueError(
                f"Invalid difficulty: {difficulty}"
            )

        # Store the validated difficulty.
        self._difficulty = difficulty

    # --------------------------------------------------------
    # STATIC METHOD - VALIDATE DIFFICULTY
    # --------------------------------------------------------
    # A static method does not need a particular Trail object.
    #
    # It simply checks whether a difficulty value is allowed.
    @staticmethod
    def validate_difficulty(difficulty):
        return difficulty in Trail.ALLOWED_DIFFICULTIES

    # --------------------------------------------------------
    # CLASS METHOD - CHANGE DEFAULT UNIT
    # --------------------------------------------------------
    # A class method receives the class as "cls".
    #
    # It changes DEFAULT_UNIT for the Trail class.
    @classmethod
    def set_default_unit(cls, unit):

        # Only kilometres and miles are supported.
        if unit not in ("km", "mi"):
            raise ValueError(
                "Default unit must be 'km' or 'mi'."
            )

        # Change the class variable.
        cls.DEFAULT_UNIT = unit

    # --------------------------------------------------------
    # CLASS METHOD - CREATE TRAIL FROM DICTIONARY
    # --------------------------------------------------------
    # This is an alternate constructor.
    #
    # It allows us to create a trail using dictionary/API data.
    @classmethod
    def from_dict(cls, data):

        # Get the nested distance dictionary.
        distance_data = data["distance"]

        # Convert the distance dictionary into a Distance object.
        distance = Distance(
            distance_data["magnitude"],
            distance_data["unit"]
        )

        # Create and return an object of the current class.
        return cls(
            trail_id=data["id"],
            name=data["name"],
            distance=distance,
            elevation_gain_m=data["elevation_gain_m"],
            difficulty=data["difficulty"]
        )

    # --------------------------------------------------------
    # EQUALITY OPERATOR
    # --------------------------------------------------------
    # Controls what happens when we write:
    #
    # trail1 == trail2
    #
    # Two trails are considered equal when their IDs match.
    def __eq__(self, other):

        # If "other" is not a Trail, Python should try
        # another way of performing the comparison.
        if not isinstance(other, Trail):
            return NotImplemented

        # Compare the two trail IDs.
        return self.id == other.id

    # --------------------------------------------------------
    # ABSTRACT METHOD - ESTIMATED TIME
    # --------------------------------------------------------
    # Every Trail subclass MUST provide its own implementation
    # of estimated_time().
    #
    # For example:
    # DayHike may calculate time differently from TrailRun.
    @abstractmethod
    def estimated_time(self):
        pass

    # --------------------------------------------------------
    # ABSTRACT METHOD - SUMMARY
    # --------------------------------------------------------
    # Every Trail subclass MUST provide its own summary().
    @abstractmethod
    def summary(self):
        pass

    # --------------------------------------------------------
    # STRING REPRESENTATION
    # --------------------------------------------------------
    # Controls what is displayed when we use:
    #
    # print(trail)
    def __str__(self):

        # Example:
        # Blue Mountain Trail - 5.00 km
        return f"{self.name} - {self.distance}"