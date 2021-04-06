from django.urls import path
from . import views

urlpatterns = [
path('', views.SchoolSchedules.index, name='index'),
path('student/', views.SchoolSchedules.studentdetails, name='studentdetails'),
path('askpage/', views.SchoolSchedules.askpage, name='askpage'),
path('askteacher/', views.SchoolSchedules.askteacher, name='askteacher'),
path('teacher/', views.teacher.teacherdetails, name='teacherdetails'),
path('addstudent/', views.SchoolSchedules.addstudent, name='addstudent'),
path('addteacher/', views.SchoolSchedules.addteacher, name='addteacher'),
path('getteacher/', views.SchoolSchedules.getteacher, name='getteacher'),
path('addstudentdetails/', views.SchoolSchedules.addstudentdetails, name='addstudentdetails'),
path('aboutus', views.SchoolSchedules.aboutus, name='aboutus'),
path('askclass/', views.SchoolSchedules.askclass, name='askclass'),
path('classdetails/', views.SchoolSchedules.classdetails, name='classdetails'),
path('classteacherlist/', views.ClassTeachersList.as_view(), name='classteacherlist'),
path('rmvclassteacher/<int:pk>', views.teacher.rmvclassteacher, name='rmvclassteacher'),
path('rmvteacher/<int:pk>', views.teacher.rmvteacher, name='rmvteacher'),
path('rmvstudent/<int:pk>', views.SchoolSchedules.rmvstudent, name='rmvstudent'),
path('rmvclass/<int:pk>', views.SchoolSchedules.rmvclass, name='rmvclass'),
path('addclass/', views.SchoolSchedules.addclass, name='addclass'),
path('getclass/', views.SchoolSchedules.getclass, name='getclass'),
]
