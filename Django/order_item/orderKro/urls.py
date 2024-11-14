from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('Item/add', views.add_item, name = "add-item"),
    path('Item/list', views.list_item, name = "list-item"),
    path('Item/update/<int:pk>', views.update_item, name = "update-item"),
    path('order/add', views.add_order, name = "add-order"),
    path('order/list', views.list_order, name = "list-order"),
    path('order/update/<int:pk>', views.update_order, name = "update-order"),
    path('order/delete/<int:pk>', views.delete_order, name = "delete-order"),
]