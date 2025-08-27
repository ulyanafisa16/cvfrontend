from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio_list, name='portfolio_list'),
    path('portfolio/<int:id>/', views.portfolio_detail, name='portfolio_detail'),
    path('service-details.html', views.service_detail, name='service_detail'),
]
