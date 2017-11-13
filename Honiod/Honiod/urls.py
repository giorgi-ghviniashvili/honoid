"""
Definition of urls for Honiod.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views
from django.views.generic import RedirectView
import app.forms
import app.views_en
import app.views_ka
# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', RedirectView.as_view(url='/ka/')),
    url(r'^en/$', app.views_en.home, name='home_en'),
    url(r'^en/contact$', app.views_en.contact, name='contact_en'),
    url(r'^en/about', app.views_en.about, name='about_en'),
    url(r'^en/projects', app.views_en.projects, name='projects_en'),
    url(r'^en/login_en/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app_en/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

     #Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

     #Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
]

urlpatterns += [
    url(r'^ka/$', app.views_ka.home, name='home_ka'),
    url(r'^ka/contact$', app.views_en.contact, name='contact_ka'),
    url(r'^ka/about', app.views_en.about, name='about_ka'),
    url(r'^ka/projects', app.views_en.projects, name='projects_ka'),
]