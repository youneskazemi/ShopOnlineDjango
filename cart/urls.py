from django.urls import path
from . import views

app_name = 'cart'
urlpatterns = [
    path('', views.detail, name="detail"),
    path('cart/add/<int:product_id>/', views.cart_add, name="cart_add"),
]
