from django.urls import path
from users_app.apps import UsersAppConfig
from users_app.views import UserCreateView, email_verification, change_password
from django.contrib.auth.views import LoginView, LogoutView


app_name = UsersAppConfig.name
urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('email-confirm/<str:token>/', email_verification, name='email-confirm'),
    path('change_password/',change_password,name="change_password"),
]
