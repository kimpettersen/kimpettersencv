from rest_framework import serializers
from get_in_touch.models import GetInTouch


class GetInTouchSerializer(serializers.ModelSerializer):

    class Meta:
        model = GetInTouch
        fields = ('id', 'name', 'info')
