from django.contrib import admin
from .models import Problem, Solution

# import mathfield
# from django import forms


# class ProblemAdminForm(forms.ModelForm):

#     class Meta:
#         widgets = {
#             'statement': mathfield.MathFieldWidget
#         }


# class ProblemAdmin(admin.ModelAdmin):
#     form = ProblemAdminForm


# Register your models here.
admin.site.register(Solution)
admin.site.register(Problem)
