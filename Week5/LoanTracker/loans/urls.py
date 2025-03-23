from django.urls import path
from . import views


urlpatterns = [
    path('list', views.listview, name='listview'),
    path('detail', views.detailview, name='detailview'),
    path('create', views.createview, name='createview'),
    path('update', views.updateview, name='updateview'),
]
