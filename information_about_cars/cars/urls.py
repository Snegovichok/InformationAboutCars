from django.urls import path
from . import views
from .views import CarListCreateAPIView, CarRetrieveUpdateDestroyAPIView, CommentListCreateAPIView

urlpatterns = [
    path('', views.information_about_cars, name='information_about_cars'),
    path('admin/', views.admin_panel, name='admin_panel'),
    path('register/', views.registration, name='registration'),
    path('login/', views.authorization, name='authorization'),
    path('logout/', views.user_logout, name='logout'),
    path('user/', views.user_dashboard, name='user_dashboard'),
    path('create_car/', views.create_car, name='create_car'),
    path('edit_car/<int:car_id>/', views.edit_car, name='edit_car'),
    path('delete_car/<int:car_id>/', views.delete_car, name='delete_car'),
    path('', views.information_about_cars, name='home'),
    path('cars/<int:car_id>/', views.car_detail, name='car_detail'),

    path('api/cars/', CarListCreateAPIView.as_view(), name='api-cars-list-create'),
    path('api/cars/<int:pk>/', CarRetrieveUpdateDestroyAPIView.as_view(), name='api-cars-detail'),
    path('api/cars/<int:car_id>/comments/', CommentListCreateAPIView.as_view(), name='api-car-comments'),
]
