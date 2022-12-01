from django.urls import path,include


from . import views
app_name='pages'
urlpatterns = [
    path('signup',views.signup,name='signup'),
]
