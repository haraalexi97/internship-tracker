from django.urls import path
from . import views
    
urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_application,name='add'),
    path('edit/<int:id>/', views.edit_application, name='edit'),
    path('delete/<int:id>/', views.delete_application, name='delete'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
]
