from django.urls import path
from . import views

urlpatterns = [
    path('', views.music, name='Music'),
    path('album/<album_title>', views.album, name='Album')
]
