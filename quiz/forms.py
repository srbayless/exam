from django import forms
from django.forms.widgets import TextInput
from django.forms.widgets import DateInput, TextInput

class patient(forms.Form):
   
    todaysDate = forms.DateField(widget=forms.TextInput(attrs={'placeholder': 'Date', 'style': 'height: 30px; width: 140px'}))
    lastName = forms.CharField(label=False,widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'style': 'height: 70px; width: 280px', 'class': 'form-control'}))
    firstName = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name', 'style': 'height: 70px; width: 280px', 'class': 'form-control'}))
    address=forms.CharField(label = "Address", widget=forms.TextInput(attrs={'placeholder': 'Address','style': 'height: 30px; width: 270px; overflow: hidden', 'class': 'form-controls'}))
    cistzip = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder': 'Zipcode','style': 'height: 30px; width: 270px', 'class': 'form-controls'}))
    phoneNumber=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Phone Number','style': 'height: 30px; width: 160px', 'class': 'form-controls'}))
    birthdate = forms.DateField(widget=forms.TextInput(attrs={'placeholder': 'Birthdate', 'style': 'height: 30px; width: 140px'}))
    GENCHOICES = [('N', 'None Selected'),('M','Male'),('F','Female'),('O', 'Other')]
    patient_gender = forms.ChoiceField(label='Gender', choices=GENCHOICES)
    patient_dob = forms.DateField(label = False, widget=DateInput(attrs={'placeholder': 'mm/dd/yyyy', 'style': 'height: 30px; width: 140px; border: none'}))
    age = forms.CharField(label='Age', widget=TextInput(attrs={'placeholder': 'Age','style': 'height: 40px; width: 60px', 'class': 'form-controls'}))
    patientId = forms.CharField(label="Patient ID", widget=forms.TextInput(attrs={'placeholder:' 'patient Id' 'style': 'height: 30px; width: 165px'}))
    TESTCHOICES = [('N','None Selected'),('B','MORPHO'),('P','FLOW'),('L','CYTO'),('PE','FISH'),('T','additional FISH'),('BI','MOLECULAR'),('BO','CONSULT')]
    test = forms.CharField(label='Test', widget=forms.Select(choices=TESTCHOICES))