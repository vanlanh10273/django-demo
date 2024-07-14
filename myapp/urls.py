from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path('', views.index, name='home'),
    path('post', views.post_list, name='post_list'),
    # ex: /polls/5/
    path("<int:post_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:post_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:post_id>/vote/", views.vote, name="vote"),
    path('create', views.create_post_view, name='create_post'),
]
