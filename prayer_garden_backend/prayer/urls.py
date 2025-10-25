from django.urls import path
from .views import PrayerClassificationView

urlpatterns = [
    path(
        "prayer_classifications/",
        PrayerClassificationView.as_view(),
        name="prayer-classifications",
    )
]
