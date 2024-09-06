from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages
import csv

@login_required(login_url='/')
def home(request):
    student_count = Student.objects.all().count()
    staff_count = Staff.objects.all().count()
    course_count = Course.objects.all().count()
    subject_count = Subject.objects.all().count()
    male_student = Student.objects.filter(gender='Male').count()
    female_student = Student.objects.filter(gender='Female').count()
    print(male_student)
    print(female_student)
    
    return render(request, 'Hod/home.html', {"student_count": student_count, "staff_count": staff_count, "course_count": course_count, "subject_count": subject_count, "male_student": male_student, "female_student": female_student})

@login_required(login_url='/')
def student_add(request):
    course = Course.objects.all()
    session = Session_year.objects.all()
    
    if request.method=="POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        course_id = request.POST.get('course_id')
        session_id = request.POST.get('session_id')
       
        
        
        if not all([username, email, password, first_name, last_name]):
            messages.error(request, "All fields are required.")
        elif CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email is already taken.")
        elif CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken.")
        else:    
            user = CustomUser(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email=email,
                profile_pic = profile_pic,
                user_type = 2
                
            )
            user.set_password(password)
            user.save()
            
            courses = Course.objects.get(id=course_id)
            sessions = Session_year.objects.get(id=session_id)
            print(courses, sessions)
            student = Student(
                admin = user,
                address = address,
                gender = gender,
                course_id = courses,
                session_id = sessions
            )
            student.save()
            messages.success(request, "Student add successfully")
            return redirect('student_add')
        
    return render(request, 'Hod/add_student.html', {'course': course, 'session': session})

@login_required(login_url='/')
def student_views(request):
    student = Student.objects.all()
    return render(request, 'Hod/view_student.html', {'student': student})

@login_required(login_url='/')
def student_save(request):
    response = HttpResponse(content_type='text/csv')
    print(response)
    response['Content-Disposition'] = 'attachment; filename=students.csv'
    
    writer = csv.writer(response)
    
    students = Student.objects.all()

    writer.writerow(['Name', 'Email', 'Course', 'Gender', 'Address', 'Session Start', 'Session End', 'Created Time', 'Updated Time'])

    for student in students:
        writer.writerow([student.admin.first_name +" "+ student.admin.last_name, student.admin.email, student.course_id.name, student.gender, student.address, student.session_id.start_session, student.session_id.end_session, student.created_at, student.updated_at])
        
    return response

@login_required(login_url='/')
def student_edit(request, id):
    stdnt = Student.objects.filter(id=id)
    course = Course.objects.all()
    session = Session_year.objects.all()
    return render(request, 'Hod/edit_student.html', {"student": stdnt, "course": course, 'session': session})

@login_required(login_url='/')
def student_update(request):
    if request.method=="POST":
        admin_id = request.POST.get('admin_id')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        course_id = request.POST.get('course_id')
        session_id = request.POST.get('session_id')
        
        print(admin_id)
        
        
        user = CustomUser.objects.get(id=admin_id)
        
        user.first_name =first_name
        user.last_name = last_name
        user.email = email
        
        if password != None and password != '':
            user.set_password(password)
                
        
            
        if profile_pic!= None and profile_pic != '':
            user.profile_pic = profile_pic
        user.save()
        student = Student.objects.get(admin=admin_id)
        student.gender = gender
        student.address = address
        
        course = Course.objects.get(id=course_id)
        
        
        session_year = Session_year.objects.get(id=session_id)
        student.course_id = course
        student.session_id = session_year
        student.save()
        messages.success(request, "Updated Successfully")
        return redirect('view_student')
    return render(request, 'Hod/edit_student.html')

@login_required(login_url='/')
def student_delete(request, id):
    student = CustomUser.objects.get(id=id)
    student.delete()
    messages.success(request, "Successfully Delete Record")
    return redirect('view_student')

