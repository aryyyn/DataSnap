from django.urls import path
from . import views
urlpatterns = [
    path('co2', views.co2Visualizer ),
    path('pollution', views.pollutionVisualizer)
]