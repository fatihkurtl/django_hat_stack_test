from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('create-user/', views.create_user, name='create_user'),
    path('update-user/<int:user_id>/', views.update_user_role, name='update_user'),
    path('delete-user/<int:user_id>/', views.delete_user, name='delete_user'),
]
