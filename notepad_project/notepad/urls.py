from django.urls import path
from . import views

urlpatterns = [
    path('', views.note_list, name='note_list'),
    path('open/', views.open_file, name='open_file'),
    path('save/', views.save_file, name='save_file'),
    path('clear/', views.clear_editor, name='clear_editor'),
]
