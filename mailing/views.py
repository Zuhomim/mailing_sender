from django.forms import inlineformset_factory
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView

from mailing.forms import MailingForm, MailingFormModerator, MessageForm
from mailing.models import Mailing, Message


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
    success_url = reverse_lazy('mailing:mailing')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm
    # permission_required = 'mailing.change_mailing'

    def get_success_url(self):
        return reverse('mailing:mailing_update', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        # VersionFormset = inlineformset_factory(Mailing, form=MailingForm, extra=1)
        # formset = VersionFormset(self.request.POST, instance=self.object)

        # VersionFormset = inlineformset_factory(Mailing, Version, form=VersionForm, extra=1)
        # if self.request.method == 'POST':
        #     formset = VersionFormset(self.request.POST, instance=self.object)
        # else:
        #     formset = VersionFormset(instance=self.object)

        # context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)

    def get_form_class(self):
        if self.request.user.groups.filter(name='Модератор').exists():
            return MailingFormModerator
        else:
            return MailingForm

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user and not self.request.user.is_staff:
            raise Http404("Вы не являетесь владельцем этого товара")
        return self.object


class MailingDetailView(DetailView):
    model = Mailing
    template_name = 'mailing/mailing_detail.html'


class MailingDeleteView(DeleteView):
    pass


class MailingListView(ListView):
    model = Mailing
    template_name = 'mailing/mailing_list.html'


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:mailing_create')

