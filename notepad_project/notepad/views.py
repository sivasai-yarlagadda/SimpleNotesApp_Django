import os
from django.shortcuts import render
from .models import Note
from django.http import HttpResponse

def note_list(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        content = file.read().decode('utf-8')
        return render(request, 'editor.html', {'content': content})
    return render(request, 'open_file.html')
    # return render(request, 'notepad/note_list.html', {})



def open_file(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        content = file.read().decode('utf-8')
        return render(request, 'error.html', {'content': content})
    return render(request, 'open_file.html')

def save_file(request):
    if request.method == 'POST':
        content = request.POST.get('content', '')
        file_name = request.POST.get('file_name', 'default.txt')

        response = HttpResponse(content, content_type='text/plain')
        response['Content-Disposition'] = f'attachment; filename="{file_name}"'
        return response

    return render(request, 'save_file.html')

def clear_editor(request):
    return render(request, 'editor.html', {'content': ''})
