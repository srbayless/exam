from django.shortcuts import render
from quiz.forms import patient


def RegistrationFormView(request):
    return render(request, 'registration.html',{'patient': patient()})
