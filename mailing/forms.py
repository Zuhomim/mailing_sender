from django import forms

from mailing.models import Mailing, Message, Client


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class MailingForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Mailing
        fields = ('start_date', 'end_date', 'message', 'periodicity', 'status')
        widgets = {
            'start_date': forms.TextInput(attrs={'type': 'datetime-local'}),
            'end_date': forms.TextInput(attrs={'type': 'datetime-local'}),
        }


class MailingFormModerator(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Mailing
        fields = ('start_date', 'end_date', 'periodicity', 'status',)


class MessageForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'


class ClientForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
