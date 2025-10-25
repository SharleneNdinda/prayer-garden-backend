from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from prayer_garden_backend.prayer.models import PrayerClassification


class PrayerClassificationView(APIView):
    """View to handle prayer classifications."""

    def get(self, request):
        classification = [
            {"value": classification.value, "label": classification.label}
            for classification in PrayerClassification
        ]
        return Response(classification)
