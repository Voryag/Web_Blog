from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.shortcuts import redirect

from models import Note


def render_index(request):
    return render(request, "index.html")

def redirect_create_page(request):
    note = request.POST.get('note')
    if note != None:
        print(note)
        note_in_base = Note(note)
        note.save()

    if request.method == "POST":
        if request.POST.get('create'):
            print('Create button is touched')

        return render(request, "create_notification_page.html")

        #if request.POST.get('create'):
        #    print('Create button is touched')
        #    return HttpResponseRedirect(reverse('create_notification_page.html'))
        #elif request.POST.get('delete'): # ПЕРЕАДРЕСАЦИЮ НЕ ВЫПОЛНЯТЬ
        #    return HttpResponseRedirect(reverse('delete'))

    return render(request, "index.html")
