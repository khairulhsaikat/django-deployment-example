from django.urls import path
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    path('',views.index,name='index'),
    path('relative',views.relative,name='relative'),
    path('other',views.other,name='other'),
    path('userpage',views.userpage,name='userpage'),
    path('register',views.register,name='register'),
    path('formpage',views.form_name_view,name='formpage'),
    path('user_login',views.user_login,name='user_login'),
]
