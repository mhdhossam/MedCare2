from django.urls import path,include


from . import views
app_name='patientlogin'
urlpatterns = [
    path('login',views.login,name='login'),
    path('json', views.json , name= 'json'),
    path('homeuser',views.homeuser,name='homeuser'),
    path('medlogin',views.medlogin,name='medlogin'),
]