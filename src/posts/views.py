from django.shortcuts import render
from .models import Post

def posts_view(requset):
    query_set = Post.objects.all()

    context = {
        'qs': query_set,
    }

    return render(requset, 'posts/main.html', context)