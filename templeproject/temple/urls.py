from django.urls import path
from .views import add_temple, show_temple, update_temple, delete_temple


urlpatterns = [
    path('add/', add_temple, name='add_url'),
    path('show/', show_temple, name='show_url'),
    path('update/<int:pk>/', update_temple, name='update_url'),
    path('delete/<int:pk>/', delete_temple, name='delete_url'),
]
