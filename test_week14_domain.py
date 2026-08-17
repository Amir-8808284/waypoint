import unittest

from waypoint_core.distance import Distance


class DistanceTests(unittest.TestCase):

    def test_negative_distance_raises_value_error(self):
        with self.assertRaises(ValueError):
            Distance(-5, "km")


if __name__ == "__main__":
    unittest.main()