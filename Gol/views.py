from django.shortcuts import render
from .models import Post

def post(request):
    posts = Post.objects.all()
    return render(request, 'home.html' )

def required(request):
    return render(request, 'REQUIREMENT.html')

def park(request):
    return render(request, 'PARK.html')

def photos(request):
    return render(request, 'PHOTOS.html')



from django.urls import path
from .views import post, required, park, photos

urlpatterns = [
    path('', post, name='post'),
    path('requirements/', required, name='requirement'),
    path('photos/', photos, name='photos'),
    path('park/', park, name='park'),
]





