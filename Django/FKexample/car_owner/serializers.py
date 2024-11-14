from rest_framework import serializers
from .models import Owner, Car





class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class OwnerSerializer(serializers.ModelSerializer):
    cars = CarSerializer(many=True)
    class Meta:
        model = Owner
        fields = ['name', 'email', 'cars']

class CarSerializerList(serializers.ModelSerializer):
    owner = OwnerSerializer()
    class Meta:
        model = Car
        fields = '__all__'
