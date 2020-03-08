from django.urls import path
from home_page import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('contact/', views.contact_me, name='contact_me'),
    path('contact_success/', views.contact_success, name='contact_success'),
    # path('', views.home_page, name='home_page'),
    # path('home', views.home_page, name='home_page'),
]
