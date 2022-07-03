from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.shortcuts import render, redirect


from .models import Problem
# Create your views here.


def index(request):
    problem_list = Problem.objects.order_by('problem_id')
    return render(request, 'home/index.html', {'problem_list': problem_list})


def description(request, problem_id):
    problem = get_object_or_404(Problem, pk=problem_id)
    return render(request, 'home/description.html', {'problem': problem})
