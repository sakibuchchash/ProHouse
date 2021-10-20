from django.urls import include, path
from .views import classroom, students, teachers,posts
from django.views.generic.base import TemplateView

urlpatterns = [
    path('contests/',posts.contest,name='contest'),
    path('contests/details/<pk>/',posts.condetails,name='contest'),
    path('contests/new/', posts.con_new, name='post_new'),
    path('contests/details/<int:pk>/edit/', posts.con_edit, name='post_edit'),

    path('posts/',posts.index,name='index'),
    path('posts/details/<pk>/', posts.details, name='details'),
    path('posts/new/', posts.post_new, name='post_new'),
    path('posts/details/<int:pk>/edit/', posts.post_edit, name='post_edit'),

    
    path('<user>/list/',students.lis,name='list'),
    path('<user>/suggetion/',students.prosugg,name='suggetion'),
    path('train/',students.train,name='train'),
    path('train/new/', students.train_new, name='train_new'),
    path('train/<int:pk>/edit/', students.train_edit, name='train_edit'),

    path('proupdate/<user>/',students.proupdate),
    path('update/',students.update),
    path('', classroom.home, name='home'),
    path('ranks/',students.ranks,name='ranks'),
    path('programmers/',students.Programmers,name='Programmers'),
    path('contests/',students.Contests,name='Contests'),

    path('profile/<user>/',students.ProgrammersProfile, name='ProgrammersProfile'),
    path('<user>/profile_edit/',students.ProgrammersProfile_edit, name='ProgrammersProfile_edit'),
    path('<user>/profile_edit/Password/',students.ProgrammersPassword.as_view(), name='ProgrammersPassword'),
    path('teachers/',students.teacher,name='teachers'),
    path('teacher/profile/<user>/',teachers.TeachersProfile, name='TeachersProfile'),
    path('teacher/<user>/profile_edit/',teachers.TeachersProfile_edit, name='TeachersProfile_edit'),
    path('teacher/<user>/profile_edit/Password/',teachers.TeachersPassword.as_view(), name='TeachersPassword'),

    #path('profile/', TemplateView.as_view(template_name='registration/profile.html'), name='ProgrammersProfile'),
    #path('students/',students.ProgrammersProfile, name='ProgrammersProfile'),
    #path('teachers/TeachersProfile/',TemplateView.as_view(template_name='registration/profile.html'), name='TeachersProfile'),
    ];
