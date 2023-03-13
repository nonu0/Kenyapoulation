from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('coast', Coast_data.as_view(), name='coast'),
    path('central', Central_data.as_view(), name='central'),
    path('nyanza', Nyanza_data.as_view(), name='nyanza'),
    path('riftvalley', Riftvalley_data.as_view(), name='riftvalley'),
    path('eastern', Eastern_data.as_view(), name='eastern'),
    path('neastern', Neastern_data.as_view(), name='neastern'),
    path('western', western_data.as_view(), name='western'),
]
