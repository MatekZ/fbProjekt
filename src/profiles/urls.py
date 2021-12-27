from django.urls import path
from .views import my_profile_view, invites_received_view, profiles_view, available_invites_view, ProfilesView

app_name = 'profiles'

urlpatterns = [
    path('myprofile/', my_profile_view, name='my_profile_view'),
    path('myinvites/', invites_received_view, name='invites_received_view'),
    path('allprofiles/', ProfilesView.as_view(), name='profiles_view'),
    path('availableinv/', available_invites_view, name='available_invites_view')

]