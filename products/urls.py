from django.urls import path

from products.views import *

urlpatterns = [
    path('', MainView.as_view(), name='search'),
    path('/search', ProductView.as_view(), name='search'),
]