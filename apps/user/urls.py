from django.urls import path
from . import views as user_views

urlpatterns = [
    path('', user_views.hello, name='hello'),
]