from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views, Hod_views, Staff_views, Student_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE, name='base'),

    # Login Path
    path('', views.LOGIN, name='login'),
    path('dologin', views.dologin, name='dologin'),
    path('dologout', views.dologout, name='logout'),

    # Profile Update
    path('profile', views.PROFILE, name='profile'),
    path('Profile/update',views.PROFILE_UPDATE, name='profile_update'),

    # This is HoD panel url

    path('Hod/Home', Hod_views.HOME, name='hod_home'),

    #This is for student curd operation
    path('Hod/Student/Add', Hod_views.ADD_STUDENT, name='add_student'),
    path('Hod/Student/View', Hod_views.VIEW_STUDENT, name='view_student'),
    path('Hod/Student/Edit/<str:id>', Hod_views.EDIT_STUDENT, name='edit_student'),
    path('Hod/Student/Update', Hod_views.UPDATE_STUDENT, name='update_student'),
    path('Hod/Student/Delete/<str:id>', Hod_views.DELETE_STUDENT, name='delete_student'),

    #This is for staff crud operation 
    path('Hod/staff/Add', Hod_views.ADD_STAFF, name='add_staff'),
    path('Hod/Staff/View', Hod_views.VIEW_STAFF, name='view_staff'),
    path('Hod/Staff/Edit/<str:id>', Hod_views.EDIT_STAFF, name='edit_staff'),
    path('Hod/Staff/Update', Hod_views.UPDATE_STAFF, name='update_staff'),
    path('Hod/Staff/Delete/<str:admin>', Hod_views.DELETE_STAFF, name='delete_staff'),

    #This is for staff notification 
    path('Hod/Staff/Send_Notofication', Hod_views.STAFF_SEND_NOTIFICATION, name='staff_send_notification'),
    path('Hod/Staff/Save_Notification', Hod_views.SAVE_STAFF_NOTIFICATION, name='save_staff_notification'),

    #This is for course curd operation
    path('Hod/Course/Add', Hod_views.ADD_COURSE, name='add_course'),
    path('Hod/Course/View', Hod_views.VIEW_COURSE, name='view_course'),
    path('Hod/Course/Edit/<str:id>',Hod_views.EDIT_COURSE,name='edit_course'),
    path('Hod/Course/Update',Hod_views.UPDATE_COURSE,name='update_course'),
    path('Hod/Course/Delete/<str:id>',Hod_views.DELETE_COURSE,name='delete_course'),

    #This is for subject curd operation
    path('Hod/Subject/Add', Hod_views.ADD_SUBJECT, name='add_subject'),
    path('Hod/Subject/View', Hod_views.VIEW_SUBJECT, name='view_subject'),
    path('Hod/Subject/Edit<str:id>', Hod_views.EDIT_SUBJECT, name='edit_subject'),
    path('Hod/Subject/Update',Hod_views.UPDATE_SUBJECT,name='update_subject'),
    path('Hod/Subject/Delete/<str:id>',Hod_views.DELETE_SUBJECT,name='delete_subject'),

    #This is for session curd operation
    path('Hod/Session/Add', Hod_views.ADD_SESSION, name='add_session'),
    path('Hod/Session/View', Hod_views.VIEW_SESSION, name='view_session'),
    path('Hod/Session/Edit/<str:id>', Hod_views.EDIT_SESSION, name='edit_session'),
    path('Hod/Session/Update/', Hod_views.UPDATE_SESSION, name='update_session'),
    path('Hod/Session/Delete/<str:id>',Hod_views.DELETE_SESSION,name='delete_session'),
    

    # This is staff pannel url 
    path('Staff/Home', Staff_views.HOME, name='staff_home'),
    path('Staff/Notifications', Staff_views.NOTIFICATIONS, name="notifications"),
    path('Staff/mark_as_read/<str:status>', Staff_views.STAFF_READ, name="staff_read"),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
