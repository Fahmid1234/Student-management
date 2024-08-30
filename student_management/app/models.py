from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    USER = (
        (1, "HOD"),
        (2, "Student"),
        (3, "Stuff"),
    )
    user_type = models.CharField(choices=USER, max_length=50, default=1)
    profile_pic = models.ImageField(upload_to='profile_pic')
    
class Course(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class Session_year(models.Model):
    start_session = models.DateField()
    end_session = models.DateField()
    
    
    
class Student(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address = models.TextField()
    gender = models.CharField(max_length=50)
    course_id = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    session_id = models.ForeignKey(Session_year, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.admin.first_name + " " + self.admin.last_name
    
class Staff(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address = models.TextField()
    gender = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.admin.first_name + " " + self.admin.last_name
    
class Subject(models.Model):
    name = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class StaffNotification(models.Model):
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(null=True, default=0)
    
    def __str__(self):
        return self.staff_id.admin.first_name + " " + self.staff_id.admin.last_name
    
class Staff_leaves(models.Model):
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    message = models.TextField()
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.staff_id.admin.first_name + " " + self.staff_id.admin.last_name
    
class Staff_Feedback(models.Model):
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    feedback = models.TextField()
    status = models.IntegerField(default=0)
    feedback_reply = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.staff_id.admin.first_name + " " + self.staff_id.admin.last_name
    
    
class StudentNotification(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(null=True, default=0)
    
    def __str__(self):
        return self.student_id.admin.first_name + " " + self.student_id.admin.last_name
    
class Attendance(models.Model):
    subject_id = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    attendance_date = models.DateField()
    session_year_id = models.ForeignKey(Session_year, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.subject_id.name
    
class Attendance_Report(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    attendance_id = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.student_id.admin.first_name + " " + self.student_id.admin.last_name
    
class StudentResult(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    subject_id = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    assignment_mark = models.IntegerField()
    class_test_mark = models.IntegerField()
    presentation_mark = models.IntegerField()
    mid_exm_mark = models.IntegerField()
    final_exm_mark = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.student_id.admin.first_name + " " + self.student_id.admin.last_name
    
class Student_Feedback(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField(null=True)
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.student_id.admin.first_name + " " + self.student_id.admin.last_name
    
class Student_leaves(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    message = models.TextField()
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.student_id.admin.first_name + " " + self.student_id.admin.last_name

class Driver(models.Model):
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=20)
    address = models.TextField()
    
    def __str__(self):
        return self.name
       
class Transport(models.Model):
    bus_number = models.CharField(max_length=20)
    where_from = models.CharField(max_length=50)
    where_to = models.CharField(max_length=50)
    driver_name = models.CharField(max_length=100)
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.bus_number} - {self.route}"
    
class Transport_Notice(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.message
    
class Assignment(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    session_year = models.ForeignKey(Session_year, on_delete=models.CASCADE, null=True)
    pdf_file = models.FileField(upload_to='pdf')
    submission_last_date = models.DateField(null=True)
    submission_last_time = models.TimeField(null=True)
    
    
class AssignmentSubmit(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    submission_file = models.FileField(upload_to='submissions')
    submission_date = models.DateField(null=True, blank=True)
    submission_time = models.TimeField(null=True, blank=True)
    status = models.IntegerField(default=0)