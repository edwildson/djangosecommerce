# coding=utf-8

from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View, TemplateView, CreateView
from django.contrib.auth import get_user_model
from django.contrib import messages

User = get_user_model()

class IndexView(TemplateView):
    template_name= 'index.html'
    def get_context_data(self, *args, **kwargs):
        texts = ['Lorem ipsum', 'dolor sit amet', 'consectetur']
        context = {
            'title': 'LolJa Onlaini',
            'texts': texts,
        }
        return context
    # def get(self, request):
    #     texts = ['Lorem ipsum', 'dolor sit amet', 'consectetur']
    #     context = {
    #         'title': 'LolJa Onlaini',
    #         'texts': texts,
    #     }
    #     return render(request, 'index.html', context)
# def index(request):
#     texts = ['Lorem ipsum', 'dolor sit amet', 'consectetur']
#     context = {
#         'title': 'LolJa Onlaini',
#         'texts': texts,
#     }
#     return render(request, 'index.html', context)

index = IndexView.as_view()

def contact(request):
    success = False
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.send_mail()
        success = True
    elif request.method == 'POST':
        messages.error(request, 'Formulário inválido')
    context = {
        'form': form,
        'success': success
    }
    return render(request, 'contact.html', context)




# Removido por causa da aplicação accounts
# class RegisterView(CreateView):

#     form_class = UserCreationForm
#     template_name = 'register.html'
#     model = User
#     success_url = reverse_lazy('index')


# register = RegisterView.as_view()