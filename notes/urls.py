from django.urls import path
from . import views
app_name = "notes"

urlpatterns = [
    path('', views.show_notes, name = 'show_notes'),
    path('<int:pk>/', views.notes_detail, name='note_detail'),
    path('create/', views.create_new_note, name='create_new_note'),
    path('<int:pk>/edit/', views.edit_note, name='edit_note'),
    path('<int:pk>/delete/', views.delete_note, name='delete_note')
] 