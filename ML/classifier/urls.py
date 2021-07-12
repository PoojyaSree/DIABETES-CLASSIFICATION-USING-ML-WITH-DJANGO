from django.urls import path,include
from classifier import views
urlpatterns = [
    path('index', views.index, name='index'),
    path('predict', views.predict, name='predict'),
]
