from django.urls import path,include
from .views import *
app_name='course'
urlpatterns = [
    path('subjects/',AllSubjects,name='subjects'),
    path('add-subject/',AddSubject,name='add_subject'),
    path('edit-subject/<int:id>',EditSubject,name='edit_subject'),
    path('delete-subject/<int:id>',DeleteSubject,name='delete_subject'),
    #Course
    path('course-list/',CourseList,name='course_list'),
    path('add-course/',AddCourse,name='add_course'),

    

] 