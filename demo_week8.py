from waypoint_core.distance import Distance
from waypoint_core.trail import Trail
from waypoint_core.day_hike import DayHike
from waypoint_core.backpacking_route import BackpackingRoute
from waypoint_core.trail_run import TrailRun
from waypoint_core.guided_day_hike import GuidedDayHike
from waypoint_core.rated_day_hike import RatedDayHike


print("=== Distance Operators ===")

d1 = Distance(3, "km")
d2 = Distance(2, "km")

print("Addition:", d1 + d2)
print("Subtraction:", Distance(8, "km") - Distance(3, "km"))
print("Equality:", (d1 + d2) == Distance(5, "km"))
print("Less than:", Distance(3, "km") < Distance(5, "km"))
print("Greater than:", Distance(8, "km") > Distance(5, "km"))


print("\n=== Distance Sorting ===")

distances = [
    Distance(8, "km"),
    Distance(2, "km"),
    Distance(5, "km")
]

for distance in sorted(distances):
    print(distance)


print("\n=== Abstract Trail Test ===")

try:
    Trail(
        99,
        "Test Trail",
        Distance(5, "km"),
        100,
        "easy"
    )
except TypeError as error:
    print("Trail cannot be instantiated:", error)


print("\n=== Polymorphism ===")

trails = [
    DayHike(
        1,
        "Blue Mountain",
        Distance(8, "km"),
        300,
        "moderate"
    ),
    BackpackingRoute(
        2,
        "Rocky Ridge",
        Distance(12, "km"),
        650,
        "hard"
    ),
    TrailRun(
        3,
        "River Run",
        Distance(16, "km"),
        180,
        "moderate"
    )
]

for trail in trails:
    print(
        trail.name,
        "-",
        trail.estimated_time(),
        "hours"
    )


print("\n=== Guided Day Hike ===")

guided = GuidedDayHike(
    4,
    "Guided Mountain Walk",
    Distance(8, "km"),
    350,
    "moderate",
    "Alex"
)

print(guided.summary())


print("\n=== Mixins ===")

rated = RatedDayHike(
    5,
    "Lake View Trail",
    Distance(10, "km"),
    500,
    "hard"
)

rated.add_rating(5)
rated.add_rating(4)
rated.add_rating(3)

print("Grade:", rated.grade_percent())
print("Average rating:", rated.average_rating())


print("\n=== MRO ===")

for cls in RatedDayHike.__mro__:
    print(cls.__name__)


print("\n=== Duck Typing ===")


class FakeTrail:
    def __init__(self, name, hours):
        self.name = name
        self.hours = hours

    def estimated_time(self):
        return self.hours


fake = FakeTrail("Fake Test Trail", 1.5)

mixed_trails = [
    trails[0],
    trails[1],
    trails[2],
    fake
]

for trail in mixed_trails:
    print(
        trail.name,
        "-",
        trail.estimated_time(),
        "hours"
    )