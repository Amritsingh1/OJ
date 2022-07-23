from django.urls import URLPattern, path
from . import views
urlpatterns = [
    path('', views.index, name='index'),

    path('problem/<int:problem_id>/',
         views.description, name='description'),
    path('problem/<int:problem_id>/submission',
         views.submission, name='submission'),
    path('leaderboard', views.LeaderBoard, name='leaderboard')
    # path('problem/<int:problem_id>/submission', views.simple, name='simple'),
]
