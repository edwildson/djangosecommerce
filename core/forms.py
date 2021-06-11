from django import forms
from django.core.mail import send_mail
from django.conf import settings
from crispy_forms.helper import FormHelper

class ContactForm(forms.Form):
    name = forms.CharField(label='Nome')
    email = forms.EmailField(label='E-mail')
    message = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_mail(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        message = self.cleaned_data['message']
        mensagem = 'Nome: {0}\n E-mail:{1}\n{2}'.format(name, email, message)
        send_mail('Contato do Django E-commerce', mensagem, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL])