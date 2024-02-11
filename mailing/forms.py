from django import forms

from mailing.models import Mailing, Message


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class MailingForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Mailing
        fields = '__all__'
        widgets = {
            'time': forms.TextInput(attrs={'type': 'datetime-local'}),
        }


class MailingFormModerator(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Mailing
        fields = ('time', 'periodicity', 'status',)


class MessageForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
