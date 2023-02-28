from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test_view, name='examples_test'),
    path('exercise/', views.exercise, name='examples_exercise'),
    path('personaldata/<int:id>/', views.personal_data_detail, name='personal_data_detail'),
    path('personaldata/', views.personal_data_list, name='personal_data_list'),

]