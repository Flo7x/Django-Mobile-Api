from rest_framework import serializers
from .models import UserProfile, Error, Countries, Histories, Types, Fact

class CountriesSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Countries
        fields = ("id", "title", "prefix")