from django.urls import path
from my1app import views

urlpatterns = [
    path('', views.churn_rate, name='churn_rate'),
]