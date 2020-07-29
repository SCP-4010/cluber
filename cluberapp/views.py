from django.shortcuts import render
from .models import Album, Music, Video
from .parser import urls_of_vids

# Create your views here.
def index(request):
    prop_list = urls_of_vids()
    context = {
        'url': prop_list[0],
        'title': prop_list[1]
    }
    return render(request, 'cluberapp/index.html', context)

def music(request):
    context = {
        'albums': Album.objects.all(),
        'music': Music.objects.all().order_by('album'),
    }
    return render(request, 'cluberapp/music.html', context)

def video(request):
    context = {
        'video': Video.objects.all(),
    }
    return render(request, 'cluberapp/video.html', context)