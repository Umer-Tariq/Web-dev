from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ItemSerializer, OrderSerializer2, OrderSerializer
from .models import Item, Order

@api_view(['POST'])
def add_item(request):
    data = request.data 
    serializer = ItemSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Response({'message' : 'Object created successfully'})
    else:
        return Response(serializer.errors)


@api_view(['GET'])
def list_item(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many = True)
    return Response(serializer.data)

@api_view(['PUT'])
def update_item(request, pk):
    try:
        item = Item.objects.get(pk = pk)
    except Item.DoesNotExist:
        return Response({'message' : "Item doesn't exist"})
    serializer = ItemSerializer(item, data = request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({'message' : 'Item saved successfully'})
    else:
        return Response(serializer.errors)
    

@api_view(['POST'])
def add_item(request):
    data = request.data 
    serializer = ItemSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Response({'message' : 'Object created successfully'})
    else:
        return Response(serializer.errors)


@api_view(['GET'])
def list_order(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many = True)
    return Response(serializer.data)

@api_view(['PUT'])
def update_order(request, pk):
    try:
        order = Order.objects.get(pk = pk)
    except Order.DoesNotExist:
        return Response({'message' : "order doesn't exist"})
    serializer = OrderSerializer2(order, data = request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({'message' : 'order saved successfully'})
    else:
        return Response(serializer.errors)
    
@api_view(['POST'])
def add_order(request):
    if request.method == 'POST':
        data = request.data 
        serializer = OrderSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'Object created successfully'})
        else:
            return Response(serializer.errors)
        


@api_view(['PUT', 'DELETE'])
def delete_order(request, pk):
    if request.method == 'DELETE':
        try:
            order = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return Response({"error" : "Order not found"})
        order.delete()

        return Response({"message" : "Order deleted successfully"})
    elif request.method == 'PUT':
        try:
            order = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return Response({"error" : "Order not found"})

        serializer = OrderSerializer(instance = order, data = request.data)
        if serializer.is_valid():
            order = serializer.save()
            order = OrderSerializer(order)
            return Response(order.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors)
            


