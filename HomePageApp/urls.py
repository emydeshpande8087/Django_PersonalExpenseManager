from django.urls import path
from . import views
urlpatterns=[
    path('landing/', views.show_homepage)
]