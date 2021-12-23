from django.shortcuts import render
from .models import Profile

def my_profile_view(request):
    my_profile = Profile.objects.get(user=request.user)

    context = {
        'my_profile': my_profile,
    }

    return render(request, 'profiles/myprofile.html', context)
