from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.shortcuts import redirect


def render_index(request):
    return render(request, "index.html")

def redirect_create_page(request):
    if request.method == "POST":
        return HttpResponse("1")

        #if request.POST.get('create'):
        #    print('Create button is touched')
        #    return HttpResponseRedirect(reverse('create_notification_page.html'))
        #elif request.POST.get('delete'): # ПЕРЕАДРЕСАЦИЮ НЕ ВЫПОЛНЯТЬ
        #    return HttpResponseRedirect(reverse('delete'))

    return render(request, "index.html")

def render_create_page(request):
    return render(request, "create_notification_page.html")