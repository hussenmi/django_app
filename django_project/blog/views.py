from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        'author': 'Hussen',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'May 28, 2021'
    },
    {
        'author': 'Chris',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'May 29, 2021'
    }
]
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})