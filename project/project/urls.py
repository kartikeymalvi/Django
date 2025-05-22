"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('home1/<int:pk>', views.home1,name='home1'),
    path('registration/', views.registration,name='registration'),
    path('register/', views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logindata/',views.logindata,name='logindata'),
    path('about/',views.about,name='about'),
    path('package/',views.package,name='package'),
    path('first_5/<int:pk>',views.first_5,name='first_5'),
    path('last_5/<int:pk>',views.last_5,name='last_5'),
    path('all_stu/<int:pk>',views.all_stu,name='all_stu'),
    path('update/<int:pk>/<int:pk1>/',views.update,name='update'),
    path('edit/<int:pk>/<int:pk1>/',views.edit,name='edit'),
    path('delete/<int:pk>/<int:pk1>/',views.delete,name='delete'),
    path('about1/<int:pk>',views.about1,name='about1'),
    path('dashboard/<int:pk>/',views.dashboard,name='dashboard'),
    path('adminpanel/<int:pk>/', views.adminpanel, name='adminpanel'),
    path('search/<int:pk>/', views.search, name='search'),

    
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
