from django.views.generic import CreateView,UpdateView, ListView, DetailView, DeleteView
from django.urls import reverse_lazy
from clients_app.models import Client


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