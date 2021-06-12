"""djangoecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import os

from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.views.static import serve as serve_static
from django.contrib.auth.views import login, logout
from django.contrib.auth import views as auth_views
from core.views import password_reset, apiGetProducts

from core import views

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contato/$', views.contact, name='contact'),
    url(r'^entrar/$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^sair/$', logout, {'next_page': 'index'}, name='logout'),
    url(r'^conta/', include('accounts.urls', namespace='accounts')),
    url(r'^catalogo/', include('catalog.urls', namespace='catalog')),
    url(r'^admin/', admin.site.urls),
    url(r'^compras/', include('checkout.urls', namespace='checkout')),
    url(r'^paypal/', include('paypal.standard.ipn.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),

    url(r'^reiniciar-senha/$', password_reset,
        {'template_name': BASE_DIR + '/core/templates/registration/password_reset_form.html'},
        name='password_reset'),
    url(r'^reiniciar-senha/confirmacao/$', auth_views.password_reset_done,
        {'template_name': BASE_DIR + '/core/templates/registration/password_reset_done.html'},
        name='password_reset_done'),
    url(r'^reiniciar/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm,
        {'template_name': BASE_DIR + '/core/templates/registration/password_reset_confirm.html'},
        name='password_reset_confirm'),
    url(r'^reiniciar/confirmacao/$', auth_views.password_reset_complete,
        {'template_name': BASE_DIR + '/core/templates/registration/password_reset_complete.html'},
        name='password_reset_complete'),

    #     Acesso externo
    url(r'api/products/', apiGetProducts, name='api_products'),
]
