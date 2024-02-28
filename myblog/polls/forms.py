from django import forms
from myblog.polls.models import *

class AddNotes(models.Model):
    note = forms.CharField(max_length=255)
    is_published = forms.BooleanField()
