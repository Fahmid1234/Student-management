from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User

@login_required(login_url='/')
def home(request):
    return render(request, 'Transport/home.html')

@login_required(login_url='/')
def notification(request):
    notice = Transport_Notice.objects.all().order_by('-id')[0:5]
    return render(request, 'Transport/notification.html', {'notice': notice})

@login_required(login_url='/')
def save_notification(request):
    if request.method=="POST":
        message = request.POST.get('message')
        transprot_notice = Transport_Notice(
            message = message
        )
        transprot_notice.save()
        messages.success(request, "Notice send successfully")
        return redirect("transport_notification")

@login_required(login_url='/')
def tranport_notification_delete(request, id):
    notice = Transport_Notice.objects.filter(id=id)
    notice.delete()
    messages.success(request, "Successfully delete the notice")
    return redirect('transport_notification')

@login_required(login_url='/')
def add_driver(request):
    return render(request, 'Transport/add_driver.html')

@login_required(login_url='/')
def save_driver(request):
    if request.method=="POST":
        name = request.POST.get('name')
        mobile_number = request.POST.get('mobile_number')
        address = request.POST.get('address')
        
        driver = Driver(
            name = name,
            mobile_number = mobile_number,
            address = address
        )
        driver.save()
        
        messages.success(request, "Driver save successfully")
        return redirect('add_driver')

@login_required(login_url='/')
def driver_view(request):
    driver = Driver.objects.all()
    return render(request, 'Transport/view_driver.html', {'driver': driver})

@login_required(login_url='/')
def tranport_driver_delete(request, id):
    driver = Driver.objects.filter(id=id)
    driver.delete()
    messages.success(request, "Successfully delete the driver data")
    return redirect('driver_view')

@login_required(login_url='/')
def add_bus(request):
    driver = Driver.objects.all()
    return render(request, 'Transport/add_bus_schedule.html', {'driver': driver})

@login_required(login_url='/')
def save_bus(request):
    if request.method=="POST":
        bus_number = request.POST.get('bus_number')
        where_from = request.POST.get('where_from')
        where_to = request.POST.get('where_to')
        driver_name = request.POST.get('driver_name')
        time = request.POST.get('time')
        
        transport = Transport(
            bus_number = bus_number,
            where_from = where_from,
            where_to = where_to,
            driver_name = driver_name,
            time = time
        )
        transport.save()
        messages.success(request, "Bus information save successfully")
        return redirect('add_bus')

@login_required(login_url='/')
def bus_view(request):
    bus = Transport.objects.all()
    return render(request, "Transport/view_bus_schedule.html", {'bus': bus})

@login_required(login_url='/')
def tranport_bus_delete(request, id):
    bus = Transport.objects.filter(id=id)
    bus.delete()
    messages.success(request, "Successfully delete bus information")
    return redirect('bus_view')