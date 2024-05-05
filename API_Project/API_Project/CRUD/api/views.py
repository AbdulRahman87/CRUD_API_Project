from django.shortcuts import render, redirect
from .models import Note
from django.core.paginator import Paginator
from .serializer import NoteSerializer
from rest_framework.viewsets import ModelViewSet
from django.http import HttpResponseRedirect
# Create your views here.

def Index(request):
    notes = Note.objects.all()
    paginator = Paginator(notes, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']
        note = Note.objects.create(note_title = title, note_desc = desc)
        note.save()
        return redirect("Home")
    return render(request, "index.html", {"notes": page_obj, 'page_no': page_number})

def note_delete(request):
    if request.method == "POST":
        note_id = request.POST['note_id']
        note = Note.objects.get(note_id=note_id)
        note.delete()
        return HttpResponseRedirect(request.path_info)
    return redirect("Home")

class NotesApi(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

def update_note(request):
    if request.method == "POST":
        note_id = request.POST['note_id']
        note_title = request.POST['note_title'];
        note_desc = request.POST['note_desc']
        note = Note.objects.get(note_id=note_id)
        note.note_title = note_title
        note.note_desc = note_desc
        note.save()
        return redirect("Home")
    return redirect("Home")

