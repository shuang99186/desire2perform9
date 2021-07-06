from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ApplicationForm

def programs(request):
    return render(request, 'application/programs.html', {})

def application_form(request):
    submitted = False
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/application_form?submitted=True')
    else: 
        form = ApplicationForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'application/application_form.html', {'form':form, 'submitted':submitted})

def home(request):
    return render(request, 'application/home.html', {})
