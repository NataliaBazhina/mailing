from django.views.generic import CreateView,UpdateView, ListView, DetailView, DeleteView
from django.urls import reverse_lazy
from clients_app.models import Client
from django.shortcuts import render

def base(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'You have new message from {name}({email}): {message}')
    return render(request, 'clients_app/base.html')

class ClientCreateView(CreateView):
    model = Client
    fields = ('email', 'name', 'surname', 'second_name', 'comment',)
    success_url = reverse_lazy("clients_app:list_client")

class ClientDetailView(DetailView):
    model = Client

class ClientListView(ListView):
    model = Client

class ClientUpdateView(UpdateView):
    model = Client
    fields = ('email', 'name', 'surname', 'second_name', 'comment',)
    success_url = reverse_lazy('clients_app:list_client')

class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('clients_app:list_client')