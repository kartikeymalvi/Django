from django.shortcuts import render
from .models import *
from django.db.models import Q

def home(request):
    return render(request,'home.html')


def home1(request,pk):
    userdata=Student.objects.get(id=pk)
    userdata={
                "id":userdata.id,
                "name":userdata.username,
                "email":userdata.email,
                # detail=detail,
                "phone":userdata.phone,
                "dob":userdata.dob,
                "subscribe":userdata.subscribe,
                "gender":userdata.gender,
                "profile_pic":userdata.profile_pic,
                "resume":userdata.resume,
                "password":userdata.password,
               

    }
    return render(request,'home.html',{'userdata':userdata})

def about1(request,pk):


    userdata=Student.objects.get(id=pk)
    userdata={
                "id":userdata.id,
                "name":userdata.username,
                "email":userdata.email,
                # detail=detail,
                "phone":userdata.phone,
                "dob":userdata.dob,
                "subscribe":userdata.subscribe,
                "gender":userdata.gender,
                "profile_pic":userdata.profile_pic,
                "resume":userdata.resume,
                "password":userdata.password,

             }
    
    return render(request,'about.html',{'userdata':userdata})
def registration(request):
    return render(request,'registration.html') 

def about(request):
    return render(request,'about.html')

def register(request):
    username=request.POST.get('username')
    email=request.POST.get('email')
    detail=request.POST.get('detail')
    phone=request.POST.get('phone')
    dob=request.POST.get('dob')
    subscribe=request.POST.getlist('subscribe')
    gender=request.POST.get('gender')
    profile_pic=request.FILES.get('profile-pic')
    resume=request.FILES.get('resume')
    password=request.POST.get('password')
    cpassword=request.POST.get('cpassword')

    user=Student.objects.filter(email=email)

    if user :
       msg='Email already registerd'
       return render(request,'login.html',{'key':msg})
    else:
        if password==cpassword:
            Student.objects.create(
                username=username,
                email=email,
                # detail=detail,
                phone=phone,
                dob=dob,
                subscribe=subscribe,
                gender=gender,
                profile_pic=profile_pic,
                resume=resume,
                password=password,
                cpassword=cpassword
             ) 

            msg1='registration success please login'
            return render(request,'login.html',{'key1':msg1})
        else:
            msg2='password does not match'
            return render(request,'registration.html',{'key2':msg2})      

def login(request):
    return render(request,'login.html') 

def logindata(request):
     if request.method=='POST':
          email=request.POST.get('email')
          passw=request.POST.get('password')
          print(email,passw)
          user=Student.objects.filter(email=email)
          if user:
               userdata=Student.objects.get(email=email)
              

               pass1=userdata.password
               if pass1==passw:
                    msg='welcome to dasboard'
                    userdata = {
                         "id":userdata.id,
                         "username":userdata.username,
                         "phone":userdata.phone,
                         "dob":userdata.dob,
                         "email":userdata.email,
                         "image":userdata.profile_pic,
                         "file":userdata.resume,
                         "education":userdata.subscribe,
                         "password":userdata.password,
                    }
                    return render(request,'profile.html',{'userdata':userdata})
               else:
                    msg='email and password not found'     
                    return render(request,'login.html',{'msg':msg})

          else:
               msg1='email not registerd'
               return render(request,'login.html',{'msg1':msg1})
     else:
          return render(request,'login.html')

def package(request):
    
    return render(request,'Package.html')

def dashboard(request,pk):
    userdata=Student.objects.get(id=pk)
    userdata={
        "id":userdata.id,
        "username":userdata.username,
        "phone":userdata.phone,
        "dob":userdata.dob,
        "email":userdata.email,
        "image":userdata.profile_pic,
        "file":userdata.resume,
        "education":userdata.subscribe,
        "password":userdata.password,
        }
    return render(request,'dashboard.html',{'userdata':userdata}) 

def first_5(request, pk):
    userdata = Student.objects.get(id=pk)
    data = Travel.objects.all()[0:5]

    userdata={
        "id":userdata.id,
        "username":userdata.username,
        "phone":userdata.phone,
        "dob":userdata.dob,
        "email":userdata.email,
        "image":userdata.profile_pic,
        "file":userdata.resume,
        "education":userdata.subscribe,
        "password":userdata.password,
    }
    
    return render(request, 'dashboard.html', {
        'userdata': userdata,
        'data': data
    })

