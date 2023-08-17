
from django.urls import path
from .import views
urlpatterns = [
    path('', views.home, name='home'),
    path('save/', views.save_data, name='save_data'),
    path('delete/', views.delete_data, name='delete_data'),
    path('edit/', views.edit_data, name='edit_data'),

    # path('first/', views.First, name='first'),

]
