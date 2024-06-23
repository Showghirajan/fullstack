# app1/views.py

from django.shortcuts import render,redirect
from .models import Appointment
from django.contrib import messages
from django.core.mail import send_mail

#import requests
#key='bx9Qm8FdnFsPDkU3dIIrUa5d2dfG1hRHampsHy37'
def drug(request):
   # data=None
   # name=request.GET.get('search')
    ##url=f'https://api.fda.gov/drug/label.json?search={name}&api_key={key}'
    #response=requests.get(url)
    #data=response.json()
    #results = data['results']
    #print(results)
    #context={
     #   'results':results   }
    #return render(request,'drug.html',context)
    return render(request,'drug.html')
def index(request):
    return render(request,'map.html')
def book(request):
    if request.method == 'POST':
        input_name = request.POST.get('name')
        input_email = request.POST.get('email')
        input_address = request.POST.get('address')
        input_dt = request.POST.get('dt')

        appoint = Appointment(
            p_name=input_name,
            p_email=input_email,
            p_address=input_address,
            p_date_time=input_dt
        )
        appoint.save()
        send_mail(
            subject='New Appointment Booked',
            message=f'Hi Doctor,\n\nA new appointment has been booked.\n\nName: {input_name}\nEmail: {input_email}\nAddress: {input_address}\nDate & Time: {input_dt}',
            from_email='sofiyaraj27@gmail.com', 
            recipient_list=['showghirajan9789@gmail.com','lochanr2965@gmail.com'], 
            fail_silently=False,
        )

        messages.success(request, f"Thank you {input_name}, your Appointment is booked successfully!")
        return redirect('book')
    return render(request,'book.html')
def doctor(request):
    booked=Appointment.objects.all().order_by('-p_date_time')
    return render(request,'doctor.html',{'booked_list':booked})