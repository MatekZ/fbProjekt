from django.shortcuts import render
from .models import Profile, Relationship
from .forms import ProfileModelForms

def my_profile_view(request):
    my_profile = Profile.objects.get(user=request.user)

    form = ProfileModelForms(request.POST or None, request.FILES or None, instance=my_profile)
    updated = False

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            updated = True

    context = {
        'my_profile': my_profile,
        'form': form,
        'updated': updated,
    }

    return render(request, 'profiles/myprofile.html', context)


def invites_received_view(request):
    my_profile = Profile.objects.get(user=request.user)
    query_set = Relationship.objects.invites_received(my_profile)

    context = {
        'qs': query_set
    }

    return render(request, 'profiles/myinvites.html', context)

def profiles_view(request):
    user = request.user
    query_set = Profile.objects.get_profiles(user)

    context = {
        'qs': query_set
    }

    return render(request, 'profiles/allprofiles.html', context)


def available_invites_view(request):
    user = request.user
    query_set = Profile.objects.get_profiles_available_to_invite(user)

    context = {
        'qs': query_set
    }

    return render(request, 'profiles/available_to_add.html', context)