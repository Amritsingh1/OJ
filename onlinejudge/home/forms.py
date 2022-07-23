# from .models import Snippet
from django import forms
from django_ace import AceWidget


class SnippetForm(forms.Form):
    # have to see how to remove this thing

    Code = forms.CharField(widget=AceWidget(
        mode="c_cpp",  # try for example "python"
        theme="dracula",  # try for example "twilight"
        width="900px",
        height="500px",
        minlines=None,
        maxlines=None,
        tabsize=None,
        fontsize="20px",
        behaviours=True,  # To disable auto-append of quote when quotes are entered
    ))
