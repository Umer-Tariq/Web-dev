from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import OwnerSerializer, CarSerializer, CarSerializerList
from .models import Owner, Car

@api_view(['POST'])
def add_owner(request):
    serializer = OwnerSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message" : "object created successfully"})
    else:
        return Response(serializer.errors)
    


@api_view(['GET'])
def list_owner(request):
    owners = Owner.objects.all()
    serialiizer = OwnerSerializer(owners, many=True)
    return Response(serialiizer.data)
    

@api_view(['PUT'])
def update_owner(request, pk):
    owner = Owner.objects.get(pk=pk)
    serialiizer = OwnerSerializer(owner, data = request.data, partial=True)

    if serialiizer.is_valid():
        serialiizer.save()
        return Response({"message" : "object modified successfully"})
    else:
        return Response(serialiizer.errors)
        

@api_view(['POST'])
def add_car(request):
    serializer = CarSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message" : "object created successfully"})
    else:
        return Response(serializer.errors)
    


@api_view(['GET'])
def list_car(request):
    cars = Car.objects.all()
    serialiizer = CarSerializerList(cars, many=True)
    return Response(serialiizer.data)
    

@api_view(['PUT'])
def update_car(request, pk):
    car = Car.objects.get(pk=pk)
    serialiizer = CarSerializer(car, data = request.data, partial=True)

    if serialiizer.is_valid():
        serialiizer.save()
        return Response({"message" : "object modified successfully"})
    else:
        return Response(serialiizer.errors)
        

@api_view(['GET'])
def owner_car(request, pk):
    owner = Owner.objects.get(pk = pk)
    serializer = CarSerializer(owner.cars, many = True)
    return Response(serializer.data)