from django.shortcuts import render
from .models import Profile, Relationship
from .forms import ProfileModelForms
from django.views.generic import ListView
from django.contrib.auth.models import User

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


def available_invites_view(request):
    user = request.user
    query_set = Profile.objects.get_profiles_available_to_invite(user)

    context = {
        'qs': query_set
    }

    return render(request, 'profiles/available_to_add.html', context)


def profiles_view(request):
    user = request.user
    query_set = Profile.objects.get_profiles(user)

    context = {
        'qs': query_set
    }

    return render(request, 'profiles/allprofiles.html', context)


class ProfilesView(ListView):
    model = Profile
    template_name = 'profiles/allprofiles.html'
    # context_object_name = 'qs'

    def get_queryset(self):
        query_set = Profile.objects.get_profiles(self.request.user)
        return query_set

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = User.objects.get(username__iexact=self.request.user)
        profile = Profile.objects.get(user=user)
        relation_receiver = Relationship.objects.filter(sender=profile)
        relation_sender = Relationship.objects.filter(receiver=profile)
        receiver_list = []
        sender_list = []

        for item in relation_receiver:
            receiver_list.append(item.receiver.user)

        for item in relation_sender:
            sender_list.append(item.sender.user)

        context["receiver_list"] = receiver_list
        context["sender_list"] = sender_list
        context["qs_empty"] = False

        if len(self.get_queryset()) == 0:
            context["qs_empty"] = True


        return context
