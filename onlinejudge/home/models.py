from datetime import datetime
from django.db import models
from django.forms import CharField
from django.utils import timezone
# Create your models here.
from mdeditor.fields import MDTextField


class Problem(models.Model):
    # large text
    difficulty_choices = (
        ('Hard', 'Hard'), ('Medium', 'Medium'), ('Easy', 'Easy'))
    problem_id = models.IntegerField()
    statement = MDTextField()
    name = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=6, choices=difficulty_choices)
    input = models.TextField(default="")
    output = models.TextField(default="")

    def __str__(self):
        return str(self.name)


class Solution(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    solution_id = models.IntegerField()
    verdict = models.CharField(max_length=12)
    datetime = models.DateTimeField()

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Solution, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.solution_id)
