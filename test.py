from waypoint_core.distance import Distance
from waypoint_core.trail import Trail
from waypoint_core.itinerary import Itinerary


print("===== DISTANCE TESTS =====")

d1 = Distance(10, "km")
print("Distance:", d1)

miles = d1.convert("mi")
print("Converted to miles:", miles)

back_to_km = miles.convert("km")
print("Converted back to km:", back_to_km)

try:
    Distance(-5, "km")
except ValueError as error:
    print("Negative distance test:", error)


print("\n===== TRAIL TESTS =====")

trail1 = Trail(
    1,
    "Blue Mountain Trail",
    Distance(5, "km"),
    250,
    "moderate"
)

print("Trail 1:", trail1)
print("Difficulty:", trail1.difficulty)


trail_data = {
    "id": 2,
    "name": "Forest Loop",
    "distance": {
        "magnitude": 8,
        "unit": "km"
    },
    "elevation_gain_m": 300,
    "difficulty": "hard"
}

trail2 = Trail.from_dict(trail_data)

print("Trail from dict:", trail2)


trail3 = Trail(
    2,
    "Different Trail",
    Distance(50, "km"),
    900,
    "easy"
)

print("Same ID equality test:", trail2 == trail3)


try:
    Trail(
        4,
        "Invalid Trail",
        Distance(3, "km"),
        100,
        "impossible"
    )
except ValueError as error:
    print("Invalid difficulty test:", error)


print("\n===== ITINERARY TESTS =====")

t1 = Trail(
    10,
    "Trail One",
    Distance(5, "km"),
    100,
    "easy"
)

t2 = Trail(
    11,
    "Trail Two",
    Distance(8, "km"),
    200,
    "moderate"
)

t3 = Trail(
    12,
    "Trail Three",
    Distance(2, "km"),
    50,
    "hard"
)

trip = Itinerary()

trip.add_trail(t1)
trip.add_trail(t2)
trip.add_trail(t3)

print("Total distance:", trip.total_distance())


trip2 = Itinerary()

print("Trip 1 trail count:", len(trip.trails))
print("Trip 2 trail count:", len(trip2.trails))