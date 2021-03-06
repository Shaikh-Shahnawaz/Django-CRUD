from .import views
from django.urls import path

urlpatterns = [
    path('', views.showstudents, name='showStudents'),
    path('<int:id>/', views.deletestudents, name='deleteStudents'),
    path('editstudent/<int:id>/', views.editstudents, name='editStudents'),
]
