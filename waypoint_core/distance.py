# ============================================================
# DISTANCE VALUE TYPE
# ============================================================
# Distance represents a numeric distance with a unit.
#
# Supported units:
# - "km" for kilometres
# - "mi" for miles
#
# Week 8 adds operator overloading so Distance objects can
# behave more like normal numeric values.
class Distance:

    # Conversion constants.
    KM_TO_MILES = 0.621371
    MILES_TO_KM = 1.60934

    # --------------------------------------------------------
    # CONSTRUCTOR
    # --------------------------------------------------------
    def __init__(self, magnitude, unit):

        # Distance cannot be negative.
        if magnitude < 0:
            raise ValueError(
                "Distance cannot be negative."
            )

        # Only kilometres and miles are supported.
        if unit not in ("km", "mi"):
            raise ValueError(
                "Unit must be 'km' or 'mi'."
            )

        # Store the magnitude privately.
        self._magnitude = magnitude

        # Store the unit privately.
        self._unit = unit

    # --------------------------------------------------------
    # MAGNITUDE PROPERTY
    # --------------------------------------------------------
    # Read-only accessor for the distance magnitude.
    @property
    def magnitude(self):
        return self._magnitude

    # --------------------------------------------------------
    # UNIT PROPERTY
    # --------------------------------------------------------
    # Read-only accessor for the distance unit.
    @property
    def unit(self):
        return self._unit

    # --------------------------------------------------------
    # CONVERT
    # --------------------------------------------------------
    # Convert this Distance object to another supported unit.
    def convert(self, target_unit):

        # Validate the requested unit.
        if target_unit not in ("km", "mi"):
            raise ValueError(
                "Unit must be 'km' or 'mi'."
            )

        # If the requested unit is already the same,
        # return a new Distance with the same value.
        if target_unit == self._unit:
            return Distance(
                self._magnitude,
                self._unit
            )

        # Convert kilometres to miles.
        if self._unit == "km" and target_unit == "mi":
            converted = (
                self._magnitude
                * self.KM_TO_MILES
            )

            return Distance(
                converted,
                "mi"
            )

        # Convert miles to kilometres.
        if self._unit == "mi" and target_unit == "km":
            converted = (
                self._magnitude
                * self.MILES_TO_KM
            )

            return Distance(
                converted,
                "km"
            )

    # --------------------------------------------------------
    # ADDITION OPERATOR
    # --------------------------------------------------------
    # Controls:
    #
    # distance1 + distance2
    #
    # Mixed units are automatically converted to the
    # unit used by the first Distance object.
    def __add__(self, other):

        # Only Distance objects can be added.
        if not isinstance(other, Distance):
            return NotImplemented

        # Convert the second distance to this object's unit.
        other_converted = other.convert(
            self._unit
        )

        # Add the magnitudes.
        result = (
            self._magnitude
            + other_converted.magnitude
        )

        # Return a new Distance object.
        return Distance(
            result,
            self._unit
        )

    # --------------------------------------------------------
    # SUBTRACTION OPERATOR
    # --------------------------------------------------------
    # Controls:
    #
    # distance1 - distance2
    def __sub__(self, other):

        # Only Distance objects can be subtracted.
        if not isinstance(other, Distance):
            return NotImplemented

        # Convert the second distance to this object's unit.
        other_converted = other.convert(
            self._unit
        )

        # Calculate the difference.
        result = (
            self._magnitude
            - other_converted.magnitude
        )

        # A negative result is not allowed because Distance
        # itself rejects negative magnitudes.
        if result < 0:
            raise ValueError(
                "Distance subtraction cannot "
                "produce a negative result."
            )

        return Distance(
            result,
            self._unit
        )

    # --------------------------------------------------------
    # EQUALITY OPERATOR
    # --------------------------------------------------------
    # Controls:
    #
    # distance1 == distance2
    def __eq__(self, other):

        if not isinstance(other, Distance):
            return NotImplemented

        # Convert the second distance to the first unit.
        other_converted = other.convert(
            self._unit
        )

        # Floating-point conversion can introduce tiny
        # rounding differences, so compare with tolerance.
        return abs(
            self._magnitude
            - other_converted.magnitude
        ) < 0.0001

    # --------------------------------------------------------
    # LESS THAN OPERATOR
    # --------------------------------------------------------
    # Controls:
    #
    # distance1 < distance2
    def __lt__(self, other):

        if not isinstance(other, Distance):
            return NotImplemented

        other_converted = other.convert(
            self._unit
        )

        return (
            self._magnitude
            < other_converted.magnitude
        )

    # --------------------------------------------------------
    # GREATER THAN OPERATOR
    # --------------------------------------------------------
    # Controls:
    #
    # distance1 > distance2
    def __gt__(self, other):

        if not isinstance(other, Distance):
            return NotImplemented

        other_converted = other.convert(
            self._unit
        )

        return (
            self._magnitude
            > other_converted.magnitude
        )

    # --------------------------------------------------------
    # STRING REPRESENTATION
    # --------------------------------------------------------
    # Used by print(distance).
    def __str__(self):
        return (
            f"{self._magnitude:.2f} "
            f"{self._unit}"
        )

    # --------------------------------------------------------
    # DEVELOPER REPRESENTATION
    # --------------------------------------------------------
    # Used when debugging or displaying objects in a list.
    def __repr__(self):
        return (
            f"Distance("
            f"{self._magnitude!r}, "
            f"{self._unit!r})"
        )