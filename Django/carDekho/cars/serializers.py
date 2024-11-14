from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    model = serializers.CharField()
    year = serializers.IntegerField()

    def create(self, validated_data):
        return Car.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.model = validated_data.get('model', instance.model)
        instance.year = validated_data.get('year', instance.year)
        instance.id = validated_data.get('id', instance.id)
        instance.save()
        return instance

class QuerySerializer(serializers.Serializer):
    search_query = serializers.CharField()
    sort_by = serializers.ChoiceField(choices=['Price', 'Year'])
    filters = serializers.DictField(child = serializers.CharField())

    