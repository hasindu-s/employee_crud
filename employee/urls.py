from django.urls import path
from . import views

urlpatterns = [
    path('', views.employees_list),
    path('new/', views.new_employee),
    path('<int:employee_id>/', views.employee_rud)
]