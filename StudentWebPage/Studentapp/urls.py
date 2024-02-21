from django.urls import path

from Studentapp import views

urlpatterns = [
    path('',views.login_fun,name='log'),
    path('reg',views.register_fun,name='reg'),
    path('home',views.home_fun,name='home'),
    path('add_course',views.addcourse_fun,name='add_course'),
    path('display_course',views.displaycouse_fun,name='display_course'),
    path('update_course/<int:courseid>',views.update_course,name='update_course'),
    path('delete_course/<int:courseid>',views.delete_coure,name='delete_course'),
    path('addstudent',views.addstudent_fun,name='addstudent'),
    path('displaystudent',views.displaystudent_fun,name='displaystudent'),
    path('updatestudent/<int:studid>',views.updatestudent_fun,name='updatestudent'),
    path('deletestudent/<int:studid>',views.deletestudent_fun,name='deletestudent'),
    path('logout',views.logout_fun,name='logout')
]