from get_in_touch.models import GetInTouch
from get_in_touch.serializers import GetInTouchSerializer
from rest_framework import generics

class GetInTouchList(generics.ListCreateAPIView):
    model = GetInTouch
    serializer_class = GetInTouchSerializer
