from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('wiki/<str:title>', views.entry, name="entry"),
    path('search/', views.search, name='search'),
    path('new_entry/', views.new_entry, name='new_entry'),
    path('edit/', views.edit, name='edit'),
    path('save_edit/', views.save_edit, name='save_edit'),
    path('random_page/',views.random_page, name='random_page')
]

