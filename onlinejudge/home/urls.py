from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('problem/<int:problem_id>/',
         views.description, name='description'),


]
