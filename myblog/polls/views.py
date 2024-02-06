from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect


def index_home(request):
    return render(request, 'index.html')

def redirect_create_page(request):
    if request.method == 'POST':
        print('1')
        return HttpResponseRedirect("1")

        if request.POST.get('create'):
            print('Create button is touched')
            return HttpResponseRedirect(reverse('create_notification_page.html'))
        elif request.POST.get('delete'): # ПЕРЕАДРЕСАЦИЮ НЕ ВЫПОЛНЯТЬ
            return HttpResponseRedirect(reverse('delete'))

    return render(request, "index.html")

def new_create_page(request):
    return render(request, "create_notification_page.html")