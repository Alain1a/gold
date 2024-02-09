from django.urls import path
from .views import post, required, park, photos

urlpatterns = [
    path('', post, name='post'),
    path('requirements/', required, name='requirement'),
    path('photos/', photos, name='photos'),
    path('park/', park, name='park'),
]
