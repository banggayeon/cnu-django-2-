"""
URL configuration for example_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from example_app.views import course, department, professor, student, signup, login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('course/', course.CourseListAPIView.as_view()),
    path('course/<int:pk>/', course.CourseDetailAPIView.as_view()),
    path('department/', department.DepartmentListAPIView.as_view()),
    path('department/<int:pk>/', department.DepartmentDetailAPIView.as_view()),
    path('professor/', professor.ProfessorListAPIView.as_view()),
    path('professor/<int:pk>/', professor.ProfessorDetailAPIView.as_view()),
    path('student/', student.StudentListAPIView.as_view()),
    path('student/<int:pk>/', student.StudentDetailAPIView.as_view()),
    path('signup/student/', signup.StudentSignupView.as_view(), name='student_signup'),
    path('signup/professor/', signup.ProfessorSignupView.as_view(), name='professor_signup'),
    path('login/', login.LoginView.as_view(), name='login'),
]
