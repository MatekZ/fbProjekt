from django.shortcuts import render
from .models import Profile
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
