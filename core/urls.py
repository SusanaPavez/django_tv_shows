from django.urls import path
from . import views
urlpatterns = [
    path('', views.tv_show),
    path('add_show/', views.add_show),
    path('display_show/<int:id>', views.display_show),
    path('edit_show/<int:id>', views.edit_show),
    path('delete_show/<int:id>', views.delete_show),
]
