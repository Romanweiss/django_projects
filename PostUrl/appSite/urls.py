from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.PageHome.as_view(), name='urlPageHome')
]
