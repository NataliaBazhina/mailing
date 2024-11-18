from django .contrib.auth.models import User
from django.views.generic import CreateView,UpdateView, DetailView, ListView
from django.urls import reverse_lazy

import users_app


class UserCreateView(CreateView):
    model = User
    fields = ('username', 'password',)
    template_name = 'users_app/user_form.html'
    success_url = reverse_lazy('clients_app:list_client')

class UserUpdateView(UpdateView):
    model = User
    fields = ('username', 'password',)
    success_url = reverse_lazy('clients_app:list_client')

class UserDetailView(DetailView):
    model = User

class UserListView(ListView):
    model = User
    template_name = 'users_app/user_list.html'