from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Profile

from django.contrib.auth.models import User

# Create your views here.


def profile(request):
    if request.method == "POST":
        DOB = request.POST['DOB']
        Height = request.POST['Height']
        Weight = request.POST['Weight']
        Smoke = request.POST['Smoke']
        Alcohol = request.POST['Alcohol']
        Allergy = request.POST['Allergy']
        Current_Medication = request.POST['Current_Medication']
        Blood_Group = request.POST['Blood_Group']
        user_id = request.user.id
        # print(user_id)
        u = Profile.objects.filter(user_id=request.user.id).update(
            DOB=DOB, Height=Height, Weight=Weight, Smoke=Smoke, Alcohol=Alcohol, Allergy=Allergy, Current_Medication=Current_Medication, Blood_Group=Blood_Group)
        # return HttpResponse(u.query)

        # profile = Profile(DOB=DOB, Height=Height, Weight=Weight, Smoke=Smoke, Alcohol=Alcohol, Allergy=Allergy,
        #    Current_Medication=Current_Medication, Blood_Group=Blood_Group)
        # profile.save()
        return redirect('covid')

    else:

        return render(request, 'Userprofile/profile.html')


def managepro(request):
    if request.method == "POST":
        DOB = request.POST['DOB']
        Height = request.POST['Height']
        Weight = request.POST['Weight']
        Smoke = request.POST['Smoke']
        Alcohol = request.POST['Alcohol']
        Allergy = request.POST['Allergy']
        Current_Medication = request.POST['Current_Medication']
        Blood_Group = request.POST['Blood_Group']

    return HttpResponse("hoo")


def covid(request):
    return render(request, 'Userprofile/covid.html')


def home(request):
    return HttpResponse(" Welcome to Generali Concierge Services")
