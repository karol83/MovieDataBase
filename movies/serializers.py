from rest_framework import serializers

from .models import FavouriteMovie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavouriteMovie
        fields = '__all__'
