from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author': 'Regis',
        'title': 'Blog Post 1',
        'content': 'First Blog Post',
        'date_posted': 'August 18 2023'
    },
    {
        'author': 'Corey',
        'title': 'Blog Post 2',
        'content': 'Second Blog Post',
        'date_posted': 'August 28 2023'
    },
]
def home(request):
    context = {
         'posts': posts
    }
       
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})