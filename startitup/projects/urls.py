from django.urls import path,include,re_path
from . import views
urlpatterns = [
    re_path(r'^$', views.index,name='index'),
    
    re_path(r'^(?P<album_id>[0-9]+)/$',views.details,name='details'),
]
