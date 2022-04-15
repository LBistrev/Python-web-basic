from django.urls import path

from notes.demo_web.views import show_index, create_note, edit_note, delete_note, details_note, create_profile, \
    show_profile, delete_profile

urlpatterns = (
    path('', show_index, name='show index'),

    path('add', create_note, name='create note'),
    path('edit/<int:pk>/', edit_note, name='edit note'),
    path('delete/<int:pk>/', delete_note, name='delete note'),
    path('details/<int:pk>/', details_note, name='details note'),

    path('profile/create/', create_profile, name='create profile'),
    path('profile/', show_profile, name='show profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
)
