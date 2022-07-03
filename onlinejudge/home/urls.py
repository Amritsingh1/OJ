from django.urls import URLPattern, path
from .home.views import views

urlpatterns = [
    path('', views.index, name='index'),

    path('problem/<int:problem_id>/',
         views.description, name='description'),

]