@login_required(login_url='/')
def course_add(request):
    if request.method == "POST":
        course_name = request.POST.get('course_name')
        if course_name:
            course = Course(name=course_name)
            course.save()
            messages.success(request, "Course saved!")
            return redirect('course_add')
    return render(request, 'Hod/add_course.html')

@login_required(login_url='/')
def course_view(request):
    courses = Course.objects.all()
    return render(request, 'Hod/view_course.html', {'course': courses})

@login_required(login_url='/')
def course_edit(request, id):
    course = Course.objects.get(id=id)
    return render(request, 'Hod/edit_course.html', {"course": course})
   
@login_required(login_url='/') 
def course_update(request):
    if request.method == "POST":
        course_name = request.POST.get('course_name')
        course_id = request.POST.get('course_id')

        try:
            course = Course.objects.get(id=course_id)
            course.name = course_name
            course.save()
            messages.success(request, "Course updated successfully!")
        except Course.DoesNotExist:
            messages.error(request, "Course not found!")

        return redirect('course_view')
    
@login_required(login_url='/')
def course_del(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    messages.success(request, "Successfully Delete Course")
    return redirect('course_view')

@login_required(login_url='/')
def staff_add(request):
    if request.method=="POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        
       
        if not all([username, email, password, first_name, last_name]):
            messages.error(request, "All fields are required.")
        elif CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email is already taken.")
        elif CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken.")
        else:    
            user = CustomUser(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email=email,
                profile_pic = profile_pic,
                user_type = 3
                
            )
            user.set_password(password)
            user.save()
            
            student = Staff(
                admin = user,
                address = address,
                gender = gender,
            )
            student.save()
            messages.success(request, "Student add successfully")
            return redirect('staff_view')
        
    return render(request, 'Hod/add_staff.html')

@login_required(login_url='/')
def staff_view(request):
    staff = Staff.objects.all()
    return render(request, 'Hod/view_staff.html', {'staff': staff})

@login_required(login_url='/')
def staff_save(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=staff.csv'
    
    writer = csv.writer(response)
    staffs = Staff.objects.all()

    writer.writerow(['Name', 'Email', 'Address', 'Gender', 'Created Time', 'Updated Time'])

    for staff in staffs:
        writer.writerow([staff.admin.first_name +" "+ staff.admin.last_name, staff.admin.email, staff.address, staff.gender, staff.created_at, staff.updated_at])
        
    return response
@login_required(login_url='/')
def staff_edit(request, id):
    staff = Staff.objects.get(id=id)
    return render(request, 'Hod/edit_staff.html', {"staff": staff})

@login_required(login_url='/')
def staff_update(request):
    if request.method=="POST":
        admin_id = request.POST.get('admin_id')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        
        
        user = CustomUser.objects.get(id=admin_id)
        
        user.first_name =first_name
        user.last_name = last_name
        user.email = email
        
        if password != None and password != '':
            user.set_password(password)
                
        
            
        if profile_pic!= None and profile_pic != '':
            user.profile_pic = profile_pic
        user.save()
        staff = Staff.objects.get(admin=admin_id)
        staff.gender = gender
        staff.address = address
        
        staff.save()
        messages.success(request, "Staff Updated Successfully")
        return redirect('staff_view')
    return render(request, 'Hod/edit_staff.html')

@login_required(login_url='/')  
def staff_del(request, id):
    staff = Staff.objects.get(id=id)
    staff.delete()
    messages.success(request, "Staff Deleted Successfully")
    return redirect('staff_view')

@login_required(login_url='/')
def subject_add(request):
    course = Course.objects.all()
    staff = Staff.objects.all()
    
    if request.method == 'POST':
        sub_name = request.POST.get('sub_name')
        course_id = request.POST.get('course_id')
        staff_id = request.POST.get('staff')
        
        courses = Course.objects.get(id=course_id)
        staffs = Staff.objects.get(id=staff_id)
        subject = Subject(
            name = sub_name,
            course = courses,
            staff =staffs
        )
        subject.save()
        messages.success(request, "Subject added successfully!")
        return redirect('subject_add')
    return render(request, 'Hod/add_subject.html', {'course': course, 'staff': staff})

@login_required(login_url='/')
def subject_view(request):
    subject = Subject.objects.all()
    
    return render(request, 'Hod/view_subject.html', {'subject': subject})

@login_required(login_url='/')
def subject_edit(request, id):
    subject = Subject.objects.get(id=id)
    course = Course.objects.all()
    staff = Staff.objects.all()
    return render(request, 'Hod/edit_subject.html', {'subject': subject, 'course': course, 'staff': staff})

@login_required(login_url='/')
def subject_update(request):
    if request.method=="POST":
        sub_name = request.POST.get('sub_name')
        sub_id = request.POST.get('sub_id')
        course_id = request.POST.get('course_id')
        staff = request.POST.get('staff')
        
        course = Course.objects.get(id=course_id)
        staff = Staff.objects.get(id=staff)
        
        subject = Subject(
            id = sub_id,
            name = sub_name,
            course = course,
            staff = staff
        )
        subject.save()
        messages.success(request, 'Successfully Updated Subject')
        return redirect('subject_view')
    
@login_required(login_url='/')
def subject_del(request, id):
    subject = Subject.objects.get(id=id)
    subject.delete()
    messages.success(request, 'Subject Delete Successfully')
    return redirect('subject_view')

@login_required(login_url='/')
def session_add(request):
    if request.method=="POST":
        start_session = request.POST.get('start_session')
        end_session = request.POST.get('end_session')
        
        session_year = Session_year(
            start_session = start_session,
            end_session = end_session
        )
        session_year.save()
        messages.success(request, "Session Year Added Successfully")
    return render(request, 'Hod/add_session.html')

@login_required(login_url='/')
def session_view(request):
    session = Session_year.objects.all()
    return render(request, 'Hod/view_session.html', {'session': session})

@login_required(login_url='/')
def session_edit(request, id):
    session = Session_year.objects.get(id=id)
    return render(request, 'Hod/edit_session.html', {'session': session})

@login_required(login_url='/')
def session_update(request):
    if request.method=="POST":
        start_session = request.POST.get('start_session')
        end_session = request.POST.get('end_session')
        
        
        session = Session_year(
            start_session = start_session,
            end_session = end_session
        )
        session.save()
        messages.success(request, "Successfully Updated Date")
        return redirect('session_view')
        
@login_required(login_url='/')
def session_del(request, id):
    session = Session_year.objects.get(id=id)
    session.delete()
    messages.success(request, "Successfully Updated Date")
    return redirect('session_view')

@login_required(login_url='/')
def staff_send_notification(request):
    staff = Staff.objects.all()
    see_notification = StaffNotification.objects.all().order_by('-id')[0:5]
    return render(request, 'Hod/staff_notification.html', {'staff': staff, 'see_notification':see_notification})

@login_required(login_url='/')
def save_staff_notifications(request):
    
    if request.method == "POST":
        message = request.POST.get('message')
        staff_id = request.POST.get('staff_id')
        
        staff = Staff.objects.get(admin=staff_id)
        notification = StaffNotification(
            staff_id = staff,
            message = message
        )
        notification.save()
        messages.success(request, "Notification Sent Successfully")
        return redirect('staff_send_notification')
   
@login_required(login_url='/')
def staff_leave_view(request):
    staff_leave = Staff_leaves.objects.all()
    return render(request, 'Hod/staff_leave.html',{'staff_leave': staff_leave})

@login_required(login_url='/')
def staff_approve_leave(request, id):
    stff_leave = Staff_leaves.objects.get(id=id)
    stff_leave.status = 1
    stff_leave.save()
    return redirect('staff_leave_view')

@login_required(login_url='/')
def staff_disapprove_leave(request, id):
    stff_leave = Staff_leaves.objects.get(id=id)
    stff_leave.status = 2
    stff_leave.save()
    return redirect('staff_leave_view')

@login_required(login_url='/')
def staff_send_reply(request):
    staff = Staff_Feedback.objects.all()
    feedback_history = staff = staff.order_by('-id')[0:5]
    return render(request, 'Hod/staff_send_reply.html', {'staff': staff, 'feedback_history': feedback_history})

@login_required(login_url='/')
def send_staff_reply(request):
    if request.method == 'POST':
        feedback_id = request.POST.get('feedback_id')
        feedback = request.POST.get('feedback_reply')
        
        staff = Staff_Feedback.objects.get(id=feedback_id)
        staff.feedback_reply = feedback
        staff.status = 1
        staff.save()
        
        return redirect('staff_send_reply')
    
@login_required(login_url='/')
def student_send_notification(request):
    student = Student.objects.all()
    notification = StudentNotification.objects.all()
    context = {
        'student': student,
        'notification': notification
    }
    return render(request, 'Hod/student_notification.html', context)

@login_required(login_url='/')
def save_student_notifications(request):
    message = request.POST.get('message')
    student_id = request.POST.get('student_id')
        
    student = Student.objects.get(admin=student_id)
    notification = StudentNotification(
        student_id = student,
        message = message
    )
    notification.save()
    messages.success(request, "Notification Sent Successfully")
    return redirect('student_send_notification')

@login_required(login_url='/')
def hod_view_attendance(request):
    subject = Subject.objects.all()
    session_year = Session_year.objects.all()
           
    action = request.GET.get('action')
    attendance_date = None
    get_subject = None
    attendance_report = None
    get_session_year = None
    if action is not None:
        if request.method=="POST":
            subject_id = request.POST.get('subject_id')
            session_year_id = request.POST.get('session_year_id')
            attendance_date = request.POST.get('attendance_date')
            
            get_subject = Subject.objects.get(id=subject_id)
            get_session_year = Session_year.objects.get(id=session_year_id)
            
            attendance = Attendance.objects.filter(subject_id=subject_id, attendance_date=attendance_date)
            
            for i in attendance:
                attendance_id = i.id
                attendance_report = Attendance_Report.objects.filter(attendance_id=attendance_id)
            
    return render(request, 'Hod/view_attendance.html', {'get_subject': get_subject, 'subject': subject, 'get_session_year': get_session_year, 'action': action, 'attendance_date': attendance_date, 'attendance_report': attendance_report, 'session_year': session_year})

@login_required(login_url='/')
def student_send_reply(request):
    student = Student_Feedback.objects.all()
    feedback_history = student.order_by('-id')[0:5]
    return render(request, 'Hod/student_send_reply.html', {'student': student, 'feedback_history': feedback_history})

@login_required(login_url='/')
def send_student_reply(request):
    if request.method == 'POST':
        feedback_id = request.POST.get('feedback_id')
        feedback = request.POST.get('feedback_reply')
        
        student = Student_Feedback.objects.get(id=feedback_id)
        student.feedback_reply = feedback
        student.status = 1
        student.save()
        
        return redirect('student_send_reply')

@login_required(login_url='/')
def student_leave_view(request):
    student_leave = Student_leaves.objects.all()
    return render(request, 'Hod/student_leave.html',{'student_leave': student_leave})

@login_required(login_url='/')
def student_approve_leave(request, id):
    student_leave = Student_leaves.objects.get(id=id)
    student_leave.status = 1
    student_leave.save()
    return redirect('student_leave_view')

@login_required(login_url='/')
def student_disapprove_leave(request, id):
    student_leave = Student_leaves.objects.get(id=id)
    student_leave.status = 2
    student_leave.save()
    return redirect('student_leave_view')

@login_required(login_url='/')
def transport_notice(request):
    notice = Transport_Notice.objects.all().order_by('-id')
    return render(request, 'Hod/notice.html', {'notice': notice})

@login_required(login_url='/')
def bus_schedule(request):
    bus = Transport.objects.all()
    return render(request, 'Hod/view_bus_schedule.html', {'bus': bus})