from waypoint_core.distance import Distance
from waypoint_core.day_hike import DayHike
from waypoint_core.backpacking_route import BackpackingRoute
from waypoint_core.trail_run import TrailRun


# ============================================================
# FAKE TRAIL
# ============================================================
# FakeTrail does NOT inherit from Trail.
#

class FakeTrail:

    # --------------------------------------------------------
    # CONSTRUCTOR
    # --------------------------------------------------------
    def __init__(self, name, hours):

        # Store a simple name.
        self.name = name

        # Store a fixed estimated time.
        self.hours = hours

    # --------------------------------------------------------
    # ESTIMATED TIME
    # --------------------------------------------------------
    # This method has the same name as the real trail classes.
    def estimated_time(self):
        return self.hours

    # --------------------------------------------------------
    # SUMMARY
    # --------------------------------------------------------
    # This also matches the method name used by real trails.
    def summary(self):
        return f"Fake Trail: {self.name}"


# ============================================================
# CREATE REAL TRAILS
# ============================================================

day_hike = DayHike(
    1,
    "Blue Mountain Trail",
    Distance(8, "km"),
    300,
    "moderate"
)

backpacking = BackpackingRoute(
    2,
    "Rocky Ridge Route",
    Distance(12, "km"),
    650,
    "hard"
)

trail_run = TrailRun(
    3,
    "River Run",
    Distance(16, "km"),
    180,
    "moderate"
)


# ============================================================
# CREATE FAKE TRAIL
# ============================================================

fake_trail = FakeTrail(
    "Testing Trail",
    1.5
)


# ============================================================
# MIXED LIST
# ============================================================
# This list contains three real trail subclasses
# plus one object that is not related to Trail at all.
trails = [
    day_hike,
    backpacking,
    trail_run,
    fake_trail
]


# ============================================================
# POLYMORPHIC / DUCK-TYPED LOOP
# ============================================================
# The loop does not care what class each object belongs to.
#
# It only expects:
# - summary()
# - estimated_time()
#
# Because FakeTrail provides those methods, it works too.
for trail in trails:
    print(
        trail.summary(),
        "| Estimated time:",
        trail.estimated_time(),
        "hours"
    )