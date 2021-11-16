from django.shortcuts import render
from 


def RegistrationFormView(request):
    return render(request, 'registration.html',{'patient': patient()})
