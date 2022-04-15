from django.shortcuts import render, redirect

from notes.demo_web.forms import CreateProfileForm, CreateNoteForm, DeleteNoteForm
from notes.demo_web.models import Profile, Note


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]
    return None


def show_index(request):
    profile = get_profile()
    notes = Note.objects.all()
    if not profile:
        return redirect('create profile')

    context = {
        'profile': profile,
        'notes': notes,
    }
    return render(request, 'home-with-profile.html', context)


def create_note(request):
    if request.method == 'POST':
        form = CreateNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = CreateNoteForm()

    context = {
        'form': form,
    }
    return render(request, 'note-create.html', context)


def edit_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        form = CreateNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = CreateNoteForm(instance=note)

    context = {
        'form': form,
        'note': note,
    }
    return render(request, 'note-edit.html', context)


def delete_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = DeleteNoteForm(instance=note)

    context = {
        'form': form,
        'note': note,
    }
    return render(request, 'note-delete.html', context)


def details_note(request, pk):
    note = Note.objects.get(pk=pk)
    context = {
        'note': note,
    }
    return render(request, 'note-details.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
    }
    return render(request, 'home-no-profile.html', context)


def show_profile(request):
    profile = get_profile()
    notes_count = len(Note.objects.all())

    context = {
        'profile': profile,
        'notes_count': notes_count,
    }
    return render(request, 'profile.html', context)


def delete_profile(request):
    Profile.objects.all().delete()
    Note.objects.all().delete()
    return redirect('show index')
