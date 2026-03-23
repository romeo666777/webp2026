from django.urls import path
from . import views

urlpatterns = [
    path('addcourse', views.add_course,name='addcourse'),
    path('courselist', views.course_list,name='courselist'),
]