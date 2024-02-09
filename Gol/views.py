from django.shortcuts import render
from .models import Post

def post(request):
    # A single line comment
    """
    A function for handling posts page:
    * This function receives post requests and saves them.
    * This function renders the page
    """
    if request.method == 'POST':
        post_received = Post()
        post_received.title = request.POST.get("title")
        post_received.author = request.POST.get("author")
        post_received.content = request.POST.get("content")
        try:
            post_received.save()
        except:
            return print("Error saving...")
        
    if request.method == 'GET':
        posts = Post.objects.all()
        return render(request, 'home.html', {"posts": posts})

def required(request):
    return render(request, 'REQUIREMENT.html')

def park(request):
    return render(request, 'PARK.html')

def photos(request):
    return render(request, 'PHOTOS.html')
