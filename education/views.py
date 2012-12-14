from education.models import Education
from education.serializers import EducationSerializer
from rest_framework import generics


class EducationList(generics.ListCreateAPIView):
    model = Education
    serializer_class = EducationSerializer

