from django.shortcuts import render, HttpResponse, redirect
from .forms import Video_form
from .models import Video

# Create your views here.

def video(request):
    all_video = Video.objects.all()
    if request.method == 'POST':
        form = Video_form(data = request.POST, files = request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1> Upload Successfully </h1>')
    else:
        form = Video_form()
    return render(request, 'Upload/upload.html', {'form':form, 'all':all_video})
