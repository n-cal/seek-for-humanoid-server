from django.urls import path
from humanoids import views

urlpatterns = [
    path('/countries', views.all_countries)
]