import operator

from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
from init_test.models import student_score
from subjects.models import suggested_subject, subject


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        username = request.POST['username']
        if User.objects.filter(email=email).exists():
            messages.info(request, 'Email Taken')
            return redirect('register')
        elif first_name == '' or email == '' or password == '' or username == '':
            messages.info(request, 'Re-enter Details')
            return redirect('register')
        elif User.objects.filter(username=username).exists():
            messages.info(request, 'Username already exists')
            return redirect('register')

        else:
            user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name,
                                            last_name=last_name)
            user.save()
            print('user created')
            return redirect('login')
    elif request.method == 'GET':
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        password = request.POST['password']
        username = request.POST['username']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')

    else:

        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def dashboard(request):
    user_id = request.user.id
    if suggested_subject.objects.filter(student_id=user_id).exists():
        global_map = {}
        student_data = student_score.objects.filter(student_id=user_id).values()[0]
        del student_data['id']
        del student_data['student_id']

        for ele in list(student_data):
            if student_data[ele] == False:
                student_data.pop(ele)

        n = len(subject.objects.values())
        for i in range(1, n + 1):
            subject_data = subject.objects.filter(id=i).values()[0]
            del subject_data['id']
            del subject_data['subject_name']

            all_keys = list(student_data.keys())

            counter1 = 0

            for ele in all_keys:
                if subject_data[ele]:
                    counter1 += 1

            global_map[subject.objects.filter(id=i).values()[0]['subject_name']] = counter1

        global_map = dict(sorted(global_map.items(), key=operator.itemgetter(1)))
        global_arr = list(global_map.keys())
        global_arr.reverse()

        return render(request, 'dashboard.html', {'subject': global_arr[:4]})
    else:
        return render(request, 'dashboard.html')
