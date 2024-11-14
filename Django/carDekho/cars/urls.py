from django.urls import path, include
from . import views


urlpatterns = [
    path('list/', view=views.list_cars, name="list"),
    path('<int:pk>/', views.get_car_detail, name="car-detail"),
    path('delete/<int:pk>/', views.delete_car, name="delete-car"),
    path('query/', views.get_query, name="query")
]