# coding=utf-8
import functools
import warnings

from django.shortcuts import render
from .forms import ContactForm
from catalog.views import Product
from django.views.generic import View, TemplateView, CreateView
from django.contrib.auth import get_user_model
from django.contrib import messages

# Sobrecarga da classe para reiniciar senha
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import resolve_url
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.deprecation import RemovedInDjango20Warning
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_protect
from django.utils.translation import ugettext as _

from django.http import JsonResponse

User = get_user_model()


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        texts = ['Lorem ipsum', 'dolor sit amet', 'consectetur']
        context = {
            'title': 'LolJa Onlaini',
            'texts': texts,
        }
        return context


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


def deprecate_current_app(func):
    """
    Handle deprecation of the current_app parameter of the views.
    """

    @functools.wraps(func)
    def inner(*args, **kwargs):
        if 'current_app' in kwargs:
            warnings.warn(
                "Passing `current_app` as a keyword argument is deprecated. "
                "Instead the caller of `{0}` should set "
                "`request.current_app`.".format(func.__name__),
                RemovedInDjango20Warning
            )
            current_app = kwargs.pop('current_app')
            request = kwargs.get('request', None)
            if request and current_app is not None:
                request.current_app = current_app
        return func(*args, **kwargs)

    return inner


@deprecate_current_app
@csrf_protect
def password_reset(request,
                   template_name='registration/password_reset_form.html',
                   email_template_name='registration/password_reset_email.html',
                   subject_template_name='registration/password_reset_subject.txt',
                   password_reset_form=PasswordResetForm,
                   token_generator=default_token_generator,
                   post_reset_redirect=None,
                   from_email=None,
                   extra_context=None,
                   html_email_template_name=None,
                   extra_email_context=None):
    if post_reset_redirect is None:
        post_reset_redirect = reverse('password_reset_done')
    else:
        post_reset_redirect = resolve_url(post_reset_redirect)
    if request.method == "POST":
        form = password_reset_form(request.POST)
        if form.is_valid():
            opts = {
                'use_https': request.is_secure(),
                'token_generator': token_generator,
                'from_email': from_email,
                'email_template_name': email_template_name,
                'subject_template_name': subject_template_name,
                'request': request,
                'html_email_template_name': html_email_template_name,
                'extra_email_context': extra_email_context,
            }
            form.save(**opts)
            return HttpResponseRedirect(post_reset_redirect)
    else:
        form = password_reset_form()
    context = {
        'form': form,
        'title': _('Password reset'),
    }
    if extra_context is not None:
        context.update(extra_context)

    return TemplateResponse(request, template_name, context)


def apiGetProducts(request):
    if request.method == "GET":
        products = Product.objects.all()
        products_resp = []

        for product in products:
            products_resp.append({
                'name': product.name,
                'score': product.score,
                'description': product.description,
                'price': product.price
            })

        return HttpResponse(JsonResponse({
            'store': "Lolja Online",
            'data': products_resp
        }), content_type='application/json')

    return HttpResponse(JsonResponse({'message': "São aceitas apenas requisições GET."}),
                        content_type='application/json')
