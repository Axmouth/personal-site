from django.urls import path
from . import views

urlpatterns = [
    path("", views.project_index, name="project_index"),
    path("detail/<str:sub_url>/", views.project_detail, name="project_detail"),
    path("technology/<str:technology>/", views.project_technology, name="project_technology"),
]