# Import the Distance class.
from waypoint_core.distance import Distance

# Import the three concrete Trail subclasses.
from waypoint_core.day_hike import DayHike
from waypoint_core.backpacking_route import BackpackingRoute
from waypoint_core.trail_run import TrailRun


# ============================================================
# CREATE DIFFERENT TYPES OF TRAILS
# ============================================================

# A DayHike uses its own estimated_time() implementation.
day_hike = DayHike(
    1,
    "Blue Mountain Trail",
    Distance(8, "km"),
    300,
    "moderate"
)

# A BackpackingRoute uses a slower estimated_time() calculation.
backpacking = BackpackingRoute(
    2,
    "Rocky Ridge Route",
    Distance(12, "km"),
    650,
    "hard"
)

# A TrailRun uses a faster estimated_time() calculation.
trail_run = TrailRun(
    3,
    "River Run",
    Distance(16, "km"),
    180,
    "moderate"
)


# ============================================================
# POLYMORPHIC LIST
# ============================================================

# This list contains objects of different classes.
# Even though they are different trail types, each object
# provides an estimated_time() method.
trails = [
    day_hike,
    backpacking,
    trail_run
]


# ============================================================
# POLYMORPHIC LOOP
# ============================================================

# The same loop works with every trail type.
# Python automatically calls the correct estimated_time()
# method for each object.
for trail in trails:
    print(
        trail.summary(),
        "| Estimated time:",
        trail.estimated_time(),
        "hours"
    )