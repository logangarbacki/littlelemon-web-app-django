from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'bookings', views.BookingViewSet, basename='booking')
router.register(r'orders', views.OrderViewSet, basename='order')

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemView.as_view(), name='menu'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu-item'),
] + router.urls
