from rest_framework import serializers
from .models import Item, Order

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'price']

    def validate_price(self, value):
        if value > 200:
            raise serializers.ValidationError("Price too high")
        return value
    

class OrderSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)
    class Meta:
        model = Order
        fields = ['id','date_time', 'items']

    """ def create(self, validated_data):
        item_data = validated_data.pop('items', None)
        order = Order.objects.create(**validated_data)

        item_list = []
        if item_data is not None:
            for item in item_data:
                item_found = Item.objects.get(**item)
                item_list.append(item_found)

        order.items.set(item_list)

        return order
     """
    def update(self, instance, validated_data):
        item_data = validated_data.pop('items', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        instance.items.clear()

        if item_data is not None:
            for item in item_data:
                item_found = Item.objects.get(**item)
                instance.items.add(item_found)

        return instance

                
class OrderSerializer2(serializers.ModelSerializer):
    items = serializers.PrimaryKeyRelatedField(queryset = Item.objects.all(), many = True)
    class Meta:
        model = Order
        fields = ['id','date_time', 'items']
        