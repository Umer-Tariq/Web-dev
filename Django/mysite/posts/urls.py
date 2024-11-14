from django.urls import path, include
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.homePage, name="homepage"),
    path('new-post', views.new_post, name="new-post"),
    path('<slug:id>', views.post_page, name = "page")
]
