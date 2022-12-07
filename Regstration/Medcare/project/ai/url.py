from django.urls import path,include


from . import views
app_name='ai'
urlpatterns = [
    path('ai',views.ai,name='ai'),
]
