from django.urls import path
from notes import views


urlpatterns = [
    path('notes/<int:id>', views.note_detail, name='note_detail'),
    path('notes/', views.note_list, name='note_list'),
    path('notes/unpublished/', views.note_unpublished_list, name='note_unpublished_list'),
    path('notes/published/', views.note_published_list, name='note_published_list'),
    path('notes/redacted/', views.note_redacted_list, name='note_redacted_list'),

]