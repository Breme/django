from multiprocessing.sharedctypes import template

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader

from .models import Album

def index1(request):
    all_albums=Album.objects.all()
    html=''
    for album in all_albums:
        url='/projects/'+str(album.id)+'/'
        html+='<a href="'+url+'">'+album.album_title +'</a><br>'
    return HttpResponse(html)
# Create your views here.
def details(request, album_id):
#     try:
#         
#         album=Album.objects.get(pk=album_id)
#     except Album.DoesNotExist:
#         raise Http404("Album does not Exist")
#or
    album=get_object_or_404(Album,pk=album_id)
    return render(request,'projects/detail.html',{"album":album})
def index(request):
    all_albums=Album.objects.all()
    template=loader.get_template('projects/index.html')
    context={
             "all_albums":all_albums
             }
    return HttpResponse(template.render(context,request))

# def favourite(request, album_id):
#     album=get_object_or_404(Album,pk=album_id)
#     try:
#         selected_song