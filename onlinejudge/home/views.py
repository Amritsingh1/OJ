from .forms import SnippetForm
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.shortcuts import render, redirect
import os
from django.utils import timezone
from .models import Problem, Solution
# Create your views here.
import subprocess as sp


def index(request):
    problem_list = Problem.objects.order_by('problem_id')
    return render(request, 'home/index.html', {'problem_list': problem_list})


def description(request, problem_id):
    problem = get_object_or_404(Problem, pk=problem_id)
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SnippetForm()
    return render(request, "home/description.html", {
        'problem': problem,
        "form": form,
    })

    return render(request, 'home/description.html', {})


def simple(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SnippetForm()
    return render(request, "home/snippets.html", {
        "form": form,
        # "snippets": Snippet.objects.all()
    })


def checker(question_id, code, input, output):

    verdict = ""
    os.chdir('judge')
    file = open('test.cpp', 'w')
    file.write(code)
    file.close()
    file_input = open('input.txt', 'w')
    file_input.write(input)
    file_input.close()
    os.system('g++ -o main test.cpp')
    os.system("main.exe<input.txt>output1.txt")
    file_output = open('output1.txt').readlines()
    file_output = [s.strip().rstrip('\n').strip() for s in file_output]
    file_output = ''.join(file_output)
    if file_output == output:
        verdict = "Accepted"
    else:
        verdict = "Wrong Answer"
    os.system('del /f test.cpp')
    os.system('del /f input.txt')
    os.system('del /f output.txt')
    os.system('del /f output1.txt')
    os.system('del /f main.exe')

    os.chdir('..')
    return verdict

    # problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    # # solution_id = models.IntegerField()
    # solution_id = models.AutoField(primary_key=True)
    # verdict = models.CharField(max_length=12)
    # datetime = models.DateTimeField()


def submission(request, problem_id):
    id = problem_id
    problem = get_object_or_404(Problem, pk=problem_id)
    code = request.POST.get('Code')

    verdict = checker(id, code, problem.input, problem.output)
    curr_time = timezone.now()
    submit = Solution(problem_id=problem.problem_id, code=code,
                      verdict=verdict, datetime=curr_time)
    submit.save()
    return redirect('/leaderboard')
    return HttpResponse(verdict)


def LeaderBoard(request):
    arr = Solution.objects.all()
    latest = []
    for i in reversed(arr):
        latest.append(i)
        if(len(latest) == 10):
            break
    context = {
        "results": latest
    }
    return render(request, 'home/leaderboard.html', context)
