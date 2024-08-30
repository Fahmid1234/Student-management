from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils import timezone

@login_required(login_url='/')
def home(request):
    return render(request, 'Student/home.html')

@login_required(login_url='/')
def notification(request):
    student_notification = Student.objects.filter(admin=request.user.id)
    for i in student_notification:
        student_id = i.id
        
        notifications = StudentNotification.objects.filter(student_id=student_id)
    return render(request, 'Student/notification.html', {'notifications': notifications})

@login_required(login_url='/')
def show_notification(request, id):
    student = StudentNotification.objects.get(id=id)
    student.status = 1
    student.save()
    return redirect('student_notification')

@login_required(login_url='/')
def student_view_attendance(request):
    student = Student.objects.get(admin=request.user.id)
    subject = Subject.objects.filter(course=student.course_id)
    action = request.GET.get('action')
    get_subject = None
    attendance_report = None
    if action is not None:
        if request.method=='POST':
            subject_id = request.POST.get('subject_id')
            get_subject = Subject.objects.get(id=subject_id)
            
            attendance = Attendance.objects.filter(subject_id=get_subject)
            attendance_report = Attendance_Report.objects.filter(student_id=student,attendance_id__subject_id=subject_id)
    return render(request, 'Student/view_attendance.html', {'subject': subject, 'action': action, 'get_subject': get_subject, 'attendance_report': attendance_report})

@login_required(login_url='/')
def student_view_result(request):
    student = Student.objects.get(admin=request.user.id)
    result = StudentResult.objects.filter(student_id=student)
    return render(request, 'Student/view_result.html', {'result': result})

@login_required(login_url='/')
def student_feedback(request):
    student_id = Student.objects.get(admin=request.user.id)
    
    feedback = Student_Feedback.objects.filter(student_id=student_id)
    
    return render(request, 'Student/feedback.html', {'feedback': feedback})

@login_required(login_url='/')
def student_feedback_save(request):
    if request.method=='POST':
        feedback = request.POST.get('feedback')
        
        student_id = Student.objects.get(admin=request.user.id)
        
        feedback = Student_Feedback(
            feedback = feedback,
            student_id = student_id,
            feedback_reply = ""
        )
        feedback.save()
        return redirect('student_feedback')

@login_required(login_url='/')
def student_apply_leaves(request):
    student = Student.objects.filter(admin=request.user.id)
    for i in student:
        student_id = i.id
        student_leave_history = Student_leaves.objects.filter(student_id=student_id)
    
    return render(request, 'Student/student_leave.html', {'student_leave_history': student_leave_history})

@login_required(login_url='/')
def student_apply_leave_save(request):
    if request.method=="POST":
        leave_date = request.POST.get('leave_date')
        message = request.POST.get('message')
        
        student = Student.objects.get(admin=request.user.id)
        
        student_leave = Student_leaves(
            student_id = student,
            date = leave_date,
            message = message
        )
        student_leave.save()
        messages.success(request, "Applied For Leave")
        return redirect('student_apply_leaves')
    
@login_required(login_url='/')
def transport_notice(request):
    notice = Transport_Notice.objects.all().order_by('-id')
    return render(request, 'Student/notice.html', {'notice': notice})

@login_required(login_url='/')
def bus_schedule(request):
    bus = Transport.objects.all()
    return render(request, 'Student/view_bus_schedule.html', {'bus': bus})

@login_required(login_url='/')
def assignment(request):
    student = Student.objects.get(admin=request.user.id)
    subjects = student.course_id.subject_set.all()
    assignments = Assignment.objects.filter(subject__in=subjects, session_year=student.session_id)
    submitted_assignments = AssignmentSubmit.objects.filter(student=student)

    submitted_assignment_ids = [submission.assignment.id for submission in submitted_assignments]
    today = timezone.now().date()
    now = timezone.now().time()

    return render(request, 'Student/show_assignment.html', {
        'assignments': assignments,
        'submitted_assignment_ids': submitted_assignment_ids,
        'today': today,
        'now': now,
    })

@login_required(login_url='/')
def assignment_submit(request):
    student = Student.objects.get(admin=request.user.id)
    assignments = Assignment.objects.filter(subject__course=student.course_id, session_year=student.session_id)
    submitted_assignments = AssignmentSubmit.objects.filter(student=student)

    submitted_assignment_ids = [submission.assignment.id for submission in submitted_assignments]

    if request.method == 'POST':
        assignment_id = request.POST.get('assignment')
        submission_file = request.FILES.get('submission_file')
    
        assignment = Assignment.objects.get(id=assignment_id)
        submission_date = timezone.now().date()
        submission_time = timezone.now().time()

        if assignment_id in submitted_assignment_ids or assignment.submission_last_date < submission_date or (assignment.submission_last_date == submission_date and assignment.submission_last_time < submission_time):
            messages.error(request, "You cannot submit this assignment.")
        else:
            assignment_submit = AssignmentSubmit(
                assignment=assignment,
                student=student,
                submission_file=submission_file,
                submission_date=submission_date,
                submission_time=submission_time,
                status=1
            )
            assignment_submit.save()
            messages.success(request, "Assignment submitted successfully")
            return redirect('show_assignment')
    
    context = {
        'assignments': assignments,
        'submitted_assignment_ids': submitted_assignment_ids,
        'today': timezone.now().date(),
    }
    
    return render(request, 'Student/show_assignment.html', context)