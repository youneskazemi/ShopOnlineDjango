from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('<int:order_id>/', views.detail, name='orders_detail'),
    path('apply/<int:order_id>/', views.coupon_apply, name='coupon_apply'),
    path('', views.create, name='orders_create'),

]
