from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import NotesForm
from django.contrib import messages  

def show_notes(request):
    notes = Note.objects.all().order_by('-date_updated')
    return render(request, 'notes/index.html', {'notes':notes})


def notes_detail(request,pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'notes/detail.html', {'note':note} )


def create_new_note(request):
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Notes created')
            return redirect('notes:show_notes')
    else:
        form = NotesForm()
    return render(request, 'notes/create.html', {'form': form,
                                                 'action' : 'create'})

def delete_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        note.delete()
        messages.success(request,'Note Deleted Successfully')
    return redirect('notes:show_notes')
    

def edit_note(request, pk):
    note = get_object_or_404(Note, pk=pk)

    if request.method == 'POST':
        form = NotesForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('notes:note_detail', pk=pk)
        
    else:
        form = NotesForm(instance=note)

    return render(
        request,
        'notes/create.html',
        {
            'form' : form,
            'action' : 'edit'
        }
    )



