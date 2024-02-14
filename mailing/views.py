from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView

from mailing.forms import MailingForm, MailingFormModerator, MessageForm, ClientForm
from mailing.models import Mailing, Message, Client


def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')
    return render(request, 'contacts/contact_list.html')


def homepage(request):
    return render(request, 'mailing/base.html')


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:list_mailing')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm

    def get_success_url(self):
        return reverse('mailing:view_mailing', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        return context_data

    # def form_valid(self, form):
    #     context_data = self.get_context_data()
    #     formset = context_data['formset']
    #     self.object = form.save()
    #
    #     if formset.is_valid():
    #         formset.instance = self.object
    #         formset.save()
    #     return super().form_valid(form)

    # def get_form_class(self):
    #     if self.request.user.groups.filter(name='Модератор').exists():
    #         return MailingFormModerator
    #     else:
    #         return MailingForm

    # def get_object(self, queryset=None):
    #     self.object = super().get_object(queryset)
    #     if self.object.owner != self.request.user and not self.request.user.is_staff:
    #         raise Http404("Вы не являетесь владельцем этого товара")
    #     return self.object


class MailingDetailView(DetailView):
    model = Mailing
    template_name = 'mailing/mailing_detail.html'


class MailingDeleteView(DeleteView):
    model = Mailing
    fields = '__all__'
    success_url = reverse_lazy('mailing:list_mailing')


class MailingListView(ListView):
    model = Mailing
    template_name = 'mailing/mailing_list.html'


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:list_mailing')


class MessageListView(ListView):
    model = Message
    template_name = 'message/message_list.html'


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm

    def get_success_url(self):
        return reverse('mailing:view_message', args=[self.kwargs.get('pk')])


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    success_url = reverse_lazy('mailing:list_message')


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:list_client')


class ClientListView(ListView):
    model = Client
    template_name = 'mailing/client_list.html'


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm

    def get_success_url(self):
        return reverse('mailing:client_view', args=[self.kwargs.get('pk')])


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('mailing:list_client')