def last_5(request, pk):
    userdata = Student.objects.get(id=pk)
    data = Travel.objects.order_by('-id')[:5]
    userdata={
        "id":userdata.id,
        "username":userdata.username,
        "phone":userdata.phone,
        "dob":userdata.dob,
        "email":userdata.email,
        "image":userdata.profile_pic,
        "file":userdata.resume,
        "education":userdata.subscribe,
        "password":userdata.password,
    }
    
    return render(request, 'dashboard.html', {
        'userdata': userdata,
        'data': data
    })   


def all_stu(request, pk):
    userdata = Student.objects.get(id=pk)
    data = Travel.objects.all()
    userdata={
        "id":userdata.id,
        "username":userdata.username,
        "phone":userdata.phone,
        "dob":userdata.dob,
        "email":userdata.email,
        "image":userdata.profile_pic,
        "file":userdata.resume,
        "education":userdata.subscribe,
        "password":userdata.password,
    }
    
    return render(request, 'dashboard.html', {
        'userdata': userdata,
        'data': data
    })

def update(request,pk,pk1):
  userdata=Student.objects.get(id=pk)
  userdata={
        "id":userdata.id,
        "username":userdata.username,
        "phone":userdata.phone,
        
        "email":userdata.email,
        "image":userdata.profile_pic,
        "file":userdata.resume,
        "education":userdata.subscribe,
        "password":userdata.password,
  }
  updatedata=Travel.objects.get(id=pk1)
  return render(request,'dashboard.html',{'userdata':userdata,'updatedata':updatedata})

def edit(request,pk,pk1):
    name=request.POST.get('name')
    email=request.POST.get('email')
    contact=request.POST.get('contact')
    dob=request.POST.get('dob')
    
    if request.method=='POST':
        edit=Travel.objects.get(pk=pk1)
        edit.username=name
        edit.email=email
        edit.contact=contact
        edit.dob=dob
        edit.save()
        userdata=Student.objects.get(id=pk)
        userdata={
        "id":userdata.id,
        "username":userdata.username,
        "phone":userdata.phone,
        "dob":userdata.dob,
        "email":userdata.email,
        "image":userdata.profile_pic,
        "file":userdata.resume,
        "education":userdata.subscribe,
        "password":userdata.password,

        }
        return render(request,'dashboard.html',{'userdata': userdata})

def delete(request,pk,pk1):
    print(pk,pk1)
    delete=Travel.objects.get(id=pk1)
    delete.delete()
    userdata=Student.objects.get(id=pk)
    userdata={
        "id":userdata.id,
        "username":userdata.username,
        "phone":userdata.phone,
        "dob":userdata.dob,
        "email":userdata.email,
        "image":userdata.profile_pic,
        "file":userdata.resume,
        "education":userdata.subscribe,
        "password":userdata.password,
        }
    return render(request,'dashboard.html',{'userdata': userdata})
def adminpanel(request, pk):
    userdata = Student.objects.get(id=pk)

    user_dict = {
        "id": userdata.id,
        "username": userdata.username,
        "phone": userdata.phone,
        "dob": userdata.dob,
        "email": userdata.email,
        "image": userdata.profile_pic,
        "file": userdata.resume,
        "education": userdata.subscribe,
        "password": userdata.password,
    }

    return render(request, 'adminpanel.html', {'userdata': user_dict})
def search(request,pk):
    x=request.POST.get('search')
    y=request.POST.get('name')
    z=request.POST.get('date')
    print(x)
    # data=Travel.objects.filter(Q(username__icontains=x)|Q(email__icontains=x)|Q(contact__icontains=x)|Q(dob__icontains=x))

    data=Travel.objects.filter(Q(username__icontains=y)|Q(email__icontains=x)|Q(contact__icontains=x)|Q(dob__icontains=z))

    userdata=Student.objects.get(id=pk)
    userdata={
        "id": userdata.id,
        "username": userdata.username,
        "phone": userdata.phone,
        "dob": userdata.dob,
        "email": userdata.email,
        "image": userdata.profile_pic,
        "file": userdata.resume,
        "education": userdata.subscribe,
        "password": userdata.password,
    }
    return render(request,'dashboard.html',{'userdata': userdata,'data': data})
 

