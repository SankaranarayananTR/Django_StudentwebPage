from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache

from Studentapp.models import Course, City, Student


# Create your views here.
def login_fun(request):
    if request.method=='POST':
        user_name = request.POST['txtUsername']
        user_pwd = request.POST['txtpwd']
        u1=authenticate(username=user_name,password=user_pwd)
        if u1 is not None and u1.is_superuser:
            request.session['Uname']=user_name
            login(request,u1)
            return redirect('home')
        else:
            return render(request,'login.html',{'msg':'Username and Password incorrect'})
    else:
        return render(request,'login.html',)


from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def register_fun(request):
    if request.method == "POST":
        user_name = request.POST['username']
        user_pwd = request.POST['pwd']
        user_pwd1 = request.POST['pwd1']
        user_email = request.POST['UserEmail']
        if User.objects.filter(username=user_name).exists():
            return render(request,'register.html',{'mssg':'Use Proper Username and Password'})
        # Convert both passwords to lowercase for case-insensitive comparison
        else:
            if user_pwd.lower() == user_pwd1.lower():
                u1 = User.objects.create_superuser(username=user_name, password=user_pwd, email=user_email)
                u1.save()
                return redirect('log')
            else:
                return render(request, 'register.html', {'msg': 'Please check both passwords for correct format'})
    else:
        return render(request, 'register.html')

@login_required
@never_cache
def home_fun(request):
    return render(request,'home.html',{'data':request.session['Uname']})

@login_required
@never_cache
def addcourse_fun(request):
    if request.method == 'POST':
        c1=Course()
        c1.course_name=request.POST['txtcourse']
        c1.course_duration=request.POST['txtduration']
        c1.course_fees=int(request.POST['txtfees'])
        c1.save()
        return render(request, 'addcourse.html',{'msg':'Sucessfully Added'})
    else:
        return render(request,'addcourse.html')

@login_required
@never_cache
def displaycouse_fun(request):
    course_data=Course.objects.all()  #it will return list of object
    return render(request,'displaycourse.html',{'data':course_data})

@login_required
@never_cache
def update_course(request,courseid):
    c1 = Course.objects.get(id=courseid)
    if request.method == 'POST':
        c1.course_name = request.POST['txtcourse']
        c1.course_duration = request.POST['txtduration']
        c1.course_fees = int(request.POST['txtfees'])
        c1.save()
        return redirect('display_course')
    else:
        return render(request,'updatecourse.html',{'data':c1})

@login_required
@never_cache
def delete_coure(request,courseid):
    c1=Course.objects.get(id=courseid)
    c1.delete()
    return redirect('display_course')

@login_required
@never_cache
def addstudent_fun(request):
    if request.method == 'POST':
        s1 = Student()
        s1.stud_name = request.POST['txtname']
        s1.stud_phno = int(request.POST['txtno'])
        s1.stud_mail = request.POST['txtmail']
        s1.stud_city = City.objects.get(city_name=request.POST['ddlcity'])
        s1.stud_course = Course.objects.get(course_name=request.POST['ddlCourse'])
        s1.paid_fees = int(request.POST['txtpaidfees'])

        c1 = Course.objects.get(course_name=request.POST['ddlCourse'])
        s1.pending_fees = c1.course_fees - s1.paid_fees  # Initialize pending fees

        s1.save()
        return render(request, 'addstudent.html', {'msg': 'Successfully Added'})
    else:
        city = City.objects.all()
        course = Course.objects.all()
        return render(request, 'addstudent.html', {'CityData': city, 'CourseData': course})


@login_required
@never_cache
def displaystudent_fun(request):
    s1=Student.objects.all()
    return render(request,'displaystudent.html',{'student_data':s1})

@login_required
@never_cache
def updatestudent_fun(request,studid):
    s1=Student.objects.get(id=studid)
    if request.method=='POST':
        s1.stud_name = request.POST['txtname']
        s1.stud_phno = int(request.POST['txtno'])
        s1.stud_mail = request.POST['txtmail']
        s1.stud_city = City.objects.get(city_name=request.POST['ddlcity'])
        s1.stud_course = Course.objects.get(course_name=request.POST['ddlCourse'])
        s1.paid_fees = s1.paid_fees + int(request.POST['txtpaidfees'])

        c1 = Course.objects.get(course_name=request.POST['ddlCourse'])
        if s1.pending_fees > 0:
            s1.pending_fees = c1.course_fees - s1.paid_fees
        else:
            s1.pending_fees=0

        s1.save()
        return redirect('displaystudent')
    else:
        city = City.objects.all()
        course = Course.objects.all()
        return render(request,'updatestudent.html',{'student':s1,'CityData':city,'CourseData':course})

@login_required
@never_cache
def deletestudent_fun(request,studid):
    s1=Student.objects.get(id=studid)
    s1.delete()
    return redirect('displaystudent')


def logout_fun(request):
    # del request.session['Uname']
    logout(request)
    return redirect('log')