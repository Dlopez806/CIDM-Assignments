"""
URL configuration for degree_checklist project.

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
from degree_checklist import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cis-records/', views.cis_records_view, name='cis_records'),
    path('add_college/', views.add_college, name='add_college'),
    path('add_department/', views.add_department, name='add_department'),
    path('add_course/', views.add_course, name='add_course'),
    path('add_section_group/', views.add_section_group, name='add_section_group'),
    path('add_section/', views.add_section, name='add_section'),
    path('add_course_option_group/', views.add_course_option_group,
         name='add_course_option_group'),
    path('add_program/', views.add_program, name='add_program'),
    path('add_student/', views.add_student, name='add_student'),
    path('add_student_role/', views.add_student_role, name='add_student_role'),
    path('add_semester/', views.add_semester, name='add_semester'),
    path('add_external_college/', views.add_external_college,
         name='add_external_college'),
    path('add_transfer_equivalency/', views.add_transfer_equivalency,
         name='add_transfer_equivalency'),
    path('add_student_course/', views.add_student_course,
         name='add_student_course'),
    path('add_prerequisite/', views.add_prerequisite, name='add_prerequisite'),
    path('add_student_degree_plan/', views.add_student_degree_plan,
         name='add_student_degree_plan'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
