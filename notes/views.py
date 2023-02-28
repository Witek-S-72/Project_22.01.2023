from django.shortcuts import render, get_object_or_404
from notes.models import Note

# Create your views here.

def note_detail(request, id):
    """widok detaila notatki"""
    note = get_object_or_404(Note, id=id)
    ctx = {'note': note}
    return render(request, 'notes/note_detail.html', ctx)

def note_list(request):
    """widok listy notatek"""
    notes = Note.objects.all()
    ctx = {'notes': notes}
    return render(request, 'notes/note_list.html', ctx)

def note_unpublished_list(request):
    notes = Note.objects.filter(status='nieopublikowana')
    counter = notes.count()
    ctx = {'notes': notes, 'counter':counter, 'page_title':'Lista nieopublikowanych notatek'}
    return render(request,'notes/note_list.html',ctx)

def note_published_list(request):
    notes = Note.objects.filter(status='opublikowana')
    counter = notes.count()
    ctx = {'notes':notes, 'counter':counter, 'page_title': 'Lista opublikowanych notatek'}
    return render(request,'notes/note_list.html',ctx)

def note_redacted_list(request):
    notes = Note.objects.filter(status='w redakcji')
    counter = notes.count()
    ctx = {'notes':notes, 'counter':counter, 'page_title':'Lista notatek w redakcji'}
    return render(request,'notes/note_list.html',ctx)

