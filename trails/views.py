from django.shortcuts import get_object_or_404, render

from .models import Park, Trail


def catalog(request):
    park_id = request.GET.get("park", "")

    trails = Trail.objects.filter(
        is_open=True
    ).select_related(
        "park"
    ).order_by(
        "distance_km"
    )

    if park_id:
        trails = trails.filter(
            park_id=park_id
        )

    parks = Park.objects.all().order_by("name")

    context = {
        "trails": trails,
        "parks": parks,
        "selected_park": park_id,
    }

    return render(
        request,
        "catalog.html",
        context
    )


def detail(request, trail_id):
    trail = get_object_or_404(
        Trail,
        id=trail_id
    )

    context = {
        "trail": trail
    }

    return render(
        request,
        "trail_detail.html",
        context
    )