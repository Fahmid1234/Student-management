from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils import timezone

@login_required(login_url='/')
def home(request):
    return render(request, 'Staff/home.html')

@login_required(login_url='/')
def notification(request):
    staff_notify = Staff.objects.filter(admin=request.user.id)
    for i in staff_notify:
        staff_id = i.id
        
        notifications = StaffNotification.objects.filter(staff_id=staff_id)
    return render(request, 'Staff/notification.html', {'notifications': notifications})

@login_required(login_url='/')
def show_notifications(request, id):
    notifications = StaffNotification.objects.get(id=id)
    notifications.status = 1
    notifications.save()
    return redirect('notification')

@login_required(login_url='/')
def staff_apply_leaves(request):
    staff = Staff.objects.filter(admin=request.user.id)
    
    for i in staff:
        staff_id = i.id
        staff_leave_history = Staff_leaves.objects.filter(staff_id=staff_id)
    return render(request, 'Staff/staff_leave.html', {'staff_leave_history': staff_leave_history})

@login_required(login_url='/')
def staff_apply_leavel_save(request):
    if request.method=="POST":
        leave_date = request.POST.get('leave_date')
        message = request.POST.get('message')
        
        staff = Staff.objects.get(admin=request.user.id)
        
        staff_leave = Staff_leaves(
            staff_id = staff,
            date = leave_date,
            message = message
        )
        staff_leave.save()
        messages.success(request, "Applied For Leave")
        return redirect('staff_apply_leaves')

@login_required(login_url='/')
def staff_feedback(request):
    staff_id = Staff.objects.get(admin=request.user.id)
    
    feedback = Staff_Feedback.objects.filter(staff_id=staff_id)
    
    return render(request, 'Staff/feedback.html', {'feedback': feedback})

@login_required(login_url='/') 
def staff_feedback_save(request):
    if request.method=='POST':
        feedback = request.POST.get('feedback')
        
        staff_id = Staff.objects.get(admin=request.user.id)
        
        feedback = Staff_Feedback(
            feedback = feedback,
            staff_id = staff_id,
            feedback_reply = ""
        )
        feedback.save()
        return redirect('staff_feedback')

@login_required(login_url='/')
def staff_take_attendance(request):
    staff_id = Staff.objects.get(admin=request.user.id)
    
    subject = Subject.objects.filter(staff=staff_id)
    session_year = Session_year.objects.all()
    
    action = request.GET.get('action')
    
    get_subject = None
    get_session_year = None
    students = None
    
    if action is not None:
        if request.method=="POST":
            subject_id = request.POST.get('subject_id')
            session_year_id = request.POST.get('session_year_id')
            
            get_subject = Subject.objects.get(id=subject_id)
            get_session_year = Session_year.objects.get(id=session_year_id)
            
            subject = Subject.objects.filter(id=subject_id)
            
            for i in subject:
                student_id = i.course.id
                students = Student.objects.filter(course_id=student_id)
                
    return render(request, 'Staff/take_attendance.html', {'subject': subject, 'session_year': session_year, 'get_subject': get_subject, 'get_session_year': get_session_year, 'action': action, 'students': students})

@login_required(login_url='/')
def staff_save_attendance(request):
    if request.method=='POST':
        subject_id = request.POST.get('subject_id')
        session_year_id = request.POST.get('session_year_id')
        attendance_date = request.POST.get('attendance_date')
        student_id = request.POST.getlist('student_id')
        
        get_subject = Subject.objects.get(id=subject_id)
        get_session_year = Session_year.objects.get(id=session_year_id)
        
        attendance = Attendance(
            subject_id = get_subject,
            attendance_date = attendance_date,
            session_year_id = get_session_year
        )
        attendance.save()
        
        for i in student_id:
            stud_id = i
            int_stud = int(i)
            students = Student.objects.get(id=int_stud)
            
            attendance_report = Attendance_Report(
                student_id = students,
                attendance_id = attendance
            )
            attendance_report.save()
    return redirect('staff_take_attendance')

@login_required(login_url='/')
def staff_view_attendance(request):
    staff_id = Staff.objects.get(admin=request.user.id)
    
    subject = Subject.objects.filter(staff=staff_id)
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
            
    return render(request, 'Staff/view_attendance.html', {'get_subject': get_subject, 'subject': subject, 'get_session_year': get_session_year, 'action': action, 'attendance_date': attendance_date, 'attendance_report': attendance_report, 'session_year': session_year})

