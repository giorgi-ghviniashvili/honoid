"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
import json
from django.core.serializers import serialize
from datetime import datetime
from app.models import Project

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app_en/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
            'active':'home',
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app_en/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
            'active':'contact',
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app_en/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
            'active':'about',
        }
    )

def projects(request):
    """Renders the projects page."""
    assert isinstance(request, HttpRequest)
    projects = Project.objects.all()
    return render(
        request,
        'app_en/projects.html',
        {
            'title':'projects',
            'active':'projects',
            'projects': serialize('json', list(projects))
        }
    )
