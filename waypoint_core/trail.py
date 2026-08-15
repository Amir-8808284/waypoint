from .distance import Distance


class Trail:
    DEFAULT_UNIT = "km"

    ALLOWED_DIFFICULTIES = {
        "easy",
        "moderate",
        "hard",
        "expert"
    }

    def __init__(
        self,
        trail_id,
        name,
        distance,
        elevation_gain_m,
        difficulty
    ):
        self.id = trail_id
        self.name = name
        self.distance = distance
        self.elevation_gain_m = elevation_gain_m

        self.set_difficulty(difficulty)

    def set_difficulty(self, difficulty):
        if not self.validate_difficulty(difficulty):
            raise ValueError(
                f"Invalid difficulty: {difficulty}"
            )

        self._difficulty = difficulty

    @property
    def difficulty(self):
        return self._difficulty

    @classmethod
    def set_default_unit(cls, unit):
        if unit not in ("km", "mi"):
            raise ValueError(
                "Default unit must be 'km' or 'mi'."
            )

        cls.DEFAULT_UNIT = unit

    @staticmethod
    def validate_difficulty(difficulty):
        return difficulty in Trail.ALLOWED_DIFFICULTIES

    @classmethod
    def from_dict(cls, data):
        distance_data = data["distance"]

        distance = Distance(
            distance_data["magnitude"],
            distance_data["unit"]
        )

        return cls(
            trail_id=data["id"],
            name=data["name"],
            distance=distance,
            elevation_gain_m=data["elevation_gain_m"],
            difficulty=data["difficulty"]
        )

    def __eq__(self, other):
        if not isinstance(other, Trail):
            return NotImplemented

        return self.id == other.id

    def __str__(self):
        return f"{self.name} - {self.distance}"