@login_required(login_url='/')
def add_result(request):
    staff = Staff.objects.get(admin=request.user.id)
    
    subject = Subject.objects.filter(staff_id=staff)
    session_year = Session_year.objects.all()
    action = request.GET.get('action')
    get_subject = None
    get_session = None
    students = None
    if action is not None:
        if request.method=="POST":
            subject_id = request.POST.get('subject_id')
            session_year_id = request.POST.get('session_year_id')
            
            get_subject = Subject.objects.get(id=subject_id)
            get_session = Session_year.objects.get(id=session_year_id)
            
            subject = Subject.objects.filter(id=subject_id)
            for i in subject:
                student_id = i.course.id
                
                students = Student.objects.filter(course_id=student_id)
            
    return render(request, 'Staff/add_result.html', {'subject': subject, 'session_year': session_year, 'action': action, 'get_subject': get_subject, 'get_session': get_session, 'students': students})

@login_required(login_url='/')
def save_result(request):
    if request.method=="POST":
        subject_id = request.POST.get('subject_id')
        session_year_id = request.POST.get('session_year_id')
        student_id = request.POST.get('student_id')
        assignment_mark = request.POST.get('assignment_mark')
        presentation_mark = request.POST.get('presentation_mark')
        class_test_mark = request.POST.get('class_test_mark')
        mid_mark = request.POST.get('mid_mark')
        final_mark = request.POST.get('final_mark')
        
        get_student = Student.objects.get(admin=student_id)
        get_subject = Subject.objects.get(id=subject_id)
        
        check_exists = StudentResult.objects.filter(subject_id=get_subject, student_id=get_student).exists()
        
        if check_exists:
            result = StudentResult.objects.get(subject_id=get_subject, student_id=get_student)
            
            result.assignment_mark = assignment_mark
            result.presentation_mark = presentation_mark
            result.class_test_mark = class_test_mark
            result.mid_exm_mark = mid_mark
            result.final_exm_mark = final_mark
            result.save()
            messages.success(request, 'Marks are successfully updated')
            return redirect('add_result')
        else:
            result = StudentResult(
                student_id = get_student,
                subject_id = get_subject,
                assignment_mark = assignment_mark,
                presentation_mark = presentation_mark,
                class_test_mark = class_test_mark,
                mid_exm_mark = mid_mark,
                final_exm_mark = final_mark
            )
            result.save()
            messages.success(request, 'Marks are successfully saved')
            return redirect('add_result')
        
@login_required(login_url='/')
def transport_notice(request):
    notice = Transport_Notice.objects.all().order_by('-id')
    return render(request, 'Staff/notice.html', {'notice': notice})

@login_required(login_url='/')
def bus_schedule(request):
    bus = Transport.objects.all()
    return render(request, 'Staff/view_bus_schedule.html', {'bus': bus})

@login_required(login_url='/')
def assignment_add(request):
    staff_id = Staff.objects.get(admin=request.user.id)
    
    subject = Subject.objects.filter(staff=staff_id)
    session_year = Session_year.objects.all()
    return render(request, 'Staff/add_assignment.html', {'subjects': subject, 'session_year': session_year})

@login_required(login_url='/')
def assignment(request):
    if request.method == 'POST':
        subject_id = request.POST.get('subject')
        session_year_id = request.POST.get('session_year')
        question = request.FILES.get('assignment_question')
        submission_date = request.POST.get('submission_last_date')
        submission_time = request.POST.get('submission_last_time')
        subject = get_object_or_404(Subject, id=subject_id)
        session_year = get_object_or_404(Session_year, id=session_year_id)
        
        assignment = Assignment(
            subject = subject,
            session_year = session_year,
            pdf_file = question,
            submission_last_date = submission_date,
            submission_last_time = submission_time
        )
        
        assignment.save()
        
        messages.success(request, "Assignment Created successfully")
        return redirect('add_assignment')

@login_required(login_url='/')    
def view_assignment(request):
    
    staff_id = Staff.objects.get(admin=request.user.id)
    subjects = Subject.objects.filter(staff=staff_id)

    assignments_status = []
    students_without_submission = []

    for subject in subjects:
        assignments = Assignment.objects.filter(subject=subject)
        for assignment in assignments:
            deadline_date = assignment.submission_last_date
            deadline_time = assignment.submission_last_time
            is_over = (deadline_date < timezone.now().date()) or \
                      (deadline_date == timezone.now().date() and deadline_time < timezone.now().time())
            assignments_status.append({
                'assignment': assignment,
                'is_over': is_over,
                'subject': subject
            })

            students = Student.objects.filter(course_id=subject.course)
            for student in students:
                if not AssignmentSubmit.objects.filter(assignment=assignment, student=student).exists():
                    students_without_submission.append({
                        'student': student,
                        'assignment': assignment,
                        'subject': subject
                    })

    return render(request, 'Staff/show_assignment.html', {
        'assignments_status': assignments_status,
        'students_without_submission': students_without_submission
    })