from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.

@admin.register(CustomUser)
class UserModel(UserAdmin):
    list_display = ['username', 'user_type', 'profile_pic']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Session_year)
class SessionAdmin(admin.ModelAdmin):
    list_display = ['start_session', 'end_session']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['admin', 'address', 'gender']

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['admin', 'address', 'gender']

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'course', 'staff']

@admin.register(StaffNotification)
class StaffNotificationAdmin(admin.ModelAdmin):
    list_display = ['staff_id', 'message']

@admin.register(Staff_leaves)
class Staff_leaveAdmin(admin.ModelAdmin):
    list_display = ['staff_id', 'date', 'message']

@admin.register(Staff_Feedback)
class Staff_FeedbackAdmin(admin.ModelAdmin):
    list_display = ['staff_id', 'feedback', 'feedback_reply']
    
@admin.register(StudentNotification)
class StudentNotificationAdmin(admin.ModelAdmin):
    list_display = ['student_id', 'message']
    
@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['subject_id', 'attendance_date', 'session_year_id']
    
@admin.register(Attendance_Report)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['student_id', 'attendance_id']
    
@admin.register(StudentResult)
class StudentResultAdmin(admin.ModelAdmin):
    list_display = ['student_id', 'subject_id', 'assignment_mark', 'class_test_mark', 'presentation_mark', 'mid_exm_mark', 'final_exm_mark']

@admin.register(Student_Feedback)
class Student_FeedbackAdmin(admin.ModelAdmin):
    list_display = ['student_id', 'feedback', 'feedback_reply']

@admin.register(Student_leaves)
class Student_leaveAdmin(admin.ModelAdmin):
    list_display = ['student_id', 'date', 'message']
    
@admin.register(Transport)
class TransportAdmin(admin.ModelAdmin):
    list_display = ['bus_number', 'where_from', 'where_to', 'driver_name', 'time']
    
@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ['name', 'mobile_number', 'address']
    
@admin.register(Transport_Notice)
class Transport_NoriceAdmin(admin.ModelAdmin):
    list_display = ['message']
    
@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ['subject', 'session_year', 'pdf_file', 'submission_last_date', 'submission_last_time']
    
@admin.register(AssignmentSubmit)
class AssignmentSubmitAdmin(admin.ModelAdmin):
    list_display = ['assignment', 'student', 'submission_file', 'submission_date', 'submission_time']
