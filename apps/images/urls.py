from django.conf.urls import url
from . import views

app_name = 'images'

urlpatterns = [
    url(r'^create/', views.image_create, name='create'),
    url(r'^upload/', views.image_upload, name='upload'),
    url(r'^detail/(?P<id>[0-9]+)/(?P<slug>[-\w]+)/',views.image_detail,name='detail'),
    url(r'^delete/(?P<id>[0-9]+)/(?P<slug>[-\w]+)/',views.image_delete,name='delete'),
    url(r'^like/', views.image_like, name='like'),
    url(r'^$', views.image_list, name='list'),
    url(r'^ranking/', views.image_ranking, name='ranking'),
]