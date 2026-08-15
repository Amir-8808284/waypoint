class Distance:
    KM_TO_MILES = 0.621371
    MILES_TO_KM = 1.60934

    def __init__(self, magnitude, unit):
        if magnitude < 0:
            raise ValueError("Distance cannot be negative.")

        if unit not in ("km", "mi"):
            raise ValueError("Unit must be 'km' or 'mi'.")

        self._magnitude = magnitude
        self._unit = unit

    @property
    def magnitude(self):
        return self._magnitude

    @property
    def unit(self):
        return self._unit

    def convert(self, target_unit):
        if target_unit not in ("km", "mi"):
            raise ValueError("Unit must be 'km' or 'mi'.")

        if target_unit == self._unit:
            return Distance(self._magnitude, self._unit)

        if self._unit == "km" and target_unit == "mi":
            converted = self._magnitude * self.KM_TO_MILES
            return Distance(converted, "mi")

        if self._unit == "mi" and target_unit == "km":
            converted = self._magnitude * self.MILES_TO_KM
            return Distance(converted, "km")

    def __str__(self):
        return f"{self._magnitude:.2f} {self._unit}"

    def __repr__(self):
        return f"Distance({self._magnitude!r}, {self._unit!r})"