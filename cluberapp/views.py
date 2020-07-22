from django.shortcuts import render
from .parser import urls_of_vids

# Create your views here.
def index(request):
    prop_list = urls_of_vids()
    context = {
        'url': prop_list[0],
        'title': prop_list[1]
    }
    return render(request, 'cluberapp/index.html', context)