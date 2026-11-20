from django.contrib import admin
from django.urls import path
from my1app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.churn_rate, name='churn_rate'),
]