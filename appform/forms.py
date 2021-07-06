from django import forms
from django.forms import ModelForm
from .models import Application_Form


class ApplicationForm(ModelForm):
    class Meta:
        model = Application_Form
        fields = "__all__"
        labels = {
            'l_name' : '',
            'm_name' : '',
            'f_name' : '',
            'gender' : '',
            'date_of_birth' : '',
            'school' : '',
            'classification' : '',
            'sport' : '',
            'position' : '',
            'email' : '',
            'phone_number' : '',
            'address_1' : '',
            'address_2' : '',
            'city' : '',
            'state' : '',
            'zipcode' : '',
            'sport_background' : '',
            'sport_play' : '',
            'dominant_hand' : '',
            'programs' : '',
        }
    
        widgets = {
            'l_name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}),
            'm_name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Middle Name Please write N/A if none'}),
            'f_name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),
            'gender' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Gender'}),
            'date_of_birth' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Date of Birth'}),
            'school' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'School'}),
            'classification' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Classification'}),
            'sport' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Sport'}),
            'position' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Position'}),
            'email' : forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),
            'phone_number' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone Number'}),
            'address_1' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address 1'}),
            'address_2' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address 2, Please write N/A if none'}),
            'city' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'City'}),
            'state' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'State'}),
            'zipcode' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Zipcode'}),
            'sport_background' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please Describe Your Sport Background'}),
            'sport_play' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'What Other Sports You have Played in the Past'}),
            'dominant_hand' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'What is Your Dominant Hand'}),
            'programs' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please Choose Program(s)You are Interested (Treatment/Rehab, Psychological Aspect, Performance Training: Speed or/and Strength Training, Nutrition Services)'}),
        }