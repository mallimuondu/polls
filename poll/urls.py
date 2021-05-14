from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('create/', create, name='create'),
    path('vote/<poll_id>/', vote, name='vote'),
    path('results/<poll_id>', result, name='result'),
]
