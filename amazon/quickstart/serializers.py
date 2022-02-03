
from rest_framework import serializers
from affairs.models import students


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = students
        fields = ['id', 'name', 'track']

