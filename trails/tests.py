from decimal import Decimal

from django.test import TestCase
from django.urls import reverse

from .models import Park, Trail


class TrailCatalogTests(TestCase):

    def setUp(self):
        self.park = Park.objects.create(
            name="Test Park",
            region="Ontario"
        )

        self.open_trail = Trail.objects.create(
            name="Open Trail",
            distance_km=Decimal("5.50"),
            elevation_gain=200,
            difficulty="easy",
            is_open=True,
            park=self.park
        )

        self.closed_trail = Trail.objects.create(
            name="Closed Trail",
            distance_km=Decimal("8.00"),
            elevation_gain=350,
            difficulty="hard",
            is_open=False,
            park=self.park
        )

    def test_catalog_displays_only_open_trails(self):
        response = self.client.get(
            reverse("trails:catalog")
        )

        self.assertEqual(
            response.status_code,
            200
        )

        self.assertContains(
            response,
            "Open Trail"
        )

        self.assertNotContains(
            response,
            "Closed Trail"
        )

    def test_trail_detail_page_returns_404_for_missing_trail(self):
        response = self.client.get(
            reverse(
                "trails:detail",
                args=[9999]
            )
        )

        self.assertEqual(
            response.status_code,
            404
        )

    def test_trail_detail_page_returns_200_for_existing_trail(self):
        response = self.client.get(
            reverse(
                "trails:detail",
                args=[self.open_trail.id]
            )
        )

        self.assertEqual(
            response.status_code,
            200
        )

        self.assertContains(
            response,
            "Open Trail"
        )