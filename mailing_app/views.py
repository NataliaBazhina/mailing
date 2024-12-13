from django.views.generic import CreateView,UpdateView, ListView, DetailView, DeleteView
from django.urls import reverse_lazy

from mailing_app.forms import MailingForm
from mailing_app.models import Mail, Mailing


class MailCreateView(CreateView):
    model = Mail
    fields = ('topic', 'content',)
    success_url = reverse_lazy("mailing_app:list_mail")


class MailDetailView(DetailView):
    model = Mail


class MailListView(ListView):
    model = Mail


class MailUpdateView(UpdateView):
    model = Mail
    fields = ('topic', 'content',)
    success_url = reverse_lazy('mailing_app:list_mail')


class MailDeleteView(DeleteView):
    model = Mail
    success_url = reverse_lazy('mailing_app:list_mail')


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy("mailing_app:list_mailing")


class MailingDetailView(DetailView):
    model = Mailing


class MailingListView(ListView):
    model = Mailing


class MailingUpdateView(UpdateView):
    model = Mailing
    fields = ('first_mailing', 'periodicity','status', 'clients', 'mail',)
    success_url = reverse_lazy('mailing_app:list_mailing')


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailing_app:list_mailing')