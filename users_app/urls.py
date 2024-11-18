from django.urls import path
from users_app.views import UserCreateView, UserListView, UserDetailView, UserUpdateView
from users_app.apps import UsersAppConfig

app_name = UsersAppConfig.name
urlpatterns = [
    path('', UserListView.as_view(), name='list_user'),
    path('create/', UserCreateView.as_view(), name='create_user'),
    path('view/<int:pk>/', UserDetailView.as_view(), name='view_user'),
    path('edit/<int:pk>/', UserUpdateView.as_view(), name='update_user'),
]