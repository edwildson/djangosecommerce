# coding=utf-8

from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings



def index(request):
    texts = ['Lorem ipsum', 'dolor sit amet', 'consectetur']
    context = {
        'title': 'LolJa Onlaini',
        'texts': texts,
    }
    return render(request, 'index.html', context)


def contact(request):
    success = False
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.send_mail()
        success = True
    else:
        form = ContactForm()
    context = {
        'form': form,
        'success': success
    }
    return render(request, 'contact.html', context)
