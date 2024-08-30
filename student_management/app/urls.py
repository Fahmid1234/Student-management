from django.urls import path
from . import views, Hod_views, student_views, staff_views, transport_views
urlpatterns = [
    path('', views.login_veiw, name='login'),
    path('dologin/', views.dologin, name='dologin'),
    path('dologout/', views.dologout, name='dologout'),
    
    path("profile/view", views.profile_view, name="profile_view"),
    path("profile/", views.profile, name="profile"),
    path("profile_update/", views.profile_update, name="profile_update"),
    path("resgistration/", views.registration, name='registration'),
    path("check_registration/", views.check_registration, name='check_registration'),
    
    #hod urls
    path('Hod/home/', Hod_views.home, name='hod_home'),
    
    path('Hod/student/add', Hod_views.student_add, name='student_add'),
    path('Hod/student/view', Hod_views.student_views, name='view_student'),
    path('Hod/student/edit/<int:id>', Hod_views.student_edit, name='edit_student'),
    path('Hod/student/update', Hod_views.student_update, name='update_student'),
    path('Hod/student/delete/<int:id>', Hod_views.student_delete, name='delete_student'),
    
    path('Hod/course/add', Hod_views.course_add, name='course_add'),
    path('Hod/course/view', Hod_views.course_view, name='course_view'),
    path('Hod/course/edit/<str:id>', Hod_views.course_edit, name='course_edit'),
    path('Hod/course/update', Hod_views.course_update, name='update_course'),
    path('Hod/course/delete/<str:id>', Hod_views.course_del, name='course_del'),
    
    path('Hod/staff/add', Hod_views.staff_add, name='staff_add'),
    path('Hod/staff/view', Hod_views.staff_view, name='staff_view'),
    path('Hod/staff/edit/<str:id>', Hod_views.staff_edit, name='staff_edit'),
    path('Hod/staff/update', Hod_views.staff_update, name='staff_update'),
    path('Hod/staff/delete/<str:id>', Hod_views.staff_del, name='staff_del'),
    
    path('Hod/subject/add', Hod_views.subject_add, name='subject_add'),
    path('Hod/subject/view', Hod_views.subject_view, name='subject_view'),
    path('Hod/subject/edit/<str:id>', Hod_views.subject_edit, name='subject_edit'),
    path('Hod/subject/update', Hod_views.subject_update, name='subject_update'),
    path('Hod/subject/delete/<str:id>', Hod_views.subject_del, name='subject_del'),
    
    path('Hod/session/add', Hod_views.session_add, name='session_add'),
    path('Hod/session/view', Hod_views.session_view, name='session_view'),
    path('Hod/session/edit/<str:id>', Hod_views.session_edit, name='session_edit'),
    path('Hod/session/update', Hod_views.session_update, name='session_update'),
    path('Hod/session/delete/<str:id>', Hod_views.session_del, name='session_del'),
    
    path('Hod/staff/send_notifications', Hod_views.staff_send_notification, name='staff_send_notification'),
    path('Hod/Staff/save_notifications', Hod_views.save_staff_notifications, name='save_staff_notifications'),
    
    path('Hod/Staff/leave_view', Hod_views.staff_leave_view, name='staff_leave_view'),
    path('Hod/Staff/approve_leave/<int:id>', Hod_views.staff_approve_leave, name='staff_approve_leave'),
    path('Hod/Staff/disapprove_leave/<int:id>', Hod_views.staff_disapprove_leave, name='staff_disapprove_leave'),
    
    path('Hod/Staff/send_reply', Hod_views.staff_send_reply, name='staff_send_reply'),
    path('Hod/Staff/reply_send', Hod_views.send_staff_reply, name='send_staff_reply'),
    path('Hod/Student/send_notifications', Hod_views.student_send_notification, name='student_send_notification'),
    path('Hod/Student/save_notifications', Hod_views.save_student_notifications, name='save_student_notifications'),
    path('Hod/view_attendance', Hod_views.hod_view_attendance, name='hod_view_attendance'),
    path('Hod/Student/send_reply', Hod_views.student_send_reply, name='student_send_reply'),
    path('Hod/Student/reply_send', Hod_views.send_student_reply, name='send_student_reply'),
    
    path('Hod/Student/leave_view', Hod_views.student_leave_view, name='student_leave_view'),
    path('Hod/Student/approve_leave/<int:id>', Hod_views.student_approve_leave, name='student_approve_leave'),
    path('Hod/Student/disapprove_leave/<int:id>', Hod_views.student_disapprove_leave, name='student_disapprove_leave'),
    
    path('Hod/tranport_notice', Hod_views.transport_notice, name="hod_transport_notice"),
    path('Hod/bus/schedule', Hod_views.bus_schedule, name='hod_bus_schedule'),
    

    #staff urls
    path('Staff/home', staff_views.home, name="staff_home"),
    path('Staff/notification', staff_views.notification, name='notification'),
    path('Staff/show_notifications/<int:id>', staff_views.show_notifications, name='show_notifications'),
    path('Staff/leave', staff_views.staff_apply_leaves, name='staff_apply_leaves'),
    path('Staff/apply_leavel_save', staff_views.staff_apply_leavel_save, name='staff_apply_leavel_save'),
    path('Staff/leave_view', Hod_views.staff_leave_view, name='staff_apply_leave_save'),
    path('Staff/feedback', staff_views.staff_feedback, name='staff_feedback'),
    path('Staff/feedback/save', staff_views.staff_feedback_save, name='staff_feedback_save'),
    path('Staff/take_attendance', staff_views.staff_take_attendance, name='staff_take_attendance'),
    path('Staff/save_attendance', staff_views.staff_save_attendance, name='staff_save_attendance'),
    path('Staff/view_attendance', staff_views.staff_view_attendance, name='staff_view_attendance'),
    path("Staff/add_result", staff_views.add_result, name="add_result"),
    path("Staff/save_result", staff_views.save_result, name="save_result"),
    
    path('Staff/tranport_notice', staff_views.transport_notice, name="staff_transport_notice"),
    path('Staff/bus/schedule', staff_views.bus_schedule, name='staff_bus_schedule'),
    
    path('Staff/add/assignment', staff_views.assignment_add, name='add_assignment'),
    path("Staff/Assignment", staff_views.assignment, name="assignment"),
    path("Staff/view_assignment", staff_views.view_assignment, name="view_assignment"),
    
    #student urls
    path('Studdent/home', student_views.home, name="student_home"),
    path('Student/notification', student_views.notification, name='student_notification'),
    path('Student/show_notification/<int:id>', student_views.show_notification, name='show_student_notification'),
    path('Student/view_attendance', student_views.student_view_attendance, name='student_view_attendance'),
    path('Student/view_result', student_views.student_view_result, name='student_view_result'),
    path('Student/feedback', student_views.student_feedback, name='student_feedback'),
    path('Student/feedback/save', student_views.student_feedback_save, name='student_feedback_save'),
    path('Student/leave', student_views.student_apply_leaves, name='student_apply_leaves'),
    path('Student/apply_leave_save', student_views.student_apply_leave_save, name='student_apply_leave_save'),
    
    path('Student/tranport_notice', student_views.transport_notice, name="student_transport_notice"),
    path('Student/bus/schedule', student_views.bus_schedule, name='student_bus_schedule'),
    
    path("Student/assignment", student_views.assignment, name="show_assignment"),
    path("Student/assignment_submit", student_views.assignment_submit, name="assignment_submit"),
    
    #transport
    path('Transport/home', transport_views.home, name="transport_home"),
    path('Transport/notification', transport_views.notification, name="transport_notification"),
    path('Transport/save_notification', transport_views.save_notification, name="transport_notification_save"),
    path('Transport/notice/delete/<int:id>', transport_views.tranport_notification_delete, name='delete_transport_notice'),
    path('Transport/driver_add', transport_views.add_driver, name="add_driver"),
    path('Transport/save_driver', transport_views.save_driver, name="transport_driver_save"),
    path('Transport/driver_view', transport_views.driver_view, name="driver_view"),
    path('Transport/driver/delete/<int:id>', transport_views.tranport_driver_delete, name='delete_transport_driver'),
    path('Transport/bus_add', transport_views.add_bus, name="add_bus"),
    path('Transport/save_bus', transport_views.save_bus, name="transport_bus_save"),
    path('Transport/bus_view', transport_views.bus_view, name="bus_view"),
    path('Transport/bus/delete/<int:id>', transport_views.tranport_bus_delete, name='delete_transport_bus'),
]
