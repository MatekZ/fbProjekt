from django.shortcuts import render, redirect
from .models import Post, Like
from profiles.models import Profile


def posts_view(requset):
    query_set = Post.objects.all()
    profile = Profile.objects.get(user=requset.user)

    context = {
        'qs': query_set,
        'profile': profile,
    }

    return render(requset, 'posts/main.html', context)


def like_view(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id=post_id)
        profile = Profile.objects.get(user=user)

        if profile in post_obj.liked.all():
            post_obj.liked.remove(profile)
        else:
            post_obj.liked.add(profile)

        like, created = Like.objects.get_or_create(user=profile, post_id=post_id)

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'
        else:
            like.value = 'Like'

        post_obj.save()
        like.save()

    return redirect('posts:main_post_view')
