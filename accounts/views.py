from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect

from django.contrib import messages, auth

from django.contrib.auth.models import User

from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.core.validators import validate_email
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.utils.encoding import force_bytes, force_text
from Userprofile.models import Profile
from .models import Registrations
# Create your views here.


def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':

        # Get form values

        first_name = request.POST['first_name']

        last_name = request.POST['last_name']

        username = request.POST['username']

        email = request.POST['email']

        password = request.POST['password']

        password2 = request.POST['password2']
        mobile_no = request.POST['mobile_no']
        gender = request.POST['gender']

    # Check if passwords match

        if password == password2:
            min_length = 8
            if len(password) < min_length:
                messages.error(
                    request, 'password should have atleast 8 characters')
                return redirect('register')
            else:
                if password.isdigit():
                    messages.error(
                        request, 'password should not all numeric')
                    return redirect('register')

            # Check username
            if User.objects.filter(username=username).exists():

                messages.error(request, 'That username is taken')

                return redirect('register')

            else:

                if User.objects.filter(email=email).exists():

                    messages.error(request, 'That email is being used')

                    return redirect('register')

                else:

                    user = User.objects.create_user(
                        username=username, password=password, email=email, first_name=first_name, last_name=last_name)

                    user.save()
                    u = User.objects.filter(email=email)
                    uid = u[0].id
                    # print(uid)
                    register = Registrations(
                        user_id=uid, mobile_no=mobile_no, gender=gender)
                    register.save()
                    pro = Profile(user_id=uid)
                    pro.save()

                    messages.success(
                        request, 'You are now registered and can log in')

                    return redirect('login')

        else:

            messages.error(request, 'Passwords do not match')

            return redirect('register')

    else:

        return render(request, 'accounts/register.html')


def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:

            auth.login(request, user)

            messages.success(request, 'You are now logged in')

            return redirect('profile')

        else:

            messages.error(request, 'Invalid credentials')

            return redirect('login')

    else:

        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)

        messages.success(request, 'You are now logged out')

        return redirect('index')


def rest_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        randotp = get_random_string(6, allowed_chars='AFB012E345R6CZ')
        if User.objects.filter(email=email).exists():
            # UPDATE User table SET password = 'randopt' WHERE email='email'
            # u=User.objects.filter(email=email).update(password=randotp)
            u = User.objects.get(email=email)
            u.set_password(randotp)
            u.save()
            current_site = get_current_site(request)
            subject, from_email, to = 'reset password', 'anjumkhan88987@gmail.com', email
            text_content = ''
            # html_content = 'Please activate your account <a href="http://' + \
            # current_site.domain + '/activate_email?e='+to+'" target="_blank">Click here</a>'
            html_content = ' Hii your new password is ' + \
                randotp + ' now you can login with this password'
            msg = EmailMultiAlternatives(
                subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            messages.success(
                request, 'we have sent you an email please follow the instructions')

            return redirect('login')
        else:
            messages.error(request, 'Invaild email')
            return redirect('rest_password')
    return render(request, 'accounts/forget_password.html')


def resetpass(request):

    if request.method == 'POST':
        password = request.POST['password']

        password2 = request.POST['password2']

        user_id = request.user.id
        newpassword = User.objects.get(username=request.user.username)
        # newpassword = User.objects.filter(
        # user_id=user_id).update(password=password)
        # newpassword = User.objects.get()

        # Steps
        # Get Values post
        # password1 == password2 check
        # Password update
        # Authenticate - Login user
        # Redirect

        # newpassword = User.objects.get(user_id=user_id)
        # newpassword.set_password('password')
        # newpassword.save()

        if password == password2:

            newpassword.set_password(password)
            newpassword.save()
            user = auth.authenticate(
                username=request.user.username, password=password)

            if user is not None:
                auth.login(request, user)
                messages.success(
                    request, 'Your password was successfully change ')

                return redirect('index')

        else:

            messages.error(request, 'Passwords do not match')
            return redirect('resetpass')

    else:

        return render(request, 'accounts/resetpass.html')
