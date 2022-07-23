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
    verdict = models.CharField(max_length=12)
    datetime = models.DateTimeField()
    code = models.TextField(default="")

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Solution, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.problem)

# Code Editor Class


# class Snippet(models.Model):
#     # class EditorForm(forms.Form):
#     # text = forms.CharField(widget=AceWidget)
#     text = models.TextField(default="Hello World")
#     created_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ('-created_at', )
