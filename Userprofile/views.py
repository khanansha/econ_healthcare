from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Profile
from django.contrib import messages
from django.contrib.auth.models import User
#import json as simplejson
import json
import requests
#from django.utils import simplejson

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
        user_id = request.user.id
        # print(user_id)
        u = Profile.objects.filter(user_id=request.user.id).update(
            DOB=DOB, Height=Height, Weight=Weight, Smoke=Smoke, Alcohol=Alcohol, Allergy=Allergy, Current_Medication=Current_Medication, Blood_Group=Blood_Group)
        messages.success(
            request, 'your profile has successfully  updated')

        return redirect('index')
    else:

        profile = Profile.objects.filter(user_id=request.user.id)

        # print(profile)
        return render(request, 'Userprofile/manageprofile.html', {'profile': profile})


def covid(request):
    return render(request, 'Userprofile/covid.html')


def home(request):
    return HttpResponse(" Welcome to Generali Concierge Services")


def dial(request):
    return render(request, 'Userprofile/dial.html')


def doctor_spcl(request):

    # params = {'gpsLatitude': '19.10384', 'gpsLongitude': '72.86821', 'page': 0, 'size': 10, 'criteria': 'Dental', 'distance': '2km'}
    # endpoint = 'https://qa-gateway.zoylo.com/zoylogateway-0.0.1-SNAPSHOT/api/user-search/popular-search?provider-type=DOCTOR_CLINIC'

    # # header = {'Accept': 'application/json'}
    # req = requests.get(endpoint, params=params, headers=header)
    # #response_dict = json.loads(req.text)
    # return HttpResponse(req)

    url = "https://qa-gateway.zoylo.com/zoylogateway-0.0.1-SNAPSHOT/api/user-search/popular-search?provider-type=DOCTOR_CLINIC"
    payload = {}
    headers = {}
    response = requests.get(url, headers=headers, data=payload)
    return HttpResponse(response)

    # print(response_dict)
# 'https://qa-gateway.zoylo.com/zoylogateway-0.0.1-SNAPSHOT/api/user-search/popular-search?provider-type=DOCTOR_CLINIC'
# 'https://qa-gateway.zoylo.com/zoylogateway-0.0.1-SNAPSHOT/zoylodoctor/zoylodoctor-0.0.1-SNAPSHOT/api/doctor-details/client-doctors'


def doctor_search(request):
    url = "https://qa-gateway.zoylo.com/zoylogateway-0.0.1-SNAPSHOT/zoylodoctor/zoylodoctor-0.0.1-SNAPSHOT//api/doctor-details/client-doctors"

    payload = "{\n    \"gpsLatitude\": 28.653458,\n    \"gpsLongitude\": 77.123767,\n    \"page\": 0,\n    \"size\": 10,\n    \"criteria\": \"Dental\",\n    \"distance\": \"20km\"\n}"
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(url, headers=headers, data=payload)
    return HttpResponse(response)


def doctor_details(request):
    url = "https://qa-gateway.zoylo.com/zoylogateway-0.0.1-SNAPSHOT/zoyloadmin/zoyloadmin-0.0.1-SNAPSHOT/api/doctor-details/client-doctor-details?doctorId=5a26e52aca07621fcc69b609"
    payload = {}
    headers = {}
    response = requests.get(url, headers=headers, data=payload)
    return HttpResponse(response)
