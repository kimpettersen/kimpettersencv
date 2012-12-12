from rest_framework import serializers
from snippets import models
from django.contrib.auth.models import User


class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.Field(source='owner.username')

    class Meta:
        model = models.Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style', 'owner')


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.ManyPrimaryKeyRelatedField()

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')
