from django.shortcuts import render

# Dummy info
posts = [
    {
        'author': 'Marshall Briggs',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'February 28, 2020'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'February 29, 2020'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
