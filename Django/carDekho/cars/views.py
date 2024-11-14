from django.shortcuts import render
from .models import Car
import json
from django.http import JsonResponse
from rest_framework.response import Response
from .serializers import CarSerializer, QuerySerializer
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.

@api_view(['GET', 'POST'])
def list_cars(request):
    if request.method == 'GET':
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)
        
    elif request.method == 'POST':
        serializer = CarSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'Object created successfully'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors)
        

@api_view(['GET', 'PUT'])
def get_car_detail(request, pk):
    if request.method == 'GET':
        try:
            car = Car.objects.get(pk = pk)
        except Car.DoesNotExist:
            return Response({'error' : 'object not found'}, status= status.HTTP_404_NOT_FOUND)
        serializer = CarSerializer(car)
        return Response(serializer.data)
        
    elif request.method == 'PUT':
        try:
            car = Car.objects.get(pk = pk)
        except Car.DoesNotExist:
            return Response({'error' : 'object not found'}, status= status.HTTP_404_NOT_FOUND)
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'information updated successfully'})
        else:
            return Response(serializer.errors)
        

@api_view(['DELETE'])
def delete_car(request, pk):
    try:
        car = Car.objects.get(pk = pk)
    except Car.DoesNotExist:
        return Response({'error' : 'object not found'}, status= status.HTTP_404_NOT_FOUND)
    car.delete()
    return Response({'message' : 'object deleted succesfully'})

@api_view(['POST'])
def get_query(request):
    data = request.data 
    serializer = QuerySerializer(data = data)
    if serializer.is_valid():
        data = serializer.validated_data
        search_query = data.get('search_query', None)
        sort_by = data.get('sort_by', None)
        filters = data.get('filters', None)

        data = {
            'search using' : search_query,
            'sort using' : sort_by,
            'Filter' : filters
        }

        return Response(data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors)