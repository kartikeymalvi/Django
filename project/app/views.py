from django.shortcuts import render,redirect
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

def package(request,pk):
    userdata = Student.objects.get(id=pk)
    userdata = {
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
    packages = Travel.objects.all()

    return render(request, 'package.html', {'packages':packages,'userdata': userdata})


def details(request,pk):
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
    item = Travel.objects.all()
    return render(request, 'details.html', {'item': item,'userdata':userdata})


    

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
    travel=Travel.objects.all()
        
    return render(request,'dashboard.html',{'userdata':userdata,'travel':travel}) 

def first_5(request, pk):
    userdata = Student.objects.get(id=pk)
    data = Booking.objects.all()[0:5]

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
    travels = Travel.objects.all()
    
    return render(request, 'dashboard.html', {
        'userdata': userdata,
        'data': data,
        "travels":travels
    })

def last_5(request, pk):
    userdata = Student.objects.get(id=pk)
    data = Booking.objects.order_by('-id')[:5]
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
    travels = Travel.objects.all()
    return render(request, 'dashboard.html', {
        'userdata': userdata,
        'data': data,
        "travels":travels
    })   


def all_stu(request, pk):
    userdata = Student.objects.get(id=pk)
    data = Booking.objects.all()
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
    travels = Travel.objects.all()
    
    return render(request, 'dashboard.html', {
        'userdata': userdata,
        'data': data,
        "travels":travels
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
  
  updatedata=Booking.objects.get(id=pk1)
  updatedata={
    "id":updatedata.id,
    "place":updatedata.place,
    "user":updatedata.user,
    "booked_at":updatedata.booked_at,
    "price":updatedata.price,

  }
  travels = Travel.objects.all()
  

  return render(request,'dashboard.html',{'userdata':userdata,'updatedata':updatedata,"travels":travels})

def edit(request, pk, pk1):
    student = Student.objects.get(pk=pk)
    booking = Booking.objects.get(pk=pk1)
    travels = Travel.objects.all()

    if request.method == 'POST':
        trip_id = request.POST.get('trip')
        price = request.POST.get('price')
        dob = request.POST.get('dob')

        booking.user = student
        booking.place = Travel.objects.get(pk=trip_id)
        booking.price = price
        booking.booked_at = dob
        booking.save()

        return render(request,"dashboard.html",{
        'userdata': student,
        'updatedata': booking,
        'travels': travels,
        'data': Booking.objects.filter(user=student)
    })  


def delete(request,pk,pk1):
    print(pk,pk1)
    delete=Booking.objects.get(id=pk1)
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


# def search(request, pk):
#     y = request.POST.get('name')  
#     x = Booking.objects.filter(place=y)
#     print(x)
    
#     # z = request.POST.get('date')
#     # print(y,z)    # available_from (date)

#     # filters = Q()


#     # if y:
#     #     filters |= Q(place__icontains=y)
#     # if z:
#     #     filters |= Q(booked_at__icontains=z)

#     # data = Booking.objects.filter(filters)

#     # userdata_obj = Student.objects.get(id=pk)
#     # userdata = {
#     #     "id": userdata_obj.id,
#     #     "username": userdata_obj.username,
#     #     "phone": userdata_obj.phone,
#     #     "dob": userdata_obj.dob,
#     #     "email": userdata_obj.email,
#     #     "image": userdata_obj.profile_pic,
#     #     "file": userdata_obj.resume,
#     #     "education": userdata_obj.subscribe,
#     #     "password": userdata_obj.password,
#     # }

#     # no_data_message = ""
#     # if not data.exists():
#     #     no_data_message = "No trips match your search."
    
#     # travels=Travel.objects.all()
#     # return render(request, 'dashboard.html', {
#     #     'userdata': userdata,
#     #     'data': data,
#     #     'no_data_message': no_data_message,
#     #     "travels":travels
#     # })
 
def book(request, pk, pk1):

    userdata = Student.objects.get(id=pk)
    item = Travel.objects.get(id=pk1)

    if request.method == 'POST':
    
        Booking.objects.create(
        place=item,  # Travel object
        user=userdata,
        price=item.price
        )

        return render(request, 'checkout.html', {
            'item': item,
            'userdata': userdata
        })

    
    return render(request, 'details.html', {
        'item': [item],  # wrap in list so {% for i in item %} works in template
        'userdata': userdata
    })
