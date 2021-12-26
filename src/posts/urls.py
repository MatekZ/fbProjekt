from django.urls import path
from .views import posts_view, like_view

app_name = 'posts'

urlpatterns = [
    path('', posts_view, name='main_post_view'),
    path('liked/', like_view, name='like_post_view'),
]