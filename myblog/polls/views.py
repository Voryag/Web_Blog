from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


def render_home(request):
    return render(request, 'index.html')


def contact(request):
    if request.method == 'POST':
        if request.POST.get('create'):
            return HttpResponseRedirect(reverse('create'))
        elif request.POST.get('delete'):
            return HttpResponseRedirect(reverse('delete'))