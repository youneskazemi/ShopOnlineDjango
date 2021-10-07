from django.urls import path
from . import views

app_name = 'cart'
urlpatterns = [
    path('detail/', views.detail, name="detail")
]